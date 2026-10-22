# Smart Batch DisneyMkt — atualização de confiabilidade

Utilitário auxiliar para processamento em lote. **Ainda não integra o painel gráfico do editor FotoSmart** e não executa IA.

## Recursos
- Conversão para JPG, PNG e WebP, formatos para redes sociais ou dimensões personalizadas.
- Ajuste por recorte ou encaixe e marca-d'água por imagem/texto.
- Novo: ponto de recorte ajustável com `--foco-x` e `--foco-y` (0 a 1; padrão central 0,5/0,5). **Não é detecção automática de rosto nem recorte por IA.**
- Novo: conferência de espaço livre no destino com `--espaco-min-mb` (padrão 256 MB); proteção preventiva, não é garantia de espaço suficiente para lotes longos.
- Novo: gravação primeiro em um arquivo temporário na pasta de destino e substituição somente após exportação concluída. Temporários criados pela tarefa são apagados após falhas tratadas.
- Preserva imagens de entrada, não substitui saídas existentes sem `--substituir`.
- Processa uma imagem por vez, produz relatório CSV de sucesso e erros.

## Windows
```powershell
py -m pip install -r tools/requirements-smart-batch.txt
py tools/smart_batch.py --entrada "C:\Fotos" --saida "C:\Posts" --formato post --tipo webp --ajuste recortar --foco-x 0.45 --foco-y 0.35
```

## macOS e Linux
```bash
python3 -m pip install -r tools/requirements-smart-batch.txt
python3 tools/smart_batch.py --entrada ./fotos --saida ./posts --formato story --tipo png --ajuste encaixar
```

Para ajuda completa, execute `python3 tools/smart_batch.py --help`.

## Limites e próximas etapas
A limpeza de cache implementada vale apenas para os **arquivos temporários deste utilitário**. Não altera o mecanismo de disco de rascunho/caches internos do editor Rust nem aumenta sua memória disponível. O auto-recorte por detecção de rostos, preenchimento generativo em 4K, orçamento de créditos, avisos sonoros e gerenciamento global de memória permanecem planejados. Para implementar esses módulos no aplicativo, será necessário adaptar a interface Rust e realizar testes reais em Windows, Linux e macOS.
