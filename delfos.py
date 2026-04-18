# analisador-delfos/delfos.py
#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║             DELFOS v2 · CLI Principal                                        ║
║   Ponto de entrada único com subcomandos:                                    ║
║     delfos mask       — mascara DDL                                          ║
║     delfos analyze    — analisa DDL (mascarado ou original)                  ║
║     delfos unmask     — desmascara relatório                                 ║
║     delfos pipeline   — executa fluxo completo                               ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""
from __future__ import annotations

import argparse
import json
import sys
import textwrap
from pathlib import Path

# Adiciona o diretório raiz ao sys.path para imports relativos funcionarem
sys.path.insert(0, str(Path(__file__).resolve().parent))

from core import (
    AnalyzerConfig, DelfosAnalysisPipeline, DDLMasker, DDLReportEmitter,
    HashAlgorithm, MaskConfig, MaskMode, PipelineConfig, ReportStyle,
    ReportUnmasker, load_mapping, save_mapping,
)


# ─────────────────────────────────────────────────────────────────────────────
# Sub-handler: mask
# ─────────────────────────────────────────────────────────────────────────────

def cmd_mask(args: argparse.Namespace) -> None:
    ddl_path = Path(args.ddl_file)
    if not ddl_path.exists():
        _die(f"Arquivo não encontrado: {ddl_path}")

    ddl = ddl_path.read_text(encoding=args.encoding, errors='replace')

    mode = {
        'hash':      MaskMode.HASH_FULL,
        'scoped':    MaskMode.HASH_SCOPED,
        'abbrev':    MaskMode.HASH_ABBREV,
        'positional': MaskMode.POSITIONAL,
        'apply':     MaskMode.APPLY,
    }[args.mode]

    existing = Path(args.apply_mapping) if args.apply_mapping else None
    sqlite   = Path(args.sqlite)        if args.sqlite        else None

    cfg = MaskConfig(
        mode=mode,
        algorithm=HashAlgorithm(args.hash),
        hash_length=args.length,
        existing_mapping=existing,
        sqlite_output=sqlite,
    )

    masker = DDLMasker()
    masked_ddl, mapping = masker.mask(ddl, cfg)

    out_ddl  = Path(args.output)
    out_map  = Path(args.mapping)
    out_ddl.write_text(masked_ddl, encoding='utf-8')
    save_mapping(mapping, out_map)
    print(f"✅  DDL mascarado  → {out_ddl}")
    print(f"✅  Mapeamento     → {out_map}")
    if sqlite:
        print(f"✅  SQLite         → {sqlite}")


# ─────────────────────────────────────────────────────────────────────────────
# Sub-handler: analyze
# ─────────────────────────────────────────────────────────────────────────────

def cmd_analyze(args: argparse.Namespace) -> None:
    ddl_path = Path(args.ddl_file)
    if not ddl_path.exists():
        _die(f"Arquivo não encontrado: {ddl_path}")

    ddl = ddl_path.read_text(encoding=args.encoding, errors='replace')

    cfg = AnalyzerConfig(
        style=ReportStyle(args.style),
        emit_json=bool(args.json_output),
    )
    emitter = DDLReportEmitter()
    report, json_data = emitter.emit(ddl, cfg)

    if args.output:
        Path(args.output).write_text(report, encoding='utf-8')
        print(f"✅  Relatório → {args.output}")
    else:
        print(report)

    if args.json_output:
        Path(args.json_output).write_text(
            json.dumps(json_data, ensure_ascii=False, indent=2), encoding='utf-8')
        print(f"✅  JSON      → {args.json_output}")


# ─────────────────────────────────────────────────────────────────────────────
# Sub-handler: unmask
# ─────────────────────────────────────────────────────────────────────────────

def cmd_unmask(args: argparse.Namespace) -> None:
    report_path  = Path(args.report)
    mapping_path = Path(args.mapping)

    for p in (report_path, mapping_path):
        if not p.exists():
            _die(f"Arquivo não encontrado: {p}")

    text    = report_path.read_text(encoding=args.encoding)
    mapping = load_mapping(mapping_path)

    unmasker  = ReportUnmasker()
    unmasked  = unmasker.unmask(text, mapping)

    out = Path(args.output)
    out.write_text(unmasked, encoding='utf-8')
    print(f"✅  Relatório desmascado → {out}")


# ─────────────────────────────────────────────────────────────────────────────
# Sub-handler: pipeline
# ─────────────────────────────────────────────────────────────────────────────

def cmd_pipeline(args: argparse.Namespace) -> None:
    ddl_path = Path(args.ddl_file)
    if not ddl_path.exists():
        _die(f"Arquivo não encontrado: {ddl_path}")

    output_dir = Path(args.output_dir)

    mode = {
        'hash':       MaskMode.HASH_FULL,
        'scoped':     MaskMode.HASH_SCOPED,
        'abbrev':     MaskMode.HASH_ABBREV,
        'positional': MaskMode.POSITIONAL,
        'apply':      MaskMode.APPLY,
    }[args.mode]

    existing = Path(args.apply_mapping) if args.apply_mapping else None

    mask_cfg = MaskConfig(
        mode=mode,
        algorithm=HashAlgorithm(args.hash),
        hash_length=args.length,
        existing_mapping=existing,
    )
    analyzer_cfg = AnalyzerConfig(
        style=ReportStyle(args.style),
        emit_json=not args.no_json,
    )
    pipeline_cfg = PipelineConfig(
        input_ddl=ddl_path,
        output_dir=output_dir,
        mask=mask_cfg,
        analyzer=analyzer_cfg,
        encoding=args.encoding,
        run_unmasked_analysis=not args.skip_original,
    )

    pipeline = DelfosAnalysisPipeline(pipeline_cfg)
    pipeline.run()


