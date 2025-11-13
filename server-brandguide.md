# server-brandguide.md — Guia de Marca Universal (server-side, raw-text)

Este guia é obrigatório. Não há opcionais. Regula apenas o repositório público de conteúdo textual (online-resources/raw-text). É independente de cliente, versão e projeto. Sem decisões visuais.

1. Propósito
   Garantir texto cru consistente, legível e verificável. O repositório entrega somente .txt com voz e tom padronizados, prontos para consumo por qualquer cliente.

2. Alcance
   Dentro: conteúdo sob online-resources/raw-text e subpastas. Fora: qualquer renderização, layout, UI, CSS, impressão ou paginação.

3. Princípios

- Clareza sobre estética verbal.
- Precisão sobre generalidade.
- Fatos e limites objetivos sobre opiniões.
- Consistência terminológica e estrutural.
- Acessibilidade textual e leitura rápida.
- Minimalismo: apenas o necessário, sem floreio.

4. Voz e Tom
   Voz: impessoal, assertiva, direta.
   Tom: normativo, técnico, autoritário, profissional e sério.
   Modais permitidos: deve, é obrigatório, é vedado, proíbe-se, pode desde que, recomenda-se.
   Modais proibidos: deveria, busca-se, pretende-se, espera-se, almeja-se, gostaríamos, desejamos, tentamos, procuramos.

5. Linguagem e Estilo

- Texto cru UTF-8, LF, sem BOM. Sem HTML, tags, scripts ou shortcodes.
- Frases curtas, verbo forte; voz ativa preferencial.
- Números em algarismos; unidades no SI quando houver medidas textuais.
- Defina siglas na primeira ocorrência; mantenha-as.
- Evite metáforas, humor, hipérboles e adjetivação gratuita.
- Evite duplicidade de termos para o mesmo conceito.
- Não use exclamação nem pergunta retórica.

6. Estrutura por categoria (um arquivo por item, salvo onde indicado)

- plaintext: parágrafos curtos; linha em branco separa parágrafos.
- callouts: mensagens curtas e objetivas; uma ideia por arquivo.
- docks: observação lateral concisa; limite de 600 caracteres.
- tradeoffs: linhas iniciadas por “+” (pró) e “−” (contra); fatos, sem narrativa.
- faqs: par q.txt e a.txt; pergunta na voz do leitor, resposta objetiva.
- tables: TSV .tsv.txt com cabeçalho; sem fórmulas; valores literais.
- data: TSV .tsv.txt para gráficos derivados; mesmo padrão de tables.
- diagrams: DOT .dot.txt válido e minimalista; um grafo por arquivo.
- disclaimers: aviso legal, privacidade, risco ou experimental; linguagem direta.
- others: conteúdo textual que não se encaixa nas categorias acima; usar com parcimônia.
- meta: dicionários em .json.txt (glossário/abreviações), além de integrity.txt e TREE.txt.

7. Terminologia

- Use termos técnicos do domínio com significado fixo.
- Prefira termos normativos consagrados; registre preferência quando houver sinônimos.
- Evite neologismos e regionalismos quando houver termo padrão claro.

8. Conformidade editorial
   Publicação exige: voz e tom verificados; modais proibidos ausentes; texto cru e válido; categorias corretas; regras por categoria atendidas; tamanho e largura de linha dentro dos limites definidos pelo CI.

9. Proibições

- Qualquer HTML, CSS, script, imagem, PDF ou binário no repositório.
- Placeholders não textuais, marcas visuais e símbolos decorativos sem função textual.
- Links externos fora de política de allowlist documentada no repositório.
