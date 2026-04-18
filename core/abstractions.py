#  analisador-delfos/core/abstractions.py
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║             DELFOS v2 · Core Abstractions                                    ║
║   Contratos base (ABC) — SOLID: Dependency Inversion + Open/Closed           ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum, auto
from pathlib import Path
from typing import Optional


# ─────────────────────────────────────────────────────────────────────────────
# Enumerações de controle
# ─────────────────────────────────────────────────────────────────────────────

class MaskMode(Enum):
    """
    Modos de operação do mascarador.

    HASH_FULL   – substitui nome completo por hash prefixado (T_<hash>, C_<hash>).
                  Desidentificação semântica máxima. Padrão para uso com LLMs.
    HASH_ABBREV – mantém os primeiros 3 chars do nome original + hash curto.
                  Ex: TB_HEADER → TBH_a1b2c3.  Auxilia debug sem expor domínio.
    POSITIONAL  – substitui por TBLNNN / COLNNN (posição ordinal).
                  Totalmente opaco. Útil para relatórios externos.
    APPLY       – aplica mapeamento JSON já existente (não recalcula hashes).
                  Garante consistência entre execuções.
    """
    HASH_FULL   = auto()   # default: col_name → hash (cross-table consistency)
    HASH_SCOPED = auto()   # table.col_name → hash (unicidade global)
    HASH_ABBREV = auto()   # 3 chars + hash curto (debug-friendly)
    POSITIONAL  = auto()   # TBL001 / COL001 (ordinal puro)
    APPLY       = auto()   # aplica mapeamento JSON existente


class HashAlgorithm(Enum):
    SHA256 = "sha256"
    MD5    = "md5"


class ReportStyle(Enum):
    TERMINAL = "terminal"
    MARKDOWN  = "markdown"


# ─────────────────────────────────────────────────────────────────────────────
# Value Objects
# ─────────────────────────────────────────────────────────────────────────────

@dataclass(frozen=True)
class MaskConfig:
    """Configuração imutável do processo de mascaramento."""
    mode: MaskMode           = MaskMode.HASH_FULL
    algorithm: HashAlgorithm = HashAlgorithm.SHA256
    hash_length: int         = 8
    existing_mapping: Optional[Path] = None   # obrigatório em APPLY mode
    sqlite_output: Optional[Path]    = None   # persistir mapeamento em SQLite


@dataclass(frozen=True)
class AnalyzerConfig:
    """Configuração imutável do analisador DDL."""
    style: ReportStyle = ReportStyle.MARKDOWN
    emit_json: bool    = True


@dataclass(frozen=True)
class PipelineConfig:
    """Configuração do pipeline completo."""
    input_ddl: Path
    output_dir: Path
    mask: MaskConfig     = field(default_factory=MaskConfig)
    analyzer: AnalyzerConfig = field(default_factory=AnalyzerConfig)
    encoding: str        = "utf-8"
    run_unmasked_analysis: bool = True  # 4º passo: analisar com nomes reais


# ─────────────────────────────────────────────────────────────────────────────
# Abstrações de serviço
# ─────────────────────────────────────────────────────────────────────────────

class IMasker(ABC):
    """Contrato do mascarador de DDL."""

    @abstractmethod
    def mask(self, ddl: str, config: MaskConfig) -> tuple[str, dict]:
        """
        Retorna (masked_ddl, mapping_dict).
        mapping_dict segue o schema:
          {
            "hash_algorithm": str,
            "hash_length": int,
            "tables":      {original: mock, ...},
            "columns":     {"table.column": mock, ...},
            "indexes":     {original: mock, ...},
            "constraints": {original: mock, ...},
          }
        """

    @abstractmethod
    def apply_mapping(self, ddl: str, mapping: dict) -> str:
        """Aplica mapeamento pré-existente a um DDL."""


class IUnmasker(ABC):
    """Contrato do desmascarador de relatórios."""

    @abstractmethod
    def unmask(self, text: str, mapping: dict) -> str:
        """Substitui tokens mascarados pelos originais no texto."""


class IReportEmitter(ABC):
    """Contrato de emissão de relatório de análise."""

    @abstractmethod
    def emit(self, ddl: str, config: AnalyzerConfig) -> tuple[str, dict]:
        """
        Retorna (report_text, json_structure).
        """


class IPipelineStep(ABC):
    """Passo atômico executável no pipeline."""

    @abstractmethod
    def execute(self, ctx: "PipelineContext") -> "PipelineContext":
        """Executa o passo e retorna contexto atualizado."""

    @property
    @abstractmethod
    def step_name(self) -> str:
        """Nome descritivo do passo."""


# ─────────────────────────────────────────────────────────────────────────────
# Contexto compartilhado entre steps
# ─────────────────────────────────────────────────────────────────────────────

@dataclass
class PipelineContext:
    """
    Objeto de estado mutável passado entre os steps do pipeline.
    Cada step lê o que precisa e escreve os seus artefatos.
    """
    config: PipelineConfig

    # Artefatos produzidos ao longo do pipeline
    original_ddl: str          = ""
    masked_ddl: str            = ""
    mapping: dict              = field(default_factory=dict)

    masked_report: str         = ""
    masked_json: dict          = field(default_factory=dict)

    unmasked_report: str       = ""

    real_report: str           = ""
    real_json: dict            = field(default_factory=dict)

    # Rastreamento de arquivos escritos: step_index → Path
    artifacts: dict[int, list[Path]] = field(default_factory=dict)

    # Log de execução
    log: list[str]             = field(default_factory=list)

    def record(self, step_index: int, path: Path) -> None:
        self.artifacts.setdefault(step_index, []).append(path)

    def info(self, msg: str) -> None:
        self.log.append(msg)
        print(f"  ℹ  {msg}")
