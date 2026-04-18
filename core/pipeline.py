# analisador-delfos/core/pipeline.py
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║             DELFOS v2 · Pipeline Orquestrador                                ║
║   Executa mask → analyze(masked) → unmask → analyze(real) em sequência      ║
╚══════════════════════════════════════════════════════════════════════════════╝
Responsabilidade: orquestrar steps e persistir artefatos numerados.

Artefatos gerados (numerados pela ordem de execução):
  01_masked.sql          — DDL com identificadores substituídos por tokens
  02_mapping.json        — Mapeamento reversível  original ↔ mock
  03_report_masked.md    — Relatório de estrutura sobre o DDL mascarado
  03_structure_masked.json
  04_report_real.md      — Relatório com nomes reais (desmascado)
  05_report_original.md  — Relatório gerado direto do DDL original (passo bonus)
  05_structure_original.json

Se run_unmasked_analysis=False o passo 5 é omitido.
"""
from __future__ import annotations

import json
from pathlib import Path

from .abstractions import (
    AnalyzerConfig, IPipelineStep, MaskConfig, MaskMode,
    PipelineConfig, PipelineContext, ReportStyle,
)
from .analyzer import DDLReportEmitter
from .masker import DDLMasker, ReportUnmasker, save_mapping


# ─────────────────────────────────────────────────────────────────────────────
# Steps individuais — SRP: cada um tem UMA responsabilidade
# ─────────────────────────────────────────────────────────────────────────────

class Step01_MaskDDL(IPipelineStep):
    """Mascara o DDL original e persiste o mapeamento."""

    @property
    def step_name(self) -> str:
        return "01 · Mascarar DDL"

    def execute(self, ctx: PipelineContext) -> PipelineContext:
        masker = DDLMasker()
        masked_ddl, mapping = masker.mask(ctx.original_ddl, ctx.config.mask)
        ctx.masked_ddl = masked_ddl
        ctx.mapping    = mapping

        out = ctx.config.output_dir
        masked_path  = out / "01_masked.sql"
        mapping_path = out / "02_mapping.json"

        masked_path.write_text(masked_ddl, encoding=ctx.config.encoding)
        save_mapping(mapping, mapping_path)

        ctx.record(1, masked_path)
        ctx.record(2, mapping_path)
        ctx.info(f"DDL mascarado → {masked_path.name}")
        ctx.info(f"Mapeamento    → {mapping_path.name}")
        return ctx


class Step02_AnalyzeMasked(IPipelineStep):
    """Analisa o DDL mascarado e gera relatório sem nomes reais."""

    @property
    def step_name(self) -> str:
        return "02 · Analisar DDL mascarado"

    def execute(self, ctx: PipelineContext) -> PipelineContext:
        emitter = DDLReportEmitter()
        report, json_data = emitter.emit(ctx.masked_ddl, ctx.config.analyzer)
        ctx.masked_report = report
        ctx.masked_json   = json_data

        out = ctx.config.output_dir
        report_path = out / "03_report_masked.md"
        json_path   = out / "03_structure_masked.json"

        report_path.write_text(report, encoding=ctx.config.encoding)
        if ctx.config.analyzer.emit_json:
            json_path.write_text(
                json.dumps(json_data, ensure_ascii=False, indent=2),
                encoding=ctx.config.encoding,
            )
            ctx.record(3, json_path)

        ctx.record(3, report_path)
        ctx.info(f"Relatório mascarado → {report_path.name}")
        return ctx


class Step03_UnmaskReport(IPipelineStep):
    """Aplica o mapeamento inverso ao relatório mascarado."""

    @property
    def step_name(self) -> str:
        return "03 · Desmascarar relatório"

    def execute(self, ctx: PipelineContext) -> PipelineContext:
        unmasker = ReportUnmasker()
        ctx.unmasked_report = unmasker.unmask(ctx.masked_report, ctx.mapping)

        report_path = ctx.config.output_dir / "04_report_real.md"
        report_path.write_text(ctx.unmasked_report, encoding=ctx.config.encoding)
        ctx.record(4, report_path)
        ctx.info(f"Relatório desmascado → {report_path.name}")
        return ctx


class Step04_AnalyzeOriginal(IPipelineStep):
    """(Opcional) Analisa o DDL original com nomes reais."""

    @property
    def step_name(self) -> str:
        return "04 · Analisar DDL original (nomes reais)"

    def execute(self, ctx: PipelineContext) -> PipelineContext:
        emitter = DDLReportEmitter()
        report, json_data = emitter.emit(ctx.original_ddl, ctx.config.analyzer)
        ctx.real_report = report
        ctx.real_json   = json_data

        out = ctx.config.output_dir
        report_path = out / "05_report_original.md"
        json_path   = out / "05_structure_original.json"

        report_path.write_text(report, encoding=ctx.config.encoding)
        if ctx.config.analyzer.emit_json:
            json_path.write_text(
                json.dumps(json_data, ensure_ascii=False, indent=2),
                encoding=ctx.config.encoding,
            )
            ctx.record(5, json_path)

        ctx.record(5, report_path)
        ctx.info(f"Relatório original  → {report_path.name}")
        return ctx


# ─────────────────────────────────────────────────────────────────────────────
# Pipeline — orquestrador (Open/Closed: adicione steps sem modificar)
# ─────────────────────────────────────────────────────────────────────────────

class DelfosAnalysisPipeline:
    """
    Orquestra os steps do pipeline DELFOS v2.

    Fluxo padrão:
      Step01_MaskDDL
      Step02_AnalyzeMasked
      Step03_UnmaskReport
      [Step04_AnalyzeOriginal]  ← condicional a config.run_unmasked_analysis

    Uso mínimo:
        cfg = PipelineConfig(
            input_ddl=Path("banco.sql"),
            output_dir=Path("output/"),
        )
        pipeline = DelfosAnalysisPipeline(cfg)
        ctx = pipeline.run()

    Adicionando um step customizado (Open/Closed):
        pipeline.register_step(MyCustomStep(), after=Step03_UnmaskReport)
        ctx = pipeline.run()
    """

    def __init__(self, config: PipelineConfig) -> None:
        self._config = config
        self._steps: list[IPipelineStep] = self._default_steps()

    def _default_steps(self) -> list[IPipelineStep]:
        steps: list[IPipelineStep] = [
            Step01_MaskDDL(),
            Step02_AnalyzeMasked(),
            Step03_UnmaskReport(),
        ]
        if self._config.run_unmasked_analysis:
            steps.append(Step04_AnalyzeOriginal())
        return steps

    def register_step(
        self,
        step: IPipelineStep,
        after: type[IPipelineStep] | None = None,
    ) -> None:
        """
        Insere um step customizado.
        Se after=None, acrescenta no final.
        Se after=SomeStepClass, insere imediatamente após a primeira ocorrência.
        """
        if after is None:
            self._steps.append(step)
            return
        for i, s in enumerate(self._steps):
            if isinstance(s, after):
                self._steps.insert(i + 1, step)
                return
        self._steps.append(step)

    def run(self) -> PipelineContext:
        self._config.output_dir.mkdir(parents=True, exist_ok=True)
        ctx = PipelineContext(config=self._config)
        ctx.original_ddl = self._config.input_ddl.read_text(
            encoding=self._config.encoding, errors='replace'
        )

        total = len(self._steps)
        _banner("DELFOS v2 · Pipeline de Análise DDL")
        _banner(f"Entrada : {self._config.input_ddl}")
        _banner(f"Saída   : {self._config.output_dir}")
        _banner(f"Steps   : {total}")
        print()

        for i, step in enumerate(self._steps, start=1):
            print(f"  [{i}/{total}] {step.step_name}")
            try:
                ctx = step.execute(ctx)
            except Exception as exc:  # noqa: BLE001
                ctx.info(f"❌ Erro no step '{step.step_name}': {exc}")
                raise

        print()
        _banner("Artefatos gerados")
        for step_idx in sorted(ctx.artifacts):
            for path in ctx.artifacts[step_idx]:
                size = path.stat().st_size
                print(f"  [{step_idx:02d}]  {path.name:<45}  {size:>8} bytes")

        print()
        _banner("Pipeline concluído ✅")
        return ctx


# ─────────────────────────────────────────────────────────────────────────────
# Helpers de apresentação
# ─────────────────────────────────────────────────────────────────────────────

def _banner(msg: str) -> None:
    print(f"  {'─'*70}")
    print(f"  {msg}")
