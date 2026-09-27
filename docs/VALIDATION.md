# Relatório de validação

**Versão publicada:** [Padaria Orinoko](https://gustavol266.github.io/Orinoko/). Testes realizados em 27/09/2026, horário de São Paulo.

## Responsividade e navegação

As larguras **320, 375, 390, 768, 1024 e 1440 px** foram verificadas na página publicada. Em todas, a largura do documento não ultrapassou a área disponível, sem overflow horizontal. As medidas estão em [responsive.json](./responsive.json). O conteúdo considera a largura reservada à barra de rolagem.

- Desktop e mobile inspecionados visualmente no navegador.
- Menu mobile aberto pelo teclado; `aria-expanded` acompanhou o estado.
- Escape fechou o menu e devolveu o foco ao botão.
- Link para a localização fechou o menu; âncoras de sabores e visita alcançaram as seções corretas.
- Um único H1; nenhum link sem nome acessível detectado na inspeção do documento.
- Console sem erros ou avisos durante a verificação da página principal.
- Página 404 exibida em rota inexistente; seu link retornou à raiz `/Orinoko/`.
- Foco visível, skip link e regra de movimento reduzido presentes. A inspeção automática não equivale a uma avaliação completa com usuários de tecnologia assistiva.

## Links, conteúdo e assets

- WhatsApp abriu o perfil **Orinoko**, com `5519974111822` e a mensagem exata do briefing. Nenhuma mensagem foi enviada.
- Links de Maps abriram a ficha correta, identificada por nome e endereço. O mapa incorporado carregou o pin da Padaria Orinoko ao entrar na seção de localização.
- Telefone usa `tel:+5519974111822`.
- Instagram não foi incluído porque não houve confirmação da conta oficial.
- CSS, JavaScript e favicon locais carregaram na página publicada.
- Não há fotografias comerciais nem `og:image`; a galeria abre externamente no Maps. Origem documentada em [IMAGE_SOURCES.md](../IMAGE_SOURCES.md).
- Pesquisa, conteúdo observado e afirmações omitidas estão registrados em [RESEARCH.md](./RESEARCH.md). Não há preços, receitas, ingredientes ou serviços não confirmados.
- Canonical, Open Graph textual, viewport e JSON-LD `Bakery` conferidos. A nota não foi incluída como avaliação própria no JSON-LD.
- Auditoria estática de arquivos, âncoras, links, WhatsApp, Maps, dados estruturados e README: `python scripts/verify.py`.
- Sintaxe JavaScript: `node --check js/main.js`.

## Lighthouse / PageSpeed Insights

Relatório oficial criado em **27/09/2026, 00:23 BRT**, após as correções de estabilidade do menu e contraste do texto decorativo. Lighthouse **13.5.0**, HeadlessChromium **153.0.8010.36**.

| Categoria      | Mobile | Desktop |
| -------------- | -----: | ------: |
| Desempenho     |    100 |     100 |
| Acessibilidade |    100 |     100 |
| Boas práticas  |    100 |     100 |
| SEO            |    100 |     100 |

| Métrica exibida          | Mobile | Desktop |
| ------------------------ | -----: | ------: |
| First Contentful Paint   |  0,8 s |   0,2 s |
| Largest Contentful Paint |  0,8 s |   0,2 s |
| Total Blocking Time      |   0 ms |    0 ms |
| Cumulative Layout Shift  |      0 |       0 |
| Speed Index              |  0,8 s |   0,4 s |

[Relatório mobile](https://pagespeed.web.dev/analysis/https-gustavol266-github-io-Orinoko/z5bxk19qsz?form_factor=mobile) · [Relatório desktop](https://pagespeed.web.dev/analysis/https-gustavol266-github-io-Orinoko/z5bxk19qsz?form_factor=desktop) · [Resumo estruturado](./lighthouse-summary.json).

Mobile: Moto G Power emulado, limitação lenta de 4G. Desktop: área de trabalho emulada com limitação personalizada. São medições de laboratório de carregamento inicial e podem variar. O serviço não apresentou dados de campo; não se afirma aprovação de Core Web Vitals com usuários reais. O mapa tem carregamento adiado e pode acrescentar custos ao ser exibido.

## Capturas reais

Capturadas da versão final publicada e convertidas para WebP sem montagem, substituição ou geração de elementos:

- [Desktop](../assets/readme/preview-desktop.webp): viewport 1440 × 1000 px.
- [Mobile](../assets/readme/preview-mobile.webp): viewport 390 × 844 px.

São capturas do projeto, permitidas expressamente no briefing, e não fotografias comerciais. Os arquivos e links foram conferidos antes do commit.

## Limites e pendências editoriais

Há zero fotografias comerciais incorporadas. A ficha indicava 32 mídias, mas o acesso foi limitado; três registros foram examinados, sem alegar uma auditoria de todas as mídias. Não foi identificada autorização explícita de reprodução, por isso adotou-se o fallback tipográfico autorizado pelo usuário.

Logotipo, fotografias autorizadas já presentes na ficha, Instagram oficial, cardápio atual e condições de atendimento devem ser confirmados com a proprietária antes da adoção oficial. A proposta está identificada discretamente como independente.
