# ceocont-etica-public-resources

Repository de conteúdo textual puro para recursos públicos de ética profissional e contabilidade.

## 🤖 AI Agent Ownership & Review Process

This repository is fully managed and owned by Claude AI (Sonnet 4.5), which has complete ownership of the codebase,
development process, and all outcomes. All changes to the main branch are made exclusively through Pull Request reviews,
which are automatically evaluated by GitHub Copilot. Claude critically assesses all Copilot suggestions and
recommendations with full context-awareness, as Copilot can also produce errors or suboptimal suggestions. Claude
actively monitors all created PRs (both self-created and Copilot-generated) to ensure code quality and architectural
consistency. The human user delegates all technical decisions, implementations, and repository management to the AI
agent. **Work resumes only after all pending Pull Requests have been merged; no new commits or PRs are created while any
PR remains unmerged.**

## 📋 Visão Geral

Este repositório contém **texto puro** (.txt) versionado de forma imutável, com integridade rastreável e estrutura
estável, para consumo via CDN. É um **servidor de conteúdo** independente de cliente, sem lógica de renderização ou UI.

## 🏗️ Estrutura

```
online-resources/raw-text/
├── plaintext/          # Texto corrido por box (70-80% do conteúdo)
├── callouts/           # Mensagens destacadas
├── docks/              # Notas laterais editoriais
├── tradeoffs/          # Listas prós/contras (+/-)
├── tables/             # Tabelas TSV (*.tsv.txt)
├── data/               # Dados TSV para gráficos
├── faqs/               # Pares q.txt + a.txt
├── diagrams/           # Diagramas DOT (*.dot.txt)
├── disclaimers/        # Avisos legais/risco
├── others/             # Conteúdo textual genérico
├── header_h1/          # Cabeçalhos nível 1 (estruturais)
├── header_h2/          # Cabeçalhos nível 2 (estruturais)
├── header_h3/          # Cabeçalhos nível 3 (estruturais)
└── meta/               # Metadados e integridade
    ├── glossario.json.txt
    ├── abbr.json.txt
    ├── integrity.txt   # SHA256 checksums
    └── TREE.txt        # Estrutura de diretórios
```

## 📦 Versão Atual

**v2.0.0** - 2025-11-13

Breaking changes: Adição de categorias header_h1/, header_h2/, header_h3/

Ver [CHANGELOG.md](CHANGELOG.md) para histórico completo.

## 📝 Contratos e Especificações

### Contrato do Servidor

- **[server-contract.md](server-contract.md)** - Contrato principal
- **[server-contract.spec](server-contract.spec)** - Especificação normativa
- **[contract.schema](contract.schema)** - Schema (latim)

### Guia de Marca

- **[server-brandguide.md](server-brandguide.md)** - Guia de marca textual
- **[server-brandguide.spec](server-brandguide.spec)** - Especificação normativa
- **[server-brandguide-schema.json](server-brandguide-schema.json)** - Schema JSON

## 🔒 Regras de Formato

### Permitido

- ✅ Extensão `.txt` (UTF-8, LF, sem BOM)
- ✅ Subtipos: `.tsv.txt`, `.dot.txt`, `.json.txt`
- ✅ Nomenclatura: lowercase-slug-with-hyphens

### Proibido

- ❌ HTML, JavaScript, CSS
- ❌ Imagens (SVG, PNG, JPG, WebP)
- ❌ PDFs, binários, áudio/vídeo
- ❌ CRLF, BOM, caracteres de controle

## 🛡️ Validação

### Pre-commit Hooks

```bash
# Instalar pre-commit
pip install -r requirements.txt
pre-commit install

# Executar manualmente
pre-commit run --all-files
```

### Hooks Ativos

- ✓ validate_raw_text_only.sh - Apenas .txt permitido
- ✓ forbid_html_js_css.sh - Sem HTML/JS/CSS
- ✓ check_crlf.sh - LF obrigatório
- ✓ validate_filename_pattern.sh - Nomenclatura correta
- ✓ validate_metadata_twins.sh - Pares .txt/.json válidos
- ✓ validate_chunks_pydantic.py - Schema chunks.json
- ✓ validate_metadata_twin_pydantic.py - Schema metadata twins

## 📊 Estatísticas do Repositório

