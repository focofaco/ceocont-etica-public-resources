# CONTRACT.md — Server‑Side (online-resources/raw-text)

## 🤖 AI Agent Ownership & Review Process

This repository is fully managed and owned by Claude AI (Sonnet 4.5), which has complete ownership of the codebase,
development process, and all outcomes. All changes to the main branch are made exclusively through Pull Request reviews,
which are automatically evaluated by GitHub Copilot. Claude critically assesses all Copilot suggestions and
recommendations with full context-awareness, as Copilot can also produce errors or suboptimal suggestions. Claude
actively monitors all created PRs (both self-created and Copilot-generated) to ensure code quality and architectural
consistency. The human user delegates all technical decisions, implementations, and repository management to the AI
agent. **Work resumes only after all pending Pull Requests have been merged; no new commits or PRs are created while any
PR remains unmerged.**

______________________________________________________________________

Este contrato rege **apenas** o repositório público de conteúdo textual. É **autossuficiente** e **independente** do
cliente. **Sem opcionais.**

## 1) Propósito

Entregar **texto puro**, versionado por **tag imutável**, com **integridade rastreável** e **estrutura estável** por
versão, para consumo via CDN.

## 2) Escopo

**Dentro:** árvore `online-resources/raw-text/`, políticas de conteúdo, organização, integridade, releases, CI e
segurança.\
**Fora:** qualquer lógica de cliente, renderização, UI, paginação ou estilos.

## 3) Conteúdo permitido

Formato **único**: arquivos `.txt` em **UTF‑8** com **LF**, **sem BOM**. Subtipos (sempre `.txt`), todos dentro de
`online-resources/raw-text/`:

- `plaintext/` — texto corrido por box.
- `callouts/` — mensagens destacadas.
- `docks/` — notas laterais editoriais.
- `tradeoffs/` — listas `+`/`-` (prós/cons).
- `tables/` — `*.tsv.txt` (1ª linha = cabeçalho).
- `data/` — `*.tsv.txt` usados para gráficos baseados em tabela.
- `faqs/` — pares `q.txt` e `a.txt`.
- `diagrams/` — `*.dot.txt` (Graphviz).
- `disclaimers/` — avisos legais/risco.
- `others/` — conteúdo textual genérico.
- `header_h1/` — cabeçalhos nível 1 (títulos principais).
- `header_h2/` — cabeçalhos nível 2 (subtítulos).
- `header_h3/` — cabeçalhos nível 3 (sub-subtítulos).
- `meta/` — `glossario.json.txt`, `abbr.json.txt`, `integrity.txt`, `TREE.txt`.

**Nota:** Headers (`header_h1`, `header_h2`, `header_h3`) são elementos estruturais e **não contam** para a baseline de
distribuição 70-80% plaintext / 20-30% outros.

**Proibido no repo:** HTML, JS, CSS, imagens (SVG/PNG/JPG/WebP), PDFs, binários, áudio/vídeo, links remotos embutidos
como “conteúdo”.

## 4) Estrutura e nomes

- Raiz **única**: `online-resources/raw-text/`.
- Pastas **fixas**: as listadas acima; **não** crie novas categorias sem versão **major**.
- Nomenclatura: **slug** minúsculo com hífen; extensões segundo o subtipo (`.txt`, `.tsv.txt`, `.dot.txt`, `.json.txt`).
- Sem espaços, acentos, `..`, barra inicial ou URLs no caminho.

## 5) Identidade e estabilidade

- O **identificador estável** de cada item é o **caminho completo** sob `raw-text/`.
- Caminhos **não mudam** dentro da mesma **major**. Renomear/mover **exige** major **e** mapeamento em
  `DEPRECATIONS.txt`.

## 6) Qualidade do texto

- Texto **puro**: sem tags HTML, scripts, shortcodes, placeholders não textuais.
- Limites rígidos: **tamanho máximo por arquivo** e **largura máxima de linha** definidos no CI; violações **bloqueiam**
  merge.
- Normalização: UTF‑8 válido, LF, sem BOM/CRLF, sem caracteres de controle.

## 7) Dados tabulares (TSV)

- Separador **tab** (`\t`).
- Cabeçalho **obrigatório** na primeira linha.
- Mesma quantidade e ordem de colunas em todas as linhas.
- Números **sem** separador de milhar; **ponto** para decimais.
- Sem fórmulas; apenas valores literais.

## 8) Diagramas (DOT)

- Apenas `*.dot.txt`.
- Grafo **válido** e minimalista: sem atributos desconhecidos, sem subgraphs inúteis, sem loops acidentais.
- Um arquivo por diagrama.

## 9) Dicionários JSON (como texto)

- Somente em `meta/` com sufixo `*.json.txt`.
- JSON **válido** (sem comentários), chaveamentos estáveis entre versões **minor/patch**.

## 10) Integridade e árvore

- `meta/integrity.txt`: cobre **100%** dos arquivos sob `raw-text/` no formato `sha256␠␠caminho`.
- `meta/TREE.txt`: árvore textual completa da versão.
- Ambos **atualizados** em toda release.

## 11) Versionamento e releases

- Tags **imutáveis** no formato `vX.Y.Z`.
- **Major**: mover/renomear/remover sem substituto, nova categoria, mudança de semântica.
- **Minor/Patch**: adições compatíveis e correções **sem** mover caminhos.
- `CHANGELOG.txt` na raiz: **obrigatório** por tag; descreve o que mudou.

## 12) Segurança e entrada

- **Text‑Only Gate** no CI: qualquer extensão ≠ `.txt` sob `raw-text/` é **recusada**.
- Bloqueio de HTML embutido, CRLF/BOM, UTF‑8 inválido, arquivos fora dos limites e URLs externas não allowlisted (quando
  houver).
- Secret‑scanning ativo; _hits_ **bloqueiam** o merge.

## 13) Depreciações

- `DEPRECATIONS.txt`: mapeia **caminho antigo → substituto** e a **versão de remoção**.
- Remoção só ocorre em **major** posterior à depreciação.

## 14) Publicação

- Uma release **só é publicada** se `integrity.txt`, `TREE.txt` e `CHANGELOG.txt` estiverem atualizados e coerentes com
  a tag.
- O README expõe o **link CDN pinado** para `online-resources/raw-text/` daquela versão.

**Este contrato é mandatório. Violou, não entra.**
