# header_h2 (Cabeçalho Nível 2)

## Propósito

Títulos de nível 2 para estruturação hierárquica do conteúdo. Representam subseções dentro de divisões principais.

## Características

- **Não usa metadata twin**: Headers são elementos estruturais puros
- **Não conta para baseline**: Headers são componentes de estrutura, não de conteúdo
- **Conteúdo**: Apenas o texto do título (geralmente 1-5 palavras)
- **Encoding**: UTF-8, LF line endings, no BOM
- **Naming**: `NNN-titulo-subsecao-XXXX.txt` onde XXXX = SHA256 (4 chars)

## Uso

Headers h2 marcam subseções como "Integridade", "Objetividade", "Competência Profissional".

## Hierarquia

- **h1**: Seções principais do documento
- **h2**: Subseções dentro de h1 ← VOCÊ ESTÁ AQUI
- **h3**: Subseções dentro de h2

## Exemplos

```
Integridade
```

```
Objetividade
```

## Validação

- Não há metadata twin (.json)
- Conteúdo deve ser breve (tipicamente < 100 caracteres)
- Não deve conter formatação especial

## Fragmentos Existentes

Total: 4 fragmentos

- `002-manual-controle-qualidade-cb38.txt`
- `004-documentacao-planejamento-operacao-controle-24c0.txt`
- `025-integridade-9730.txt`
- `032-objetividade-994b.txt`
