# header_h1 (Cabeçalho Nível 1)

## Propósito

Títulos de nível 1 para estruturação hierárquica do conteúdo. Representam divisões principais do manual.

## Características

- **Não usa metadata twin**: Headers são elementos estruturais puros
- **Não conta para baseline**: Headers são componentes de estrutura, não de conteúdo
- **Conteúdo**: Apenas o texto do título (geralmente 1-5 palavras)
- **Encoding**: UTF-8, LF line endings, no BOM
- **Naming**: `NNN-titulo-secao-XXXX.txt` onde XXXX = SHA256 (4 chars)

## Uso

Headers h1 marcam seções principais como "Política de Controle da Qualidade", "Requisitos Éticos", "Sistema de Controle".

## Hierarquia

- **h1**: Seções principais do documento ← VOCÊ ESTÁ AQUI
- **h2**: Subseções dentro de h1
- **h3**: Subseções dentro de h2

## Exemplo

```
Requisitos Éticos Fundamentais
```

## Validação

- Não há metadata twin (.json)
- Conteúdo deve ser breve (tipicamente < 100 caracteres)
- Não deve conter formatação especial

## Fragmentos Existentes

Total: 13 fragmentos

- `001-politica-controle-qualidade-cc68.txt`
- `002-introducao-800c.txt`
- `004-sistema-controle-qualidade-0782.txt`
- `005-responsabilidade-lideranca-qualidade-de75.txt`
- `007-normas-aplicaveis-servicos-contabeis-eabc.txt`
- `010-politica-responsabilidade-social-ambiental-climatica-86cb.txt`
- `012-classificacao-entidades-4093.txt`
- `014-exigencias-eticas-relevantes-72f6.txt`
- `016-requisitos-eticos-obrigatorios-e578.txt`
- `019-detalhamento-principios-fundamentais-c589.txt`
- `022-responsabilidades-reporte-requisitos-eticos-4e23.txt`
- `024-conclusao-e27d.txt`
- `031-procedimentos-documentacao-f303.txt`
