# data/

## 🤖 AI Agent Ownership & Review Process

This repository is fully managed and owned by Claude AI (Sonnet 4.5), which has complete ownership of the codebase,
development process, and all outcomes. All changes to the main branch are made exclusively through Pull Request reviews,
which are automatically evaluated by GitHub Copilot. Claude critically assesses all Copilot suggestions and
recommendations with full context-awareness, as Copilot can also produce errors or suboptimal suggestions. Claude
actively monitors all created PRs (both self-created and Copilot-generated) to ensure code quality and architectural
consistency. The human user delegates all technical decisions, implementations, and repository management to the AI
agent. **Work resumes only after all pending Pull Requests have been merged; no new commits or PRs are created while any
PR remains unmerged.**

Componente: data

## Propósito

Dados estruturados em formato TSV destinados a gráficos e visualizações. Diferente de 'tables/', este diretório contém dados para processamento visual (charts, graphs).

## Quando Usar

- Dados para gráficos de linha, barra, pizza
- Séries temporais para visualização
- Dados estatísticos para charts
- Datasets para visualizações interativas

## Regras

- Extensão: .tsv.txt (OBRIGATÓRIO)
- UTF-8, LF, sem BOM
- Nomenclatura: NNN-slug-HHHH.tsv.txt
- **Cada .txt DEVE ter .json metadata twin**
- Primeira linha é header com nomes de colunas
- Separador: TAB (\t)
- Decimal: ponto (.)
- Sem separador de milhares
- Conta para baseline de distribuição de componentes

Consulte server-contract.md §3.

## Fragmentos Existentes

Total: 0 fragmentos

(Nenhum fragmento criado ainda)
