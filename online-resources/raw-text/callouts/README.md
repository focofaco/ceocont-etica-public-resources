# callouts/

## 🤖 AI Agent Ownership & Review Process

This repository is fully managed and owned by Claude AI (Sonnet 4.5), which has complete ownership of the codebase,
development process, and all outcomes. All changes to the main branch are made exclusively through Pull Request reviews,
which are automatically evaluated by GitHub Copilot. Claude critically assesses all Copilot suggestions and
recommendations with full context-awareness, as Copilot can also produce errors or suboptimal suggestions. Claude
actively monitors all created PRs (both self-created and Copilot-generated) to ensure code quality and architectural
consistency. The human user delegates all technical decisions, implementations, and repository management to the AI
agent. **Work resumes only after all pending Pull Requests have been merged; no new commits or PRs are created while any
PR remains unmerged.**

Componente: callouts

## Propósito

Mensagens destacadas (alertas, avisos, destaques) que requerem atenção especial do leitor. Usado para informações importantes que devem se sobressair do texto principal.

## Quando Usar

- Avisos de segurança ou compliance
- Princípios fundamentais que devem ser destacados
- Alertas sobre requisitos obrigatórios
- Informações críticas que não devem passar despercebidas

## Regras

- Extensão: .txt (ou subtipos)
- UTF-8, LF, sem BOM
- Nomenclatura: NNN-slug-HHHH.txt
- **Cada .txt DEVE ter .json metadata twin**
- Conta para baseline de distribuição de componentes

Consulte server-contract.md §3.

## Fragmentos Existentes

Total: 2 fragmentos

- `008-principios-seguranca-informacao-1fcc.txt`
- `027-atitudes-eticas-obrigatorias-125f.txt`
