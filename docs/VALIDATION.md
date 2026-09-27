# Relatório de validação

## Estado inicial

Implementação estática concluída. Validação visual final e capturas pendentes da publicação.

## Verificações antes da primeira publicação

- Pesquisa anterior à programação registrada em `RESEARCH.md`.
- JavaScript verificado com `node --check`.
- Auditoria estática disponível em `scripts/verify.py`: arquivos, âncoras, WhatsApp, identificador da ficha, dados estruturados, fontes das imagens e links locais do README.
- Resposta HTTP 200 obtida do servidor local.
- A prévia inicial foi carregada no navegador e sua árvore de acessibilidade mostrou as seções e links esperados.
- As tentativas posteriores de acesso à prévia local foram restringidas pelo ambiente. A validação responsiva será feita no endereço público após a primeira publicação.

## Limites

- Não há fotografia comercial incorporada; a galeria é externa, seguindo o fallback autorizado no briefing.
- Não existe conta de Instagram confirmada para testar.
- Um link `wa.me` correto não comprova que o estabelecimento atende pelo WhatsApp. Nenhuma mensagem será enviada durante testes.
- Metas de Lighthouse não equivalem a resultados medidos.
