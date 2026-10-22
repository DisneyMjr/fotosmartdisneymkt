# FotoSmart DisneyMkt

**Editor de imagens para Windows, Linux e macOS**, desenvolvido em Rust a partir de uma base open source de edição de imagens.

**DisneyMkt** · [Instagram @disneymkt](https://www.instagram.com/disneymkt/)

## Visão geral

O FotoSmart oferece edição raster, ferramentas de pintura, camadas, máscaras, ajustes, filtros e suporte ao fluxo de trabalho com documentos PSD. A compatibilidade exata com funcionalidades do Adobe Photoshop depende da implementação e precisa ser validada em cada versão. Este projeto não é afiliado à Adobe.

## Funcionalidades e novidades

- **Edição:** ferramentas de imagem, máscaras, camadas, filtros e ajustes já presentes na base Rust.
- **Smart Social:** atalhos para documentos de Instagram, Stories, carrossel e YouTube em `File > Smart Social`.
- **Smart Batch (novo, versão inicial):** ferramenta auxiliar de linha de comando para processar pastas de fotos, redimensionar, recortar, converter JPG/PNG/WebP e aplicar logo ou texto como marca-d'água. Nesta versão **não está integrada ao menu do editor**.
- **macOS (novo):** workflow para compilar DMG universal Intel/Apple Silicon, além dos workflows existentes Windows MSI e Linux.

### Smart Batch: exemplo

Instale Python 3 e Pillow:

```bash
python -m pip install -r tools/requirements-smart-batch.txt
```

Processar fotos para post do Instagram:

```bash
python tools/smart_batch.py --entrada minhas-fotos --saida posts-prontos --formato post --tipo jpg --ajuste recortar
```

Aplicar marca da empresa e preservar a proporção das fotos:

```bash
python tools/smart_batch.py --entrada minhas-fotos --saida posts-prontos --formato story --tipo png --ajuste encaixar --logo minha-logo.png
```

Os originais não são alterados. A saída inclui `relatorio-smart-batch.csv`. Consulte `SMART-BATCH.md`.

## Instaladores

| Plataforma | GitHub Actions | Formato |
|---|---|---|
| Windows x64 | `Gerar MSI FotoSmart` | `.msi` |
| Linux x64 | `Gerar Linux FotoSmart` | AppImage, `.deb`, `.rpm`, `.tar.gz` |
| macOS Intel + Apple Silicon | `Gerar DMG FotoSmart macOS` | `.dmg` universal |

Abra **Actions** no seu repositório GitHub, selecione o workflow desejado e execute **Run workflow**. Os pacotes compilados, se a compilação passar, ficam nos **Artifacts** da execução. O workflow macOS utiliza assinatura ad hoc enquanto não houver certificado Apple Developer configurado: esse DMG serve para testes e poderá apresentar restrições do Gatekeeper.

**Estado da validação:** o código-fonte e o workflow foram preparados; a compilação final Windows/Linux/macOS precisa ser executada e conferida no GitHub Actions. Não há binário macOS pronto neste repositório.

## Futuras melhorias

- Smart Remove: seleção de objeto e remoção de fundo assistida por IA.
- Smart Fill: preenchimento e expansão generativa mediante integração com provedor de IA.
- Smart Retouch: ferramentas de retoque não destrutivo.
- Integração nativa do Smart Batch ao painel do FotoSmart.
- Melhorias de desempenho, testes de PSD e gerenciamento de cores.

Os itens acima são **planejados**, não funcionalidades entregues.

## Desenvolvimento

Projeto Rust organizado como workspace Cargo. Consulte `Cargo.toml`, `crates/` e `apps/`. A compilação requer toolchain Rust compatível com a versão definida no workspace e dependências específicas de cada plataforma.

## Licenças, créditos e atribuição

A personalização e as ferramentas adicionadas são apresentadas sob a marca **DisneyMkt**. A base original e seus contribuidores mantêm seus direitos e créditos, conforme `ATTRIBUTION.md`, `NOTICE`, `LICENSE-MIT` e `LICENSE-APACHE`. Arquivos adicionais podem ter suas próprias licenças. A marca FotoSmart não substitui essas obrigações.

Contato e novidades: [@disneymkt](https://www.instagram.com/disneymkt/).
