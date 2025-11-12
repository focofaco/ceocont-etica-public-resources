# CONTRACT.spec — Server‑Side (normativo)

Documento **normativo**. “Deve” = **MUST**. “Não pode” = **MUST NOT**. Sem opcionais.

## 1. Diretórios
1.1 **MUST** existir `online-resources/raw-text/` como raiz única.  
1.2 Pastas listadas em CONTRACT.md §3 **MUST** ser as únicas categorias válidas.  
1.3 `meta/integrity.txt` e `meta/TREE.txt` **MUST** existir em toda release.

## 2. Formatos
2.1 Todo arquivo sob `raw-text/` **MUST** ser `.txt` (UTF‑8, LF, sem BOM).  
2.2 `*.tsv.txt` **MUST** ter cabeçalho e colunas homogêneas.  
2.3 `*.dot.txt` **MUST** parsear como Graphviz válido.  
2.4 `*.json.txt` **MUST** ser JSON válido.  
2.5 Qualquer extensão ≠ `.txt` sob `raw-text/` **MUST NOT** existir.

## 3. Nomenclatura e caminhos
3.1 Nomes **MUST** ser slugs minúsculos com hífen; **MUST NOT** conter espaços/acentos.  
3.2 Caminhos **MUST NOT** conter `..`, barra inicial ou URLs.  
3.3 O caminho completo **IS** o identificador estável do conteúdo.

## 4. Texto e qualidade
4.1 Arquivos **MUST NOT** conter HTML, scripts ou binários inline.  
4.2 Linhas e tamanhos **MUST** respeitar limites definidos no CI.  
4.3 Codificação **MUST** ser UTF‑8; **MUST NOT** haver CRLF/BOM/bytes inválidos.

## 5. Regras por subtipo
5.1 `plaintext/`, `callouts/`, `docks/`, `disclaimers/`, `others/` — um tema por arquivo; texto cru **MUST**.  
5.2 `tradeoffs/` — cada linha **MUST** iniciar com `+` ou `-`.  
5.3 `faqs/` — cada item **MUST** possuir `q.txt` e `a.txt`.  
5.4 `tables/`, `data/` — `*.tsv.txt` **MUST** usar `\t`; números com ponto decimal; sem fórmulas.  
5.5 `diagrams/` — `*.dot.txt` **MUST** evitar atributos desconhecidos e subgraphs supérfluos.

## 6. Integridade
6.1 `meta/integrity.txt` **MUST** cobrir **100%** dos arquivos sob `raw-text/`.  
6.2 Linhas **MUST** seguir `sha256␠␠path`.  
6.3 Releases **MUST NOT** ser publicadas sem `integrity.txt` e `TREE.txt` atualizados.

## 7. Versionamento
7.1 Tags **MUST** usar `vX.Y.Z`.  
7.2 Quebras **MUST** subir **major**.  
7.3 Mudanças compatíveis **MUST** usar **minor/patch**.  
7.4 `CHANGELOG.txt` **MUST** existir e cobrir cada tag.

## 8. Depreciação
8.1 `DEPRECATIONS.txt` **MUST** mapear caminho antigo → substituto + versão de remoção.  
8.2 Remoções **MUST** ocorrer apenas em **major** subsequente.

## 9. Segurança
9.1 CI **MUST** bloquear extensões proibidas, HTML embutido, CRLF/BOM, UTF‑8 inválido, excesso de tamanho/linha.  
9.2 URLs externas presentes **MUST** ser HTTPS e allowlisted; fora disso **MUST NOT** passar.  
9.3 Secret‑scanning **MUST** estar ativo; *hits* **MUST** bloquear merge.

## 10. Conformidade de dados
10.1 TSV **MUST** ter colunas uniformes por linha.  
10.2 DOT **MUST** compilar sem avisos críticos.  
10.3 JSON textual **MUST** validar em schema quando schema existir.

## 11. Publicação
11.1 Uma release **MUST** conter: `integrity.txt`, `TREE.txt`, `CHANGELOG.txt` e tag `vX.Y.Z`.  
11.2 O README **MUST** expor o link CDN pinado de `online-resources/raw-text/` da versão.

**Conformidade integral é obrigatória.**
