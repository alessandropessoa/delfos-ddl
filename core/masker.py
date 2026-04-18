#analisador-delfos/core/masker.py
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║             DELFOS v2 · DDL Masker (corrigido)                               ║
╚══════════════════════════════════════════════════════════════════════════════╝

Modos (MaskMode):
  HASH_FULL   — default. Colunas com mesmo nome em tabelas diferentes → MESMO
                hash (cross-table consistency). Ideal para análise com LLMs.
  HASH_SCOPED — hash único por tabela.coluna. Máximo isolamento.
  HASH_ABBREV — 3 chars + hash curto. Ex: TTBH_ae14bf.
  POSITIONAL  — TBL001 / COL001 (ordinal puro, totalmente opaco).
  APPLY       — aplica mapeamento JSON existente sem recalcular.

Bug corrigido (v2.1):
  Colunas entre aspas duplas ("ANO") agora são corretamente substituídas.
  O substituidor faz duas passagens: primeiro "NOME"→"MOCK" (com aspas),
  depois NOME→MOCK (sem aspas, para SELECTs não-quoted).
"""
from __future__ import annotations

import hashlib
import json
import re
import sqlite3
from pathlib import Path

from .abstractions import IMasker, MaskConfig, MaskMode, HashAlgorithm


# ─────────────────────────────────────────────────────────────────────────────
# Helpers de token
# ─────────────────────────────────────────────────────────────────────────────

def _digest(value: str, algo: HashAlgorithm, length: int) -> str:
    h = hashlib.new(algo.value, value.encode()).hexdigest()
    return h[:length] if length > 0 else h

def _token_hash(name: str, prefix: str, cfg: MaskConfig) -> str:
    return f"{prefix}_{_digest(name, cfg.algorithm, cfg.hash_length)}"

def _token_hash_scoped(scope: str, name: str, prefix: str, cfg: MaskConfig) -> str:
    return f"{prefix}_{_digest(f'{scope}.{name}', cfg.algorithm, cfg.hash_length)}"

def _token_abbrev(name: str, prefix: str, cfg: MaskConfig) -> str:
    abbrev = re.sub(r'[^A-Z0-9]', '', name.upper())[:3]
    return f"{prefix}{abbrev}_{_digest(name, cfg.algorithm, 6)}"

def _token_positional(counter: int, prefix: str) -> str:
    return f"{prefix}{counter:03d}"


# ─────────────────────────────────────────────────────────────────────────────
# Extractor de identificadores
# ─────────────────────────────────────────────────────────────────────────────

class _DDLIdentifierExtractor:
    _RE_TABLE_PLAIN = re.compile(
        r'CREATE\s+(?:OR\s+REPLACE\s+)?(?:FORCE\s+)?(?:EDITIONABLE\s+)?'
        r'(?:MATERIALIZED\s+)?(?:TABLE|VIEW)\s+'
        r'"?(?:[A-Z0-9_]+\.)?"?([A-Z0-9_]+)"?',
        re.IGNORECASE,
    )
    _RE_COLUMN_LINE = re.compile(
        r'^\s*"?([A-Za-z0-9_\-\xc0-\xff]+)"?\s+'
        r'(?:VARCHAR2|VARCHAR|NVARCHAR2?|CHAR|NCHAR|NUMBER|INTEGER|INT|'
        r'BIGINT|SMALLINT|FLOAT|REAL|BINARY_DOUBLE|DATE|TIMESTAMP|CLOB|'
        r'BLOB|RAW|LONG|BOOLEAN|TEXT|BIT|MONEY|UNIQUEIDENTIFIER|DECIMAL|NUMERIC)',
        re.IGNORECASE | re.MULTILINE,
    )
    _RE_INDEX = re.compile(r'CREATE\s+(?:UNIQUE\s+)?INDEX\s+"?([A-Z0-9_]+)"?\s+ON', re.IGNORECASE)
    _RE_CONSTRAINT = re.compile(
        r'CONSTRAINT\s+"?([A-Z0-9_]+)"?\s+(?:PRIMARY\s+KEY|FOREIGN\s+KEY|UNIQUE)', re.IGNORECASE)
    _RE_ALTER_CONSTRAINT = re.compile(r'ADD\s+CONSTRAINT\s+"?([A-Z0-9_]+)"?', re.IGNORECASE)

    def extract_tables(self, ddl: str) -> list[str]:
        seen, result = set(), []
        for m in self._RE_TABLE_PLAIN.finditer(ddl):
            name = m.group(1).upper()
            if name not in seen:
                seen.add(name); result.append(name)
        return result

    def extract_columns_for_table(self, body: str) -> list[str]:
        seen, result = set(), []
        for m in self._RE_COLUMN_LINE.finditer(body):
            name = m.group(1).upper()
            if name not in seen:
                seen.add(name); result.append(name)
        return result

    def extract_indexes(self, ddl: str) -> list[str]:
        seen, result = set(), []
        for m in self._RE_INDEX.finditer(ddl):
            name = m.group(1).upper()
            if name not in seen:
                seen.add(name); result.append(name)
        return result

    def extract_constraints(self, ddl: str) -> list[str]:
        seen, result = set(), []
        for pat in (self._RE_CONSTRAINT, self._RE_ALTER_CONSTRAINT):
            for m in pat.finditer(ddl):
                name = m.group(1).upper()
                if name not in seen:
                    seen.add(name); result.append(name)
        return result

    @staticmethod
    def extract_table_bodies(ddl: str) -> dict[str, str]:
        result = {}
        pattern = re.compile(
            r'CREATE\s+TABLE\s+"?(?:[A-Z0-9_]+\.)?"?([A-Z0-9_]+)"?\s*\(', re.IGNORECASE)
        for m in pattern.finditer(ddl):
            name = m.group(1).upper()
            start = m.end()
            depth, i = 1, start
            while i < len(ddl) and depth > 0:
                if ddl[i] == '(':   depth += 1
                elif ddl[i] == ')': depth -= 1
                i += 1
            result[name] = ddl[start:i - 1]
        return result


# ─────────────────────────────────────────────────────────────────────────────
# Gerador de mapeamento
# ─────────────────────────────────────────────────────────────────────────────

class _MappingBuilder:
    """
    Regra de negócio de colunas:
      HASH_FULL  : token = hash(col_name). ANO em TB1 == ANO em TB2.
                   Reutiliza token já gerado se nome da coluna já foi mapeado.
      HASH_SCOPED: token = hash(table.col_name). Cada célula é única.
      Outros modos: token independente por ocorrência.
    """
    def __init__(self, cfg: MaskConfig) -> None:
        self._cfg = cfg
        self._extractor = _DDLIdentifierExtractor()
        self._used: set[str] = set()
        self._counters: dict[str, int] = {}

    def build(self, ddl: str) -> dict:
        cfg = self._cfg
        mapping: dict = {
            "hash_algorithm": cfg.algorithm.value,
            "hash_length":    cfg.hash_length,
            "mask_mode":      cfg.mode.name,
            "tables":         {},
            "columns":        {},
            "indexes":        {},
            "constraints":    {},
        }
        for tbl in self._extractor.extract_tables(ddl):
            mapping["tables"][tbl] = self._tbl_token(tbl)

        tbl_bodies = _DDLIdentifierExtractor.extract_table_bodies(ddl)
        for tbl_name, body in tbl_bodies.items():
            for col in self._extractor.extract_columns_for_table(body):
                key = f"{tbl_name}.{col}"
                mapping["columns"][key] = self._col_token(tbl_name, col, mapping["columns"])

        for idx in self._extractor.extract_indexes(ddl):
            mapping["indexes"][idx] = self._simple_token(idx, "I", "IDX")
        for cst in self._extractor.extract_constraints(ddl):
            mapping["constraints"][cst] = self._simple_token(cst, "K", "CST")

        return mapping

    def _tbl_token(self, name: str) -> str:
        mode = self._cfg.mode
        if mode in (MaskMode.HASH_FULL, MaskMode.HASH_SCOPED):
            c = _token_hash(name, "T", self._cfg)
        elif mode == MaskMode.HASH_ABBREV:
            c = _token_abbrev(name, "T", self._cfg)
        else:
            return _token_positional(self._next("T"), "TBL")
        return self._unique(c, name)

    def _col_token(self, table: str, col: str, existing: dict) -> str:
        mode = self._cfg.mode

        if mode == MaskMode.HASH_FULL:
            # Reutiliza token se o nome da coluna já foi mapeado em qualquer tabela
            for k, v in existing.items():
                if k.split(".", 1)[-1] == col:
                    return v  # mesmo hash — não registra novamente em _used
            c = _token_hash(col, "C", self._cfg)
            return self._unique(c, col)

        if mode == MaskMode.HASH_SCOPED:
            c = _token_hash_scoped(table, col, "C", self._cfg)
            return self._unique(c, f"{table}.{col}")

        if mode == MaskMode.HASH_ABBREV:
            c = _token_abbrev(col, "C", self._cfg)
            return self._unique(c, col)

        if mode == MaskMode.POSITIONAL:
            return _token_positional(self._next("C"), "COL")

        raise ValueError(f"Modo inesperado: {mode}")

    def _simple_token(self, name: str, hp: str, pp: str) -> str:
        mode = self._cfg.mode
        if mode in (MaskMode.HASH_FULL, MaskMode.HASH_SCOPED):
            c = _token_hash(name, hp, self._cfg)
        elif mode == MaskMode.HASH_ABBREV:
            c = _token_abbrev(name, hp, self._cfg)
        else:
            return _token_positional(self._next(hp), pp)
        return self._unique(c, name)

    def _unique(self, candidate: str, name: str) -> str:
        salt, token = 0, candidate
        while token in self._used:
            salt += 1
            base = candidate.rsplit("_", 1)[0]
            token = f"{base}_{_digest(f'{name}_salt{salt}', self._cfg.algorithm, self._cfg.hash_length)}"
        self._used.add(token)
        return token

    def _next(self, key: str) -> int:
        self._counters[key] = self._counters.get(key, 0) + 1
        return self._counters[key]


# ─────────────────────────────────────────────────────────────────────────────
# Flatten: mapeamento → dict plano {ORIGINAL_UPPER → mock}
# ─────────────────────────────────────────────────────────────────────────────

def _flatten_mapping(mapping: dict) -> dict[str, str]:
    """
    HASH_FULL: colunas com mesmo nome têm mesmo mock → flat_map é consistente.
    HASH_SCOPED: colunas com mesmo nome podem ter mocks diferentes; o flat_map
    usa o primeiro encontrado para substituições não-contextuais (fora de CREATE TABLE).
    A substituição contextual dentro de CREATE TABLE é feita pelo _ScopedDDLSubstitutor.
    """
    flat: dict[str, str] = {}
    flat.update(mapping.get("tables", {}))
    flat.update(mapping.get("indexes", {}))
    flat.update(mapping.get("constraints", {}))
    for full_col, mock in mapping.get("columns", {}).items():
        col_name = full_col.split(".", 1)[-1] if "." in full_col else full_col
        if col_name not in flat:
            flat[col_name] = mock
    return flat

def _scoped_col_maps(mapping: dict) -> dict[str, dict[str, str]]:
    """Para HASH_SCOPED: {TABLE_UPPER: {COL_UPPER: mock}}."""
    result: dict[str, dict[str, str]] = {}
    for full_col, mock in mapping.get("columns", {}).items():
        if "." in full_col:
            tbl, col = full_col.split(".", 1)
            result.setdefault(tbl, {})[col] = mock
    return result


# ─────────────────────────────────────────────────────────────────────────────
# Substituidor base — duas passagens (com e sem aspas)
# ─────────────────────────────────────────────────────────────────────────────

class _DDLSubstitutor:
    """
    Corrige o bug das aspas duplas com duas passagens distintas:
      1. "NOME" → "MOCK"   (tokens quotados no DDL Oracle)
      2.  NOME  →  MOCK    (tokens não-quotados: aliases, SELECTs, comentários)
    Ordenação por comprimento decrescente evita substituições parciais.
    """

    def apply(self, text: str, flat_map: dict[str, str]) -> str:
        pairs = sorted(flat_map.items(), key=lambda kv: len(kv[0]), reverse=True)
        # Passagem 1 — com aspas duplas
        for orig, mock in pairs:
            text = re.sub(r'"' + re.escape(orig) + r'"',
                          lambda m, mk=mock: f'"{mk}"', text, flags=re.IGNORECASE)
        # Passagem 2 — sem aspas (word boundary)
        for orig, mock in pairs:
            text = re.sub(r'\b' + re.escape(orig) + r'\b', mock,
                          text, flags=re.IGNORECASE)
        return text

    def apply_reverse(self, text: str, flat_map: dict[str, str]) -> str:
        reverse = {v: k for k, v in flat_map.items()}
        pairs   = sorted(reverse.items(), key=lambda kv: len(kv[0]), reverse=True)
        for mock, orig in pairs:
            text = re.sub(r'"' + re.escape(mock) + r'"',
                          lambda m, o=orig: f'"{o}"', text, flags=re.IGNORECASE)
        for mock, orig in pairs:
            text = re.sub(r'\b' + re.escape(mock) + r'\b', orig,
                          text, flags=re.IGNORECASE)
        return text


# ─────────────────────────────────────────────────────────────────────────────
# Substituidor Scoped — processa colunas por bloco de tabela
# ─────────────────────────────────────────────────────────────────────────────

class _ScopedDDLSubstitutor:
    """
    Para HASH_SCOPED: dentro de cada CREATE TABLE aplica o mapa de colunas
    daquela tabela especificamente, evitando cruzamento entre tabelas.
    """
    def __init__(self) -> None:
        self._base = _DDLSubstitutor()

    def apply(self, ddl: str, mapping: dict) -> str:
        tbl_map   = mapping.get("tables", {})
        idx_map   = mapping.get("indexes", {})
        cst_map   = mapping.get("constraints", {})
        scoped    = _scoped_col_maps(mapping)

        result = self._replace_table_blocks(ddl, tbl_map, scoped)

        # Substitui tabelas/índices/constraints fora dos blocos CREATE TABLE
        global_flat = {**tbl_map, **idx_map, **cst_map}
        result = self._base.apply(result, global_flat)

        # Substitui colunas em contextos fora de CREATE TABLE (FKs, índices, SELECTs)
        flat_cols: dict[str, str] = {}
        for tbl_cols in scoped.values():
            for col, mock in tbl_cols.items():
                if col not in flat_cols:
                    flat_cols[col] = mock
        result = self._base.apply(result, flat_cols)

        return result

    def apply_reverse(self, text: str, mapping: dict) -> str:
        flat = _flatten_mapping(mapping)
        return self._base.apply_reverse(text, flat)

    def _replace_table_blocks(self, ddl: str, tbl_map: dict,
                               scoped: dict[str, dict[str, str]]) -> str:
        RE_CT = re.compile(
            r'(CREATE\s+TABLE\s+"?(?:[A-Z0-9_]+\.)?"?)([A-Z0-9_]+)("?\s*\()',
            re.IGNORECASE,
        )
        parts, last = [], 0
        for m in RE_CT.finditer(ddl):
            tbl_orig = m.group(2).upper()
            tbl_mock = tbl_map.get(tbl_orig, tbl_orig)
            col_map  = scoped.get(tbl_orig, {})
            # corpo da tabela
            start  = m.end()
            depth, i = 1, start
            while i < len(ddl) and depth > 0:
                if ddl[i] == '(':   depth += 1
                elif ddl[i] == ')': depth -= 1
                i += 1
            body        = ddl[start:i - 1]
            body_masked = self._base.apply(body, col_map)
            parts.append(ddl[last:m.start()])
            parts.append(f"{m.group(1)}{tbl_mock}{m.group(3)}{body_masked}")
            last = i - 1  # aponta para o ')' de fechamento
        parts.append(ddl[last:])
        return "".join(parts)


# ─────────────────────────────────────────────────────────────────────────────
# Persistência
# ─────────────────────────────────────────────────────────────────────────────

class _MappingPersistence:
    @staticmethod
    def save_json(mapping: dict, path: Path) -> None:
        path.write_text(json.dumps(mapping, ensure_ascii=False, indent=2), encoding="utf-8")

    @staticmethod
    def load_json(path: Path) -> dict:
        return json.loads(path.read_text(encoding="utf-8"))

    @staticmethod
    def save_sqlite(mapping: dict, path: Path) -> None:
        conn = sqlite3.connect(str(path))
        cur  = conn.cursor()
        cur.executescript("""
            CREATE TABLE IF NOT EXISTS table_map (original TEXT PRIMARY KEY, mock TEXT NOT NULL);
            CREATE TABLE IF NOT EXISTS column_map (table_col TEXT PRIMARY KEY, mock TEXT NOT NULL);
            CREATE TABLE IF NOT EXISTS index_map (original TEXT PRIMARY KEY, mock TEXT NOT NULL);
            CREATE TABLE IF NOT EXISTS constraint_map (original TEXT PRIMARY KEY, mock TEXT NOT NULL);
        """)
        cur.executemany("INSERT OR REPLACE INTO table_map VALUES (?,?)", mapping.get("tables", {}).items())
        cur.executemany("INSERT OR REPLACE INTO column_map VALUES (?,?)", mapping.get("columns", {}).items())
        cur.executemany("INSERT OR REPLACE INTO index_map VALUES (?,?)", mapping.get("indexes", {}).items())
        cur.executemany("INSERT OR REPLACE INTO constraint_map VALUES (?,?)", mapping.get("constraints", {}).items())
        conn.commit(); conn.close()


# ─────────────────────────────────────────────────────────────────────────────
# DDLMasker — fachada pública
# ─────────────────────────────────────────────────────────────────────────────

class DDLMasker(IMasker):
    def __init__(self) -> None:
        self._persistence = _MappingPersistence()
        self._base_sub    = _DDLSubstitutor()
        self._scoped_sub  = _ScopedDDLSubstitutor()

    def mask(self, ddl: str, config: MaskConfig) -> tuple[str, dict]:
        if config.mode == MaskMode.APPLY:
            if config.existing_mapping is None:
                raise ValueError("MaskMode.APPLY requer existing_mapping no config.")
            mapping = self._persistence.load_json(config.existing_mapping)
            return self._apply_mapping_to_ddl(ddl, mapping), mapping

        builder = _MappingBuilder(config)
        mapping = builder.build(ddl)
        masked  = self._apply_mapping_to_ddl(ddl, mapping)
        if config.sqlite_output:
            self._persistence.save_sqlite(mapping, config.sqlite_output)
        return masked, mapping

    def apply_mapping(self, ddl: str, mapping: dict) -> str:
        return self._apply_mapping_to_ddl(ddl, mapping)

    def _apply_mapping_to_ddl(self, ddl: str, mapping: dict) -> str:
        if mapping.get("mask_mode") == MaskMode.HASH_SCOPED.name:
            return self._scoped_sub.apply(ddl, mapping)
        return self._base_sub.apply(ddl, _flatten_mapping(mapping))

    @staticmethod
    def _flatten(mapping: dict) -> dict[str, str]:
        return _flatten_mapping(mapping)


# ─────────────────────────────────────────────────────────────────────────────
# ReportUnmasker
# ─────────────────────────────────────────────────────────────────────────────

class ReportUnmasker:
    def __init__(self) -> None:
        self._base   = _DDLSubstitutor()
        self._scoped = _ScopedDDLSubstitutor()

    def unmask(self, text: str, mapping: dict) -> str:
        if mapping.get("mask_mode") == MaskMode.HASH_SCOPED.name:
            return self._scoped.apply_reverse(text, mapping)
        return self._base.apply_reverse(text, _flatten_mapping(mapping))


# ─────────────────────────────────────────────────────────────────────────────
# I/O helpers
# ─────────────────────────────────────────────────────────────────────────────

def save_mapping(mapping: dict, path: Path) -> None:
    _MappingPersistence.save_json(mapping, path)

def load_mapping(path: Path) -> dict:
    return _MappingPersistence.load_json(path)
