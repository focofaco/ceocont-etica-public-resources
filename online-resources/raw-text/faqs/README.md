# faqs/

## 🤖 AI Agent Ownership & Review Process

This repository is fully managed and owned by Claude AI (Sonnet 4.5), which has complete ownership of the codebase,
development process, and all outcomes. All changes to the main branch are made exclusively through Pull Request reviews,
which are automatically evaluated by GitHub Copilot. Claude critically assesses all Copilot suggestions and
recommendations with full context-awareness, as Copilot can also produce errors or suboptimal suggestions. Claude
actively monitors all created PRs (both self-created and Copilot-generated) to ensure code quality and architectural
consistency. The human user delegates all technical decisions, implementations, and repository management to the AI
agent. **Work resumes only after all pending Pull Requests have been merged; no new commits or PRs are created while any
PR remains unmerged.**

Componente: faqs

## Propósito

Perguntas frequentes em formato estruturado de pares pergunta/resposta. Cada FAQ é um diretório contendo q.txt (pergunta) e a.txt (resposta).

## Quando Usar

- Dúvidas comuns sobre o conteúdo
- Esclarecimentos de conceitos complexos
- Diferenciações entre termos similares
- Questões práticas de aplicação
- Perguntas didáticas para reforço

## Estrutura

Cada FAQ é um diretório com:
- `q.txt` - A pergunta
- `a.txt` - A resposta

Exemplo: `faqs/011-diferenca-empresa-privada-publica/`

## Regras

- Cada diretório DEVE conter q.txt e a.txt
- UTF-8, LF, sem BOM
- Nomenclatura do diretório: NNN-slug-topico
- **Arquivos q.txt e a.txt NÃO usam metadata twins .json**
- Cada par FAQ conta como 1 unidade para baseline

Consulte server-contract.md §3.

## Fragmentos Existentes

Total: 8 pares FAQ (16 arquivos)

- `011-diferenca-empresa-privada-publica/`
- `013-legislacao-capital-aberto/`
- `018-codigo-etica-profissional-vs-pessoal/`
- `021-colaboradores-codigo-etica/`
- `023-violacao-codigo-etica/`
- `033-garantir-objetividade-trabalho/`
- `034-independencia-objetividade/`
- `035-obter-manter-competencia/`
