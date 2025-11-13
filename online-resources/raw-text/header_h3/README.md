# header_h3 (Cabeçalho Nível 3)

## Propósito

Títulos de nível 3 para estruturação hierárquica do conteúdo. Representam subseções dentro de subseções.

## Características

- **Não usa metadata twin**: Headers são elementos estruturais puros
- **Não conta para baseline**: Headers são componentes de estrutura, não de conteúdo
- **Conteúdo**: Apenas o texto do título (geralmente 1-5 palavras)
- **Encoding**: UTF-8, LF line endings, no BOM
- **Naming**: `NNN-titulo-subsubsecao-XXXX.txt` onde XXXX = SHA256 (4 chars)

## Uso

Headers h3 marcam detalhamentos específicos como "Requisitos de Documentação", "Procedimentos de Reporte", "Exemplos Práticos".

## Hierarquia

- **h1**: Seções principais do documento
- **h2**: Subseções dentro de h1
- **h3**: Subseções dentro de h2 ← VOCÊ ESTÁ AQUI

## Exemplo

```
Procedimentos de Reporte
```

## Validação

- Não há metadata twin (.json)
- Conteúdo deve ser breve (tipicamente < 100 caracteres)
- Não deve conter formatação especial

## Fragmentos Existentes

Total: 0 fragmentos

(Nenhum fragmento criado ainda)