# ─────────────────────────────────────────────────────────────────────────────
# Parser de argumentos
# ─────────────────────────────────────────────────────────────────────────────

def build_parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(
        prog='delfos',
        description='DELFOS v2 — Análise e Anonimização de DDLs',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""\
            Exemplos rápidos:
              # Pipeline completo (recomendado)
              python delfos.py pipeline banco.sql --output-dir ./output

              # Apenas mascarar (modo hash, padrão)
              python delfos.py mask banco.sql --output banco_mock.sql --mapping mapping.json

              # Mascarar com abreviação + SQLite
              python delfos.py mask banco.sql --mode abbrev --sqlite mapping.db \\
                               --output banco_mock.sql --mapping mapping.json

              # Mascarar aplicando mapeamento existente
              python delfos.py mask banco.sql --mode apply --apply-mapping mapping.json \\
                               --output banco_mock2.sql --mapping mapping.json

              # Só analisar (markdown)
              python delfos.py analyze banco_mock.sql --style markdown --output relatorio.md

              # Só desmascarar relatório
              python delfos.py unmask relatorio_mock.md mapping.json --output relatorio_real.md
        """),
    )
    sub = root.add_subparsers(dest='command', required=True)

    # ── mask ──────────────────────────────────────────────────────────────────
    p_mask = sub.add_parser('mask', help='Mascara DDL e gera mapeamento')
    p_mask.add_argument('ddl_file')
    p_mask.add_argument('--output',   '-o', required=True,
                        help='DDL mascarado de saída')
    p_mask.add_argument('--mapping',  '-m', default='mapping.json',
                        help='Arquivo JSON do mapeamento (padrão: mapping.json)')
    p_mask.add_argument('--mode', choices=['hash','scoped','abbrev','positional','apply'],
                        default='hash',
                        help='hash=T_<hash8> cross-table (default) | '
                             'scoped=hash único por tabela.coluna | '
                             'abbrev=TBH_<hash6> | positional=TBL001 | '
                             'apply=usar mapping existente')
    p_mask.add_argument('--hash', choices=['sha256','md5'], default='sha256')
    p_mask.add_argument('--length', '-l', type=int, default=8,
                        help='Comprimento do hash hex (0=completo)')
    p_mask.add_argument('--apply-mapping', default=None,
                        help='Mapeamento JSON existente (obrigatório em --mode apply)')
    p_mask.add_argument('--sqlite', default=None,
                        help='Persistir mapeamento também em SQLite')
    p_mask.add_argument('--encoding', '-e', default='utf-8')
    p_mask.set_defaults(func=cmd_mask)

    # ── analyze ───────────────────────────────────────────────────────────────
    p_analyze = sub.add_parser('analyze', help='Analisa DDL e gera relatório')
    p_analyze.add_argument('ddl_file')
    p_analyze.add_argument('--output',      '-o', default=None)
    p_analyze.add_argument('--json',        '-j', dest='json_output', default=None)
    p_analyze.add_argument('--style',       '-s',
                           choices=['terminal','markdown'], default='markdown')
    p_analyze.add_argument('--encoding',    '-e', default='utf-8')
    p_analyze.set_defaults(func=cmd_analyze)

    # ── unmask ────────────────────────────────────────────────────────────────
    p_unmask = sub.add_parser('unmask', help='Desmascara relatório')
    p_unmask.add_argument('report',  help='Relatório mascarado')
    p_unmask.add_argument('mapping', help='Arquivo de mapeamento JSON')
    p_unmask.add_argument('--output', '-o', required=True)
    p_unmask.add_argument('--encoding', '-e', default='utf-8')
    p_unmask.set_defaults(func=cmd_unmask)

    # ── pipeline ──────────────────────────────────────────────────────────────
    p_pipe = sub.add_parser('pipeline',
                            help='Executa mask → analyze → unmask → analyze(original)')
    p_pipe.add_argument('ddl_file')
    p_pipe.add_argument('--output-dir', '-d', default='./delfos_output',
                        help='Diretório de saída (padrão: ./delfos_output)')
    p_pipe.add_argument('--mode', choices=['hash','scoped','abbrev','positional','apply'],
                        default='hash')
    p_pipe.add_argument('--hash', choices=['sha256','md5'], default='sha256')
    p_pipe.add_argument('--length', '-l', type=int, default=8)
    p_pipe.add_argument('--apply-mapping', default=None)
    p_pipe.add_argument('--style', '-s',
                        choices=['terminal','markdown'], default='markdown')
    p_pipe.add_argument('--no-json',       action='store_true',
                        help='Não emitir arquivos JSON')
    p_pipe.add_argument('--skip-original', action='store_true',
                        help='Não executar análise do DDL original (passo 5)')
    p_pipe.add_argument('--encoding', '-e', default='utf-8')
    p_pipe.set_defaults(func=cmd_pipeline)

    return root


# ─────────────────────────────────────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────────────────────────────────────

def _die(msg: str) -> None:
    print(f"❌  {msg}", file=sys.stderr)
    sys.exit(1)


# ─────────────────────────────────────────────────────────────────────────────
# Entry point
# ─────────────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = build_parser()
    args   = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
