# header_h1 (Cabeçalho Nível 1)

## Propósito

Títulos de nível 1 para estruturação hierárquica do conteúdo. Representam divisões principais do manual.

## Características

- **Não usa metadata twin**: Headers são elementos estruturais puros
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
