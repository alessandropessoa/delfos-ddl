# analisador-delfos/core/analyzer.py
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║             DELFOS v2 · DDL Analyzer                                         ║
║   Análise estática de esquemas Oracle · PostgreSQL · SQL Server              ║
╚══════════════════════════════════════════════════════════════════════════════╝
Responsabilidade única: receber DDL texto, extrair estrutura e emitir
relatório (terminal ou markdown) + estrutura JSON.

Alterações em relação ao v1:
  - Satisfaz IReportEmitter (Dependency Inversion)
  - ReportGenerator separado do Analyzer (SRP)
  - Nenhuma lógica de I/O de arquivo aqui (delegado ao pipeline)
"""
from __future__ import annotations

import json
import re
import textwrap
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from typing import Literal, Optional

try:
    import sqlglot
    import sqlglot.expressions as exp
    HAS_SQLGLOT = True
except ImportError:
    HAS_SQLGLOT = False

from .abstractions import AnalyzerConfig, IReportEmitter, ReportStyle


# ─────────────────────────────────────────────────────────────────────────────
# Data-classes (inalterados — são contratos de domínio)
# ─────────────────────────────────────────────────────────────────────────────

@dataclass
class ColumnInfo:
    name: str
    data_type: str
    nullable: bool = True
    default: Optional[str] = None
    comment: Optional[str] = None

    @property
    def is_pk_candidate(self) -> bool:
        name_l = self.name.lower()
        return not self.nullable and any(
            kw in name_l for kw in ("id", "cod", "chave", "key", "num", "nr")
        )


@dataclass
class IndexInfo:
    name: str
    table: str
    columns: list[str]
    is_unique: bool = False


@dataclass
class PrimaryKeyInfo:
    constraint_name: str
    table: str
    columns: list[str]


@dataclass
class ForeignKeyInfo:
    constraint_name: str
    from_table: str
    from_columns: list[str]
    to_table: str
    to_columns: list[str]


@dataclass
class CommentInfo:
    target_type: str
    table: str
    column: Optional[str]
    text: str


@dataclass
class TableInfo:
    name: str
    schema: Optional[str] = None
    table_type: str = "TABLE"
    columns: list[ColumnInfo] = field(default_factory=list)
    primary_key: Optional[PrimaryKeyInfo] = None
    tablespace: Optional[str] = None
    storage_type: Optional[str] = None
    mview_sql: Optional[str] = None
    comment: Optional[str] = None

    @property
    def col_count(self) -> int:
        return len(self.columns)

    @property
    def not_null_count(self) -> int:
        return sum(1 for c in self.columns if not c.nullable)

    @property
    def nullable_count(self) -> int:
        return len(self.columns) - self.not_null_count


@dataclass
class JoinEdge:
    left_table: str
    left_col: str
    right_table: str
    right_col: str
    join_type: str
    source_object: str


# ─────────────────────────────────────────────────────────────────────────────
# Tokenizer
# ─────────────────────────────────────────────────────────────────────────────

class DDLTokenizer:
    _LINE_COMMENT  = re.compile(r'--[^\n]*')
    _BLOCK_COMMENT = re.compile(r'/\*.*?\*/', re.DOTALL)

    def tokenize(self, ddl: str) -> list[str]:
        ddl = self._BLOCK_COMMENT.sub(' ', ddl)
        ddl = self._LINE_COMMENT.sub('', ddl)
        return [s.strip() for s in ddl.split(';') if len(s.strip()) > 6]


# ─────────────────────────────────────────────────────────────────────────────
# DDLAnalyzer — extrai estrutura (sem gerar relatório)
# ─────────────────────────────────────────────────────────────────────────────

class DDLAnalyzer:
    _RE_TABLE_WITH_SCHEMA = re.compile(
        r'CREATE\s+TABLE\s+"?([A-Z0-9_]+)"?\."?([A-Z0-9_]+)"?\s*\(', re.IGNORECASE)
    _RE_TABLE_PLAIN = re.compile(
        r'CREATE\s+TABLE\s+"?([A-Z0-9_]+)"?\s*\(', re.IGNORECASE)
    _RE_TABLESPACE = re.compile(r'TABLESPACE\s+"?([A-Z0-9_]+)"?', re.IGNORECASE)
    _RE_COMPRESS   = re.compile(
        r'(ROW STORE COMPRESS ADVANCED|NOCOMPRESS|COMPRESS)', re.IGNORECASE)
    _RE_INLINE_PK  = re.compile(
        r'CONSTRAINT\s+"?([A-Z0-9_]+)"?\s+PRIMARY\s+KEY\s*\(([^)]+)\)', re.IGNORECASE)
    _RE_INLINE_FK  = re.compile(
        r'CONSTRAINT\s+"?([A-Z0-9_]+)"?\s+FOREIGN\s+KEY\s*\(([^)]+)\)'
        r'\s+REFERENCES\s+"?(?:[A-Z0-9_]+\.)?"?([A-Z0-9_]+)"?\s*\(([^)]+)\)',
        re.IGNORECASE)
    _RE_ALTER_PK   = re.compile(
        r'ALTER\s+TABLE\s+"?(?:[A-Z0-9_]+\.)?"?([A-Z0-9_]+)"?\s+'
        r'ADD\s+CONSTRAINT\s+"?([A-Z0-9_]+)"?\s+PRIMARY\s+KEY\s*\(([^)]+)\)',
        re.IGNORECASE)
    _RE_ALTER_FK   = re.compile(
        r'ALTER\s+TABLE\s+"?(?:[A-Z0-9_]+\.)?"?([A-Z0-9_]+)"?\s+'
        r'ADD\s+CONSTRAINT\s+"?([A-Z0-9_]+)"?\s+FOREIGN\s+KEY\s*\(([^)]+)\)'
        r'\s+REFERENCES\s+"?(?:[A-Z0-9_]+\.)?"?([A-Z0-9_]+)"?\s*\(([^)]+)\)',
        re.IGNORECASE)
    _RE_CREATE_INDEX = re.compile(
        r'CREATE\s+(UNIQUE\s+)?INDEX\s+"?([A-Z0-9_]+)"?\s+ON\s+'
        r'"?(?:[A-Z0-9_]+\.)?"?([A-Z0-9_]+)"?\s*\(([^)]+)\)',
        re.IGNORECASE)
    _RE_MV_HEAD    = re.compile(
        r'CREATE\s+(?:MATERIALIZED\s+VIEW)\s+"?(?:[A-Z0-9_]+\.)?"?([A-Z0-9_]+)"?',
        re.IGNORECASE)
    _RE_VIEW_HEAD  = re.compile(
        r'CREATE\s+(?:OR\s+REPLACE\s+)?(?:FORCE\s+)?(?:EDITIONABLE\s+)?VIEW\s+'
        r'"?(?:[A-Z0-9_]+\.)?"?([A-Z0-9_]+)"?',
        re.IGNORECASE)
    _RE_AS_SELECT  = re.compile(r'\bAS\b\s*(SELECT\b.+)', re.IGNORECASE | re.DOTALL)
    _RE_COMMENT_TABLE = re.compile(
        r"COMMENT\s+ON\s+(?:TABLE|MATERIALIZED\s+VIEW)\s+"
        r"\"?(?:[A-Z0-9_]+\.)\"?\"?([A-Z0-9_]+)\"?\s+IS\s+'((?:[^']|'')*)'",
        re.IGNORECASE | re.DOTALL)
    _RE_COMMENT_COL = re.compile(
        r"COMMENT\s+ON\s+COLUMN\s+\"?(?:[A-Z0-9_]+\.)\"?\"?([A-Z0-9_]+)\"?\."
        r"\"?([A-Z0-9_\-\xc0-\xff]+)\"?\s+IS\s+'((?:[^']|'')*)'",
        re.IGNORECASE | re.DOTALL)

    def __init__(self) -> None:
        self.tables:       dict[str, TableInfo]  = {}
        self.indexes:      list[IndexInfo]        = []
        self.foreign_keys: list[ForeignKeyInfo]   = []
        self.comments:     list[CommentInfo]      = []
        self.join_edges:   list[JoinEdge]         = []
        self._tokenizer = DDLTokenizer()

    def analyze(self, ddl: str) -> None:
        for stmt in self._tokenizer.tokenize(ddl):
            self._dispatch(stmt)
        self._apply_comments()
        if HAS_SQLGLOT:
            self._extract_all_joins()

    # ── dispatch ──────────────────────────────────────────────────────────────

    def _dispatch(self, stmt: str) -> None:
        up = stmt.upper().lstrip()
        if up.startswith('CREATE TABLE'):
            self._parse_create_table(stmt)
        elif up.startswith('CREATE MATERIALIZED'):
            self._parse_materialized_view(stmt)
        elif re.match(r'CREATE\s+(OR\s+REPLACE\s+)?(FORCE\s+)?(EDITIONABLE\s+)?VIEW',
                      stmt, re.IGNORECASE):
            self._parse_view(stmt)
        elif up.startswith('CREATE') and 'INDEX' in up:
            self._parse_index(stmt)
        elif up.startswith('ALTER TABLE') and 'PRIMARY KEY' in up:
            self._parse_alter_pk(stmt)
        elif up.startswith('ALTER TABLE') and 'FOREIGN KEY' in up:
            self._parse_alter_fk(stmt)
        elif up.startswith('COMMENT ON'):
            self._parse_comment(stmt)

    # ── parsers (mantidos do v1) ──────────────────────────────────────────────

    def _parse_create_table(self, stmt: str) -> None:
        m_schema = self._RE_TABLE_WITH_SCHEMA.search(stmt)
        m_plain  = self._RE_TABLE_PLAIN.search(stmt)
        if m_schema:
            schema, name = m_schema.group(1), m_schema.group(2)
        elif m_plain:
            schema, name = None, m_plain.group(1)
        else:
            return
        name = name.upper()
        body = self._extract_paren_body(stmt)
        if not body:
            return
        tbl = TableInfo(name=name, schema=schema, table_type='TABLE')
        ts = self._RE_TABLESPACE.search(stmt)
        if ts:
            tbl.tablespace = ts.group(1)
        cs = self._RE_COMPRESS.search(stmt)
        if cs:
            tbl.storage_type = cs.group(1).upper()
        clauses   = self._split_body(body)
        pk_cols:  list[str] = []
        pk_name:  str       = ''
        for clause in clauses:
            clause = clause.strip()
            if not clause:
                continue
            up = clause.upper()
            if re.match(r'CONSTRAINT\s+', clause, re.IGNORECASE) and 'PRIMARY KEY' in up:
                m = self._RE_INLINE_PK.search(clause)
                if m:
                    pk_name = m.group(1)
                    pk_cols = [c.strip().strip('"').upper() for c in m.group(2).split(',')]
                continue
            if re.match(r'CONSTRAINT\s+', clause, re.IGNORECASE) and 'FOREIGN KEY' in up:
                m = self._RE_INLINE_FK.search(clause)
                if m:
                    self.foreign_keys.append(ForeignKeyInfo(
                        constraint_name=m.group(1), from_table=name,
                        from_columns=[c.strip().strip('"').upper() for c in m.group(2).split(',')],
                        to_table=m.group(3).upper(),
                        to_columns=[c.strip().strip('"').upper() for c in m.group(4).split(',')],
                    ))
                continue
            if re.match(
                r'(CONSTRAINT|PCTFREE|PCTUSED|INITRANS|MAXTRANS|STORAGE|TABLESPACE|'
                r'SEGMENT|LOGGING|NOCOMPRESS|ROW\s+STORE|BUFFER_POOL|NO\s+INMEMORY)',
                clause, re.IGNORECASE,
            ):
                continue
            col = self._parse_column(clause)
            if col:
                tbl.columns.append(col)
        if pk_cols:
            tbl.primary_key = PrimaryKeyInfo(
                constraint_name=pk_name, table=name, columns=pk_cols)
        self.tables[name] = tbl

    def _parse_column(self, clause: str) -> Optional[ColumnInfo]:
        m = re.match(
            r'"?([A-Za-z0-9_\-\xc0-\xff]+)"?\s+'
            r'((?:VARCHAR2|VARCHAR|NVARCHAR2?|NVARCHAR|CHAR|NCHAR|NUMBER|INTEGER|INT|'
            r'BIGINT|SMALLINT|FLOAT|REAL|BINARY_DOUBLE|DATE|TIMESTAMP|CLOB|BLOB|'
            r'RAW|LONG|BOOLEAN|TEXT|BIT|MONEY|UNIQUEIDENTIFIER|DECIMAL|NUMERIC)'
            r'(?:\s*\([^)]*\))?)',
            clause, re.IGNORECASE,
        )
        if not m:
            return None
        col_name  = m.group(1).upper()
        data_type = m.group(2).strip()
        rest      = clause[m.end():]
        nullable  = 'NOT NULL' not in rest.upper()
        default   = None
        dm = re.search(
            r'\bDEFAULT\s+(.+?)(?=\s+(?:NOT\s+NULL|ENABLE|CONSTRAINT|$))',
            rest, re.IGNORECASE)
        if dm:
            default = dm.group(1).strip().rstrip(',')
        return ColumnInfo(name=col_name, data_type=data_type,
                          nullable=nullable, default=default)

    def _parse_materialized_view(self, stmt: str) -> None:
        m = self._RE_MV_HEAD.search(stmt)
        if not m:
            return
        name = m.group(1).upper()
        cols: list[ColumnInfo] = []
        col_list_m = re.search(
            r'"?[A-Z0-9_]+"?\s*\(([^)]+)\)\s+(?:SEGMENT|ORGANIZATION|BUILD|REFRESH|AS)',
            stmt, re.IGNORECASE)
        if col_list_m:
            for c in col_list_m.group(1).split(','):
                cn = c.strip().strip('"').upper()
                if cn:
                    cols.append(ColumnInfo(name=cn, data_type='UNKNOWN'))
        as_m     = self._RE_AS_SELECT.search(stmt)
        sql_body = as_m.group(1).strip() if as_m else None
        tbl = TableInfo(name=name, table_type='MATERIALIZED VIEW',
                        columns=cols, mview_sql=sql_body)
        ts = self._RE_TABLESPACE.search(stmt)
        if ts:
            tbl.tablespace = ts.group(1)
        if name not in self.tables:
            self.tables[name] = tbl
        else:
            self.tables[name].table_type = 'MATERIALIZED VIEW'
            self.tables[name].mview_sql  = sql_body

    def _parse_view(self, stmt: str) -> None:
        m = self._RE_VIEW_HEAD.search(stmt)
        if not m:
            return
        name     = m.group(1).upper()
        as_m     = self._RE_AS_SELECT.search(stmt)
        sql_body = as_m.group(1).strip() if as_m else None
        tbl = TableInfo(name=name, table_type='VIEW', mview_sql=sql_body)
        if name not in self.tables:
            self.tables[name] = tbl
        else:
            self.tables[name].table_type = 'VIEW'
            self.tables[name].mview_sql  = sql_body

    def _parse_index(self, stmt: str) -> None:
        m = self._RE_CREATE_INDEX.search(stmt)
        if not m:
            return
        is_unique = bool(m.group(1))
        idx_name  = m.group(2)
        tbl_name  = m.group(3).upper()
        cols = []
        for c in m.group(4).split(','):
            col = re.sub(r'\s+(ASC|DESC)\s*$', '', c.strip(), flags=re.IGNORECASE)
            col = col.strip().strip('"').upper()
            if col:
                cols.append(col)
        self.indexes.append(IndexInfo(name=idx_name, table=tbl_name,
                                      columns=cols, is_unique=is_unique))

    def _parse_alter_pk(self, stmt: str) -> None:
        m = self._RE_ALTER_PK.search(stmt)
        if not m:
            return
        tbl_name = m.group(1).upper()
        pk = PrimaryKeyInfo(
            constraint_name=m.group(2), table=tbl_name,
            columns=[c.strip().strip('"').upper() for c in m.group(3).split(',')])
        if tbl_name in self.tables:
            self.tables[tbl_name].primary_key = pk
        else:
            tbl = TableInfo(name=tbl_name, table_type='TABLE')
            tbl.primary_key = pk
            self.tables[tbl_name] = tbl

    def _parse_alter_fk(self, stmt: str) -> None:
        m = self._RE_ALTER_FK.search(stmt)
        if not m:
            return
        self.foreign_keys.append(ForeignKeyInfo(
            constraint_name=m.group(2),
            from_table=m.group(1).upper(),
            from_columns=[c.strip().strip('"').upper() for c in m.group(3).split(',')],
            to_table=m.group(4).upper(),
            to_columns=[c.strip().strip('"').upper() for c in m.group(5).split(',')],
        ))

    def _parse_comment(self, stmt: str) -> None:
        m = self._RE_COMMENT_TABLE.search(stmt)
        if m:
            self.comments.append(CommentInfo(
                target_type='TABLE', table=m.group(1).upper(),
                column=None, text=m.group(2).replace("''", "'")))
            return
        m = self._RE_COMMENT_COL.search(stmt)
        if m:
            self.comments.append(CommentInfo(
                target_type='COLUMN', table=m.group(1).upper(),
                column=m.group(2).upper(), text=m.group(3).replace("''", "'")))

    def _apply_comments(self) -> None:
        for c in self.comments:
            tbl = self.tables.get(c.table)
            if not tbl:
                continue
            if c.target_type == 'TABLE':
                tbl.comment = c.text
            elif c.target_type == 'COLUMN' and c.column:
                for col in tbl.columns:
                    if col.name == c.column:
                        col.comment = c.text
                        break

    def _extract_all_joins(self) -> None:
        for obj in self.tables.values():
            if obj.mview_sql:
                self._extract_joins_from_sql(obj.mview_sql, obj.name)

    def _extract_joins_from_sql(self, sql: str, source: str) -> None:
        try:
            trees = sqlglot.parse(sql, error_level=sqlglot.ErrorLevel.IGNORE)
        except Exception:
            return
        for tree in trees:
            if tree is None:
                continue
            alias_map: dict[str, str] = {}
            for tbl_exp in tree.find_all(exp.Table):
                tbl_name = tbl_exp.name.upper() if tbl_exp.name else ''
                alias    = (tbl_exp.alias or '').upper()
                if tbl_name:
                    alias_map[tbl_name] = tbl_name
                    if alias:
                        alias_map[alias] = tbl_name
            for join in tree.find_all(exp.Join):
                join_type = 'INNER'
                if join.args.get('side'):
                    join_type = str(join.args['side']).upper()
                on = join.args.get('on')
                if on:
                    self._walk_on(on, alias_map, source, join_type)

    def _walk_on(self, node, alias_map: dict, source: str, jtype: str) -> None:
        if isinstance(node, exp.And):
            self._walk_on(node.left,  alias_map, source, jtype)
            self._walk_on(node.right, alias_map, source, jtype)
        elif isinstance(node, exp.EQ):
            l, r = node.left, node.right
            if isinstance(l, exp.Column) and isinstance(r, exp.Column):
                lt = alias_map.get((l.table or '').upper(), (l.table or '').upper())
                rt = alias_map.get((r.table or '').upper(), (r.table or '').upper())
                if lt and rt and lt != rt:
                    self.join_edges.append(JoinEdge(
                        left_table=lt, left_col=l.name.upper(),
                        right_table=rt, right_col=r.name.upper(),
                        join_type=jtype, source_object=source))

    # ── helpers ───────────────────────────────────────────────────────────────

    def _extract_paren_body(self, stmt: str) -> Optional[str]:
        depth, start = 0, None
        for i, ch in enumerate(stmt):
            if ch == '(':
                if depth == 0:
                    start = i + 1
                depth += 1
            elif ch == ')':
                depth -= 1
                if depth == 0 and start is not None:
                    return stmt[start:i]
        return None

    def _split_body(self, body: str) -> list[str]:
        clauses, depth, current = [], 0, []
        for ch in body:
            if ch == '(':
                depth += 1
                current.append(ch)
            elif ch == ')':
                depth -= 1
                current.append(ch)
            elif ch == ',' and depth == 0:
                clauses.append(''.join(current).strip())
                current = []
            else:
                current.append(ch)
        if current:
            clauses.append(''.join(current).strip())
        return clauses

    def table_join_stats(self) -> dict[str, int]:
        c: Counter = Counter()
        for e in self.join_edges:
            c[e.left_table]  += 1
            c[e.right_table] += 1
        return dict(c.most_common())

    def column_join_stats(self) -> dict[str, int]:
        c: Counter = Counter()
        for e in self.join_edges:
            c[f"{e.left_table}.{e.left_col}"]   += 1
            c[f"{e.right_table}.{e.right_col}"]  += 1
        return dict(c.most_common())

    def to_dict(self) -> dict:
        return {
            "tables": {
                name: {
                    "type":       tbl.table_type,
                    "schema":     tbl.schema,
                    "tablespace": tbl.tablespace,
                    "comment":    tbl.comment,
                    "columns": [{
                        "name":     c.name, "type": c.data_type,
                        "nullable": c.nullable, "default": c.default,
                        "comment":  c.comment,
                    } for c in tbl.columns],
                    "primary_key": {
                        "constraint": tbl.primary_key.constraint_name,
                        "columns":    tbl.primary_key.columns,
                    } if tbl.primary_key else None,
                }
                for name, tbl in sorted(self.tables.items())
            },
            "indexes": [
                {"name": i.name, "table": i.table,
                 "columns": i.columns, "unique": i.is_unique}
                for i in self.indexes
            ],
            "foreign_keys": [
                {"constraint": fk.constraint_name,
                 "from_table": fk.from_table, "from_columns": fk.from_columns,
                 "to_table":   fk.to_table,   "to_columns":   fk.to_columns}
                for fk in self.foreign_keys
            ],
            "join_statistics": {
                "table_join_frequency":  self.table_join_stats(),
                "column_join_frequency": self.column_join_stats(),
            } if HAS_SQLGLOT else None,
        }


# ─────────────────────────────────────────────────────────────────────────────
# ReportGenerator — gera texto (SRP: só renderiza)
# ─────────────────────────────────────────────────────────────────────────────

class ReportGenerator:
    def __init__(self, analyzer: DDLAnalyzer,
                 style: Literal['terminal', 'markdown'] = 'terminal') -> None:
        self.az    = analyzer
        self.style = style
        self._lines: list[str] = []

    def build(self) -> str:
        self._lines = []
        if self.style == 'markdown':
            self._md_disclaimer()
            self._md_summary()
            self._md_tables()
            self._md_indexes()
            self._md_primary_keys()
            self._md_foreign_keys()
            self._md_comments()
            if HAS_SQLGLOT and self.az.join_edges:
                self._md_joins()
        else:
            self._t_disclaimer()
            self._t_summary()
            self._t_tables()
            self._t_indexes()
            self._t_primary_keys()
            self._t_foreign_keys()
            self._t_comments()
            if HAS_SQLGLOT and self.az.join_edges:
                self._t_joins()
        return '\n'.join(self._lines)

    # ── terminal ──────────────────────────────────────────────────────────────

    def _t_disclaimer(self) -> None:
        self._w(textwrap.dedent("""\
        ╔══════════════════════════════════════════════════════════════════════════════╗
        ║                    ⚠  DISCLAIMER — ANÁLISE ESTÁTICA DE DDL                 ║
        ╠══════════════════════════════════════════════════════════════════════════════╣
        ║  Esta análise é puramente ESTRUTURAL, baseada no DDL (schema estático).     ║
        ║  Sem acesso ao banco populado, NÃO é possível inferir:                      ║
        ║  1. CONSISTÊNCIA DAS REGRAS DE NEGÓCIO                                      ║
        ║  2. NORMALIZAÇÃO REAL DAS COLUNAS                                           ║
        ║  3. CANDIDATOS REAIS A ÍNDICE B-TREE                                        ║
        ║  ➜ Use estatísticas reais do banco para validação.                          ║
        ╚══════════════════════════════════════════════════════════════════════════════╝
        """))

    def _t_summary(self) -> None:
        az     = self.az
        tables = [t for t in az.tables.values() if t.table_type == 'TABLE']
        mvs    = [t for t in az.tables.values() if t.table_type == 'MATERIALIZED VIEW']
        views  = [t for t in az.tables.values() if t.table_type == 'VIEW']
        self._h1("SUMÁRIO GERAL")
        self._w(f"  Tabelas físicas          : {len(tables)}")
        self._w(f"  Materialized Views       : {len(mvs)}")
        self._w(f"  Views                    : {len(views)}")
        self._w(f"  Índices explícitos       : {len(az.indexes)}")
        self._w(f"  Chaves primárias         : {sum(1 for t in tables if t.primary_key)}")
        self._w(f"  Chaves estrangeiras (FK) : {len(az.foreign_keys)}")
        tc = len([c for c in az.comments if c.target_type == 'TABLE'])
        cc = len([c for c in az.comments if c.target_type == 'COLUMN'])
        self._w(f"  Comentários de tabela    : {tc}")
        self._w(f"  Comentários de coluna    : {cc}")
        if HAS_SQLGLOT:
            self._w(f"  Arestas de join (SQL)    : {len(az.join_edges)}")
        else:
            self._w("  Análise de joins         : [instale sqlglot para habilitar]")
        no_pk = [t.name for t in tables if not t.primary_key]
        if no_pk:
            self._w(f"\n  ⚠  Tabelas SEM chave primária ({len(no_pk)}):")
            for n in sorted(no_pk):
                self._w(f"       {n}")
        self._w("")

    def _t_tables(self) -> None:
        self._h1("TABELAS — DETALHAMENTO DE COLUNAS")
        for obj_type, label in [('TABLE','Tabela'),
                                  ('MATERIALIZED VIEW','Materialized View'),
                                  ('VIEW','View')]:
            objs = sorted([t for t in self.az.tables.values()
                           if t.table_type == obj_type], key=lambda t: t.name)
            if not objs:
                continue
            self._h2(f"{label}s ({len(objs)})")
            for tbl in objs:
                self._t_one_table(tbl)

    def _t_one_table(self, tbl: TableInfo) -> None:
        pk_cols = set(tbl.primary_key.columns) if tbl.primary_key else set()
        idx_cols: set[str] = set()
        for idx in self.az.indexes:
            if idx.table == tbl.name:
                idx_cols.update(idx.columns)
        self._w(f"\n  ┌─ {tbl.name}")
        if tbl.comment:
            self._w(f"  │  📝 {tbl.comment[:100]}")
        if tbl.tablespace:
            self._w(f"  │  Tablespace: {tbl.tablespace}  |  Storage: {tbl.storage_type or '—'}")
        if tbl.primary_key:
            self._w(f"  │  PK [{tbl.primary_key.constraint_name}]: {', '.join(tbl.primary_key.columns)}")
        if not tbl.columns:
            self._w("  │  (nenhuma coluna extraída — verificar DDL)")
        else:
            self._w(f"  │  {'COLUNA':<35} {'TIPO':<25} {'NULL?':<7} {'PK':^4} {'IDX':^4} {'DEFAULT':<20}")
            self._w(f"  │  {'─'*35} {'─'*25} {'─'*7} {'─'*4} {'─'*4} {'─'*20}")
            for col in tbl.columns:
                pk_f = '●' if col.name in pk_cols else ''
                ix_f = '◆' if col.name in idx_cols else ''
                ns   = 'YES' if col.nullable else 'NO'
                ds   = (col.default or '')[:20]
                self._w(f"  │  {col.name:<35} {col.data_type:<25} {ns:<7} {pk_f:^4} {ix_f:^4} {ds:<20}")
                if col.comment:
                    self._w(f"  │      └─ 💬 {col.comment[:90]}")
        self._w(f"  └{'─'*60}")

    def _t_indexes(self) -> None:
        if not self.az.indexes:
            return
        self._h1("ÍNDICES EXPLÍCITOS")
        by_tbl: dict[str, list[IndexInfo]] = defaultdict(list)
        for idx in self.az.indexes:
            by_tbl[idx.table].append(idx)
        for tbl_name in sorted(by_tbl):
            self._w(f"\n  {tbl_name}")
            for idx in by_tbl[tbl_name]:
                uq = '[UNIQUE]' if idx.is_unique else '       '
                self._w(f"    {uq}  {idx.name:<45} → {', '.join(idx.columns)}")
        self._w("")

    def _t_primary_keys(self) -> None:
        pks = [(t.name, t.primary_key) for t in self.az.tables.values() if t.primary_key]
        if not pks:
            return
        self._h1("CHAVES PRIMÁRIAS")
        self._w(f"  {'TABELA':<40} {'CONSTRAINT':<40} {'COLUNAS'}")
        self._w(f"  {'─'*40} {'─'*40} {'─'*30}")
        for n, pk in sorted(pks, key=lambda x: x[0]):
            self._w(f"  {n:<40} {pk.constraint_name:<40} {', '.join(pk.columns)}")
        self._w("")

    def _t_foreign_keys(self) -> None:
        if not self.az.foreign_keys:
            self._h1("RELACIONAMENTOS (FOREIGN KEYS)")
            self._w("  Nenhuma FK explícita encontrada no DDL.")
            self._w("")
            return
        self._h1("RELACIONAMENTOS — FOREIGN KEYS")
        for fk in sorted(self.az.foreign_keys, key=lambda f: f.from_table):
            self._w(f"  {fk.from_table}({', '.join(fk.from_columns)})  →  "
                    f"{fk.to_table}({', '.join(fk.to_columns)})  [{fk.constraint_name}]")
        self._w("")

    def _t_comments(self) -> None:
        tc = [c for c in self.az.comments if c.target_type == 'TABLE']
        cc = [c for c in self.az.comments if c.target_type == 'COLUMN']
        if not tc and not cc:
            return
        self._h1("COBERTURA DE COMENTÁRIOS")
        if tc:
            self._w("  Comentários de objeto:")
            for c in sorted(tc, key=lambda x: x.table):
                self._w(f"    {c.table:<45} {c.text[:70]}")
        self._w("")
        if cc:
            by_tbl: dict[str, list[CommentInfo]] = defaultdict(list)
            for c in cc:
                by_tbl[c.table].append(c)
            self._w("  Colunas comentadas por tabela:")
            for tbl_name in sorted(by_tbl):
                tbl   = self.az.tables.get(tbl_name)
                total = tbl.col_count if tbl else '?'
                self._w(f"    {tbl_name:<45} {len(by_tbl[tbl_name])}/{total}")
        self._w("")

    def _t_joins(self) -> None:
        self._h1("ANÁLISE DE JOINS (extraída dos SQLs de Views / MVs)")
        for tbl_name, count in sorted(self.az.table_join_stats().items(),
                                      key=lambda x: -x[1])[:20]:
            bar = '█' * min(count, 30)
            self._w(f"  {tbl_name:<45} {count:>5}  {bar}")
        self._w("")

    # ── markdown ──────────────────────────────────────────────────────────────

    def _md_disclaimer(self) -> None:
        for line in [
            "> ⚠️ **DISCLAIMER — ANÁLISE ESTÁTICA DE DDL**", "> ",
            "> Esta análise é puramente ESTRUTURAL, baseada no DDL (schema estático).",
            "> Sem acesso ao banco populado, NÃO é possível inferir:", "> ",
            "> 1. **Consistência das regras de negócio**",
            "> 2. **Normalização real das colunas**",
            "> 3. **Candidatos reais a índice B‑tree**", "> ",
            "> ➜ Use estatísticas reais do banco para validação.", "",
        ]:
            self._w(line)

    def _md_summary(self) -> None:
        az     = self.az
        tables = [t for t in az.tables.values() if t.table_type == 'TABLE']
        mvs    = [t for t in az.tables.values() if t.table_type == 'MATERIALIZED VIEW']
        views  = [t for t in az.tables.values() if t.table_type == 'VIEW']
        self._mh1("SUMÁRIO GERAL", "📊")
        rows = [
            ("Tabelas físicas",         len(tables)),
            ("Materialized Views",       len(mvs)),
            ("Views",                    len(views)),
            ("Índices explícitos",       len(az.indexes)),
            ("Chaves primárias",         sum(1 for t in tables if t.primary_key)),
            ("Chaves estrangeiras (FK)", len(az.foreign_keys)),
            ("Comentários de tabela",    len([c for c in az.comments if c.target_type=='TABLE'])),
            ("Comentários de coluna",    len([c for c in az.comments if c.target_type=='COLUMN'])),
        ]
        if HAS_SQLGLOT:
            rows.append(("Arestas de join (SQL)", len(az.join_edges)))
        else:
            rows.append(("Análise de joins", "⚠️ sqlglot não instalado"))
        self._w("| Métrica | Valor |")
        self._w("|---------|-------|")
        for label, val in rows:
            self._w(f"| {label} | {val} |")
        self._w("")
        no_pk = [t.name for t in tables if not t.primary_key]
        if no_pk:
            self._w(f"> ⚠️ **Tabelas sem chave primária ({len(no_pk)}):**")
            for n in sorted(no_pk):
                self._w(f"> - `{n}`")
            self._w("")

    def _md_tables(self) -> None:
        self._mh1("TABELAS — DETALHAMENTO DE COLUNAS", "🗃️")
        for obj_type, label, icon in [
            ('TABLE', 'Tabela', '📌'),
            ('MATERIALIZED VIEW', 'Materialized View', '🧊'),
            ('VIEW', 'View', '👁️'),
        ]:
            objs = sorted([t for t in self.az.tables.values()
                           if t.table_type == obj_type], key=lambda t: t.name)
            if not objs:
                continue
            self._mh2(f"{label}s ({len(objs)})", icon)
            for tbl in objs:
                self._md_one_table(tbl)

    def _md_one_table(self, tbl: TableInfo) -> None:
        pk_cols = set(tbl.primary_key.columns) if tbl.primary_key else set()
        idx_cols: set[str] = set()
        for idx in self.az.indexes:
            if idx.table == tbl.name:
                idx_cols.update(idx.columns)
        self._mh3(f"`{tbl.name}`")
        if tbl.comment:
            self._w(f"> 💬 {tbl.comment}")
        if tbl.tablespace:
            self._w(f"- **Tablespace:** `{tbl.tablespace}`")
        if tbl.storage_type:
            self._w(f"- **Storage:** `{tbl.storage_type}`")
        if tbl.primary_key:
            self._w(f"- **PK:** `{', '.join(tbl.primary_key.columns)}` (`{tbl.primary_key.constraint_name}`)")
        self._w("")
        if not tbl.columns:
            self._w("*(nenhuma coluna extraída)*")
        else:
            self._w("| Coluna | Tipo | NULL? | PK | IDX | DEFAULT |")
            self._w("|--------|------|-------|----|-----|---------|")
            for col in tbl.columns:
                pk_f = "✅" if col.name in pk_cols else ""
                ix_f = "🔍" if col.name in idx_cols else ""
                ds   = f"`{col.default}`" if col.default else ""
                ns   = "YES" if col.nullable else "NO"
                self._w(f"| `{col.name}` | `{col.data_type}` | {ns} | {pk_f} | {ix_f} | {ds} |")
                if col.comment:
                    self._w(f"| | | | | | 💬 _{col.comment}_ |")
        self._w("")

    def _md_indexes(self) -> None:
        if not self.az.indexes:
            return
        self._mh1("ÍNDICES EXPLÍCITOS", "📇")
        by_tbl: dict[str, list[IndexInfo]] = defaultdict(list)
        for idx in self.az.indexes:
            by_tbl[idx.table].append(idx)
        for tbl_name in sorted(by_tbl):
            self._mh3(f"`{tbl_name}`")
            self._w("| Nome do Índice | Colunas | Único? |")
            self._w("|----------------|---------|--------|")
            for idx in by_tbl[tbl_name]:
                uq   = "🔒 UNIQUE" if idx.is_unique else ""
                cols = "`, `".join(idx.columns)
                self._w(f"| `{idx.name}` | `{cols}` | {uq} |")
            self._w("")

    def _md_primary_keys(self) -> None:
        pks = [(t.name, t.primary_key) for t in self.az.tables.values() if t.primary_key]
        if not pks:
            return
        self._mh1("CHAVES PRIMÁRIAS", "🔑")
        self._w("| Tabela | Constraint | Colunas |")
        self._w("|--------|------------|---------|")
        for n, pk in sorted(pks, key=lambda x: x[0]):
            cols = "`, `".join(pk.columns)
            self._w(f"| `{n}` | `{pk.constraint_name}` | `{cols}` |")
        self._w("")

    def _md_foreign_keys(self) -> None:
        if not self.az.foreign_keys:
            self._mh1("RELACIONAMENTOS (FOREIGN KEYS)", "🔗")
            self._w("Nenhuma FK explícita encontrada no DDL.")
            self._w("> ℹ️ Verifique a seção 'Análise de Joins'.")
            self._w("")
            return
        self._mh1("RELACIONAMENTOS — FOREIGN KEYS", "🔗")
        self._w("| Tabela Origem | Coluna(s) | Tabela Destino | Coluna(s) | Constraint |")
        self._w("|---------------|-----------|----------------|-----------|------------|")
        for fk in sorted(self.az.foreign_keys, key=lambda f: f.from_table):
            fc = "`, `".join(fk.from_columns)
            tc = "`, `".join(fk.to_columns)
            self._w(f"| `{fk.from_table}` | `{fc}` | `{fk.to_table}` | `{tc}` | `{fk.constraint_name}` |")
        self._w("")

    def _md_comments(self) -> None:
        tc = [c for c in self.az.comments if c.target_type == 'TABLE']
        cc = [c for c in self.az.comments if c.target_type == 'COLUMN']
        if not tc and not cc:
            return
        self._mh1("COBERTURA DE COMENTÁRIOS", "💬")
        if tc:
            self._mh2("Comentários de Objeto", "📝")
            self._w("| Tabela | Comentário |")
            self._w("|--------|------------|")
            for c in sorted(tc, key=lambda x: x.table):
                self._w(f"| `{c.table}` | {c.text.replace('|','\\|')[:70]} |")
            self._w("")
        if cc:
            self._mh2("Colunas por Tabela", "📋")
            self._w("| Tabela | Cobertura |")
            self._w("|--------|-----------|")
            by_tbl: dict[str, list[CommentInfo]] = defaultdict(list)
            for c in cc:
                by_tbl[c.table].append(c)
            for tbl_name in sorted(by_tbl):
                tbl   = self.az.tables.get(tbl_name)
                total = tbl.col_count if tbl else '?'
                self._w(f"| `{tbl_name}` | {len(by_tbl[tbl_name])}/{total} |")
            self._w("")

    def _md_joins(self) -> None:
        self._mh1("ANÁLISE DE JOINS", "🕸️")
        self._w("*Extraída dos SQLs de Views e Materialized Views*")
        self._w("")
        tbl_stats = self.az.table_join_stats()
        if tbl_stats:
            self._mh2("Tabelas mais referenciadas", "🔥")
            self._w("| Tabela | Aparições |")
            self._w("|--------|-----------|")
            for n, count in sorted(tbl_stats.items(), key=lambda x: -x[1])[:20]:
                self._w(f"| `{n}` | {count} |")
            self._w("")
        col_stats = self.az.column_join_stats()
        if col_stats:
            self._mh2("Colunas em condição de JOIN (candidatas a índice)", "🎯")
            self._w("| Tabela.Coluna | Freq |")
            self._w("|---------------|------|")
            for ck, count in sorted(col_stats.items(), key=lambda x: -x[1])[:30]:
                self._w(f"| `{ck}` | {count} |")
            self._w("")
        pairs: Counter = Counter()
        for edge in self.az.join_edges:
            pairs[tuple(sorted([edge.left_table, edge.right_table]))] += 1
        if pairs:
            self._mh2("Pares de tabelas mais frequentes", "🔁")
            self._w("| Tabela A | Tabela B | Ocorrências |")
            self._w("|----------|----------|-------------|")
            for (t1, t2), count in pairs.most_common(15):
                self._w(f"| `{t1}` | `{t2}` | {count} |")
            self._w("")

    # ── helpers compartilhados ────────────────────────────────────────────────

    def _h1(self, title: str) -> None:
        self._w(f"\n{'═'*80}")
        self._w(f"  {title.upper()}")
        self._w('═'*80)

    def _h2(self, title: str) -> None:
        self._w(f"\n  ── {title} {'─'*(72-len(title))}")

    def _mh1(self, title: str, icon: str = "") -> None:
        p = f"{icon} " if icon else ""
        self._w(f"## {p}{title}")
        self._w("")

    def _mh2(self, title: str, icon: str = "") -> None:
        p = f"{icon} " if icon else ""
        self._w(f"### {p}{title}")
        self._w("")

    def _mh3(self, title: str) -> None:
        self._w(f"#### {title}")
        self._w("")

    def _w(self, line: str = '') -> None:
        self._lines.append(line)


# ─────────────────────────────────────────────────────────────────────────────
# Fachada — implementa IReportEmitter (Open/Closed + Dependency Inversion)
# ─────────────────────────────────────────────────────────────────────────────

class DDLReportEmitter(IReportEmitter):
    """
    Fachada que combina DDLAnalyzer + ReportGenerator.
    Expõe emit(ddl, config) → (report_text, json_structure).
    """

    def emit(self, ddl: str, config: AnalyzerConfig) -> tuple[str, dict]:
        analyzer = DDLAnalyzer()
        analyzer.analyze(ddl)
        style    = config.style.value      # 'terminal' | 'markdown'
        generator = ReportGenerator(analyzer, style=style)
        report    = generator.build()
        json_data = analyzer.to_dict() if config.emit_json else {}
        return report, json_data