**Estado atual:**

- **Total de fragmentos:** 51 (36 conteúdo + 15 headers)
- **Total de chunks:** 6
- **Componentes em uso:** 8 (plaintext, callouts, docks, tradeoffs, tables, faqs, disclaimers, headers h1/h2)
- **Placeholders rastreados:** 18

**Distribuição de fragmentos:**

- 47.1% plaintext (24 fragmentos)
- 23.5% faqs (12 fragmentos)
- 14.7% docks (7 fragmentos)
- 5.9% callouts (3 fragmentos)
- 5.9% header_h2 (3 fragmentos)
- 3.9% disclaimers (2 fragmentos)

**Baseline obrigatória:**

- 70-80% plaintext (meta: conteúdo textual principal)
- 20-30% outros componentes

**Headers são estruturais** e NÃO contam na baseline de conteúdo.

Ver [chunks.json](chunks.json) para status completo e atualizado.

## 🔐 Integridade

Todos os arquivos sob `online-resources/raw-text/` possuem checksums SHA256 em:

```
online-resources/raw-text/meta/integrity.txt
```

Verificar integridade:

```bash
cd online-resources/raw-text
sha256sum -c meta/integrity.txt
```

## 📌 Versionamento Semântico

- **MAJOR** (X.0.0): Breaking changes (renomear/mover paths, nova categoria)
- **MINOR** (0.X.0): Adições compatíveis (novo conteúdo)
- **PATCH** (0.0.X): Correções (typos, bugs)

Ver [DEPRECATIONS.txt](DEPRECATIONS.txt) para paths depreciados.

## 🚀 Releases

### Tags Disponíveis

- **v2.0.0** - Header components (BREAKING)
- **v1.1.0** - Pre-commit hooks e validação
- **v1.0.0** - Estrutura inicial

### Documentação de Releases

- [RELEASE-v2.0.0.md](RELEASE-v2.0.0.md)
- [RELEASE-v1.1.0.md](RELEASE-v1.1.0.md)
- [RELEASE-v1.0.0.md](RELEASE-v1.0.0.md)

## 🔧 Desenvolvimento

### Estrutura de Branches

```
main                    # Produção (protegida)
claude/*-SESSION_ID     # Feature branches
```

### Workflow

1. Criar branch `claude/dev-description-SESSION_ID`
1. Fazer alterações seguindo [CLAUDE.md](CLAUDE.md)
1. Se aplicável, extrair headers (h1, h2) de fragmentos plaintext para header_h1/ e header_h2/
1. Validar com pre-commit hooks
1. Commit com Conventional Commits
1. Push para branch
1. Criar Pull Request
1. Merge para main
1. Criar GitHub Release (gera tag automaticamente)

**Processo de extração de headers:**

Headers estruturais (h1, h2) são extraídos de fragmentos plaintext e armazenados em categorias dedicadas (header_h1/, header_h2/). Este processo mantém:
- Headers como componentes estruturais separados
- Atualização de metadata twins para referenciar headers extraídos
- Chunks.json atualizado com novos fragmentos
- Integridade de referências entre fragmentos e headers

## 📚 Documentação Adicional

- **[CLAUDE.md](CLAUDE.md)** - Regras operacionais para AI agents
- **[TAG-PUSH-WORKAROUND.md](TAG-PUSH-WORKAROUND.md)** - Workflow de tags
- **[GITHUB-RELEASES-STATUS.md](GITHUB-RELEASES-STATUS.md)** - Status de releases

## 🧩 Metadata Twins

Arquivos .txt podem ter .json metadata twins (Single Source of Truth):

```
plaintext/001-politica-controle-qualidade-contabil-41f5.txt
plaintext/001-politica-controle-qualidade-contabil-41f5.json
```

JSON contém conteúdo completo + metadados. TXT é derivado (CDN only).

## 📞 Suporte

Para issues, bugs ou sugestões:

- GitHub Issues:
  [ceocont-etica-public-resources/issues](https://github.com/focofaco/ceocont-etica-public-resources/issues)

## 📄 Licença

Este repositório contém conteúdo textual para recursos públicos de ética profissional.

______________________________________________________________________

**Última atualização**: 2025-11-13 | **Versão**: v2.0.0
