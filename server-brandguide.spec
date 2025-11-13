# server-brandguide.spec — Especificação Normativa (server-side, raw-text)

Normas obrigatórias. “Deve” = MUST. “É vedado” = MUST NOT. Sem opcionais. Este documento não trata de cliente, UI ou estética.

1. Texto e codificação
1.1 Arquivos MUST ser .txt em UTF-8 com LF, sem BOM.
1.2 HTML, tags, scripts e shortcodes MUST NOT existir.
1.3 Emojis e símbolos decorativos MUST NOT ser usados.

2. Voz e tom
2.1 Voz impessoal, assertiva e direta MUST.
2.2 Tom normativo, técnico, autoritário, profissional e sério MUST.
2.3 Modais permitidos MUST: deve, é obrigatório, é vedado, proíbe-se, pode desde que, recomenda-se.
2.4 Modais proibidos MUST NOT: deveria, busca-se, pretende-se, espera-se, almeja-se, gostaríamos, desejamos, tentamos, procuramos.

3. Linguagem e estilo
3.1 Frases curtas, verbo forte e preferência por voz ativa MUST.
3.2 Siglas definidas na primeira ocorrência MUST.
3.3 Metáforas, humor, hipérboles e adjetivação gratuita MUST NOT.
3.4 Números em algarismos e unidades no SI quando aplicável MUST.

4. Categorias e regras
4.1 plaintext: parágrafos separados por linha em branco MUST.
4.2 callouts: uma mensagem por arquivo, curta e direta MUST.
4.3 docks: no máximo 600 caracteres MUST.
4.4 tradeoffs: cada linha MUST iniciar com “+” ou “−”; narrativa longa MUST NOT.
4.5 faqs: cada item MUST possuir q.txt e a.txt; pergunta clara e resposta objetiva MUST.
4.6 tables e data: *.tsv.txt MUST ter cabeçalho; separador tab; colunas estáveis; sem fórmulas; ponto decimal MUST.
4.7 diagrams: *.dot.txt MUST ser Graphviz válido; um grafo por arquivo; atributos desconhecidos e subgraphs supérfluos MUST NOT.
4.8 disclaimers: linguagem direta; sem links fora da allowlist MUST.
4.9 others: uso parcimonioso; quando existir categoria específica, usar a específica MUST.

5. Nomes e caminhos
5.1 Nomes MUST ser slugs minúsculos com hífen.
5.2 Caminhos MUST ser relativos sob online-resources/raw-text; “..”, barra inicial e URLs diretas MUST NOT.

6. Qualidade e limites
6.1 Largura de linha e tamanho máximo por arquivo MUST seguir limites do CI.
6.2 UTF-8 válido, sem CRLF/BOM e sem caracteres de controle MUST.
6.3 Linhas em branco finais supérfluas MUST NOT.

7. Terminologia
7.1 Um termo por conceito; concorrência de sinônimos MUST NOT.
7.2 Preferência documentada quando coexistirem termos próximos MUST.

8. Conformidade e publicação
8.1 Rejeitar arquivos que violem qualquer regra MUST.
8.2 Releases devem passar por verificação editorial completa MUST.
8.3 Alterações que mudem semântica exigem registro no CHANGELOG MUST.
