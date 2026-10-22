# FotoSmart DisneyMkt - Atualização inicial de produtividade

## Adicionado no código-fonte

Menu **File > Smart Social** com seis predefinições de documentos de imagem:

- Post Instagram: 1080 x 1440 px
- Post quadrado: 1080 x 1080 px
- Story / Reels: 1080 x 1920 px
- Capa horizontal: 1920 x 1080 px
- Thumbnail YouTube: 1280 x 720 px
- Carrossel Instagram: 1080 x 1350 px

As predefinições criam um documento novo usando o comando nativo `file.new` do editor, preservando camadas e ferramentas existentes. Também foi removida uma duplicata do menu de atualizações e o rótulo **Sobre o FotoSmart** foi ajustado.

## Limitações importantes

Este pacote **não implementa todas as funções do Photoshop**. A base já possui diversos recursos de edição, mas ainda precisam ser auditados e comparados individualmente. Remoção automática de fundo, preenchimento generativo, filtros neurais, batch de imagens e suporte avançado a PSD exigem trabalhos adicionais.

Os workflows preexistentes de Windows e Linux foram preservados sem alteração. Não foi executado `cargo check` por ausência de Rust neste ambiente. A compilação no GitHub Actions é obrigatória antes de lançar instaladores.

## GitHub

Após substituir os arquivos no repositório local (preservando `.git`):

```powershell
git add -A
git commit -m "FotoSmart - presets Smart Social e ajustes de menu"
git push origin main
```
