# FotoSmart DisneyMkt — prioridades de evolução

Baseado nos pontos encaminhados sobre demandas de usuários do Photoshop. Este arquivo separa o que foi codificado daquilo que ainda está em planejamento.

## Já codificado nesta atualização (utilitário Smart Batch)
1. Exportação WebP (recurso anterior mantido e testado).
2. Controle do ponto de recorte por posição focal manual, sem reconhecimento facial.
3. Validação preventiva do espaço livre em disco na pasta de saída.
4. Exportação atômica para diminuir a chance de arquivos incompletos.
5. Processamento sequencial, mantendo originais e log CSV.

## Próximas entregas, ainda não implementadas
1. **Scratch Manager do editor:** selecionar unidade temporária; cache com limites de espaço; limpeza segura e análise de uso; reduzir pico de RAM; testes de recuperação após falhas. Nunca apagar temporários de outros aplicativos.
2. **Smart Auto Crop:** detecção de rostos/objetos e opções de composição por regra dos terços; permitir prévia e correção manual.
3. **Smart Generative:** seleção por máscara, preservação de perspectiva, geração em blocos e composição de alta resolução; requer motor/modelo de IA e testes de qualidade.
4. **Custos de IA:** informar modelo, resolução, estimativa de custo, limites por usuário e histórico de geração antes da confirmação.
5. **Avisos sonoros:** configuração opcional de alerta de conclusão e de erro, respeitando modo silencioso.
6. **Linux nativo:** validar e automatizar empacotamento AppImage/DEB/RPM e codecs/filtros no ambiente de execução.
7. **Exportador web integrado:** otimização WebP na interface do editor e geração automática de ativos por camada.

Os workflows de Windows, Linux e macOS foram preservados, **mas não foram compilados ou validados nesta atualização**.
