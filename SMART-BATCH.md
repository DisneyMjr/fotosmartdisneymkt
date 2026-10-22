# Smart Batch DisneyMkt — primeira versão

Utilitário auxiliar para produzir imagens em lote a partir de uma pasta. Ainda não está integrado visualmente ao editor FotoSmart.

## Recursos disponíveis

- Tamanhos: post 1080×1440, quadrado 1080×1080, Story 1080×1920, carrossel 1080×1350, thumbnail 1280×720, horizontal 1920×1080 ou personalizado.
- Tipos: PNG, JPG, WebP.
- Ajuste `recortar`: ocupa a imagem inteira, cortando excessos; `encaixar`: mantém toda a imagem, com margens.
- Marca d'água com arquivo PNG e texto simples.
- Proteção dos arquivos originais; não substitui arquivos existentes sem `--substituir`.
- Relatório CSV de execução.

## Windows

```powershell
py -m pip install -r tools/requirements-smart-batch.txt
py tools/smart_batch.py --entrada "C:\Fotos" --saida "C:\Posts" --formato post --tipo jpg --ajuste recortar
```

## macOS / Linux

```bash
python3 -m pip install -r tools/requirements-smart-batch.txt
python3 tools/smart_batch.py --entrada ./fotos --saida ./posts --formato story --tipo png --ajuste encaixar
```

`--help` lista todas as opções. Esta etapa não implementa processamento por IA, edição de PSD em lote ou ligação visual com os painéis Rust.
