<div align="center">

# Orinoko

**Proposta de website para a Padaria Orinoko — Campinas/SP.**

Uma presença digital com composição editorial, conteúdo pesquisado e caminhos diretos para conversar com a padaria e planejar uma visita.

![HTML5](https://img.shields.io/badge/HTML5-54271f?style=flat&logo=html5&logoColor=fffdf7)
![CSS3](https://img.shields.io/badge/CSS3-54271f?style=flat&logo=css&logoColor=fffdf7)
![JavaScript](https://img.shields.io/badge/JavaScript-54271f?style=flat&logo=javascript&logoColor=fffdf7)

[Pesquisa e fontes](./docs/RESEARCH.md) · [Origem das imagens](./IMAGE_SOURCES.md) · [Validação](./docs/VALIDATION.md)

</div>

---

## ✨ Preview

As capturas reais de desktop e celular serão adicionadas após a validação visual da versão publicada. Não foram usados mockups ou capturas geradas.

## 🌐 Site online

Publicação no GitHub Pages em preparação. O endereço será registrado após a confirmação do serviço.

**Repositório:** [GustavoL266/Orinoko](https://github.com/GustavoL266/Orinoko).

## Sobre o projeto

Este projeto apresenta uma proposta de presença digital para a Padaria Orinoko, na Vila Industrial, em Campinas. A experiência prioriza leitura em celulares, contato em um clique e acesso fácil à localização.

A pesquisa na ficha pública do Google Maps antecedeu a implementação. O site utiliza dados confirmados de endereço, telefone, horários e avaliações, além de uma narrativa curta sustentada por uma publicação do Sebrae-SP sobre a empreendedora venezuelana Maria Eugenia Andre Avilez.

## Objetivos

- Apresentar a Orinoko e a história ligada ao estabelecimento.
- Facilitar a conversa pelo WhatsApp e o acesso ao endereço.
- Oferecer uma experiência confortável em celulares e desktops.
- Valorizar informações reais, sem criar receitas, preços, promoções ou serviços.

## Design

A composição combina grandes títulos em serifada, fundo de papel claro, castanho avermelhado e detalhes em cobre. Essa direção é uma interpretação provisória dos tons de madeira e dos tecidos vermelhos observados nos registros da empresa, não uma afirmação de paleta oficial.

O hero é tipográfico e os sabores aparecem em linhas editoriais. A identidade usa o wordmark **ORINOKO** até que o estabelecimento forneça o logotipo oficial. Não há desenhos de produtos ou imagens artificiais para simular fotografias ausentes.

## 📸 Fotografias

**Esta versão não incorpora fotografias comerciais.** Os registros da Orinoko foram examinados no Google Maps, mas não foi encontrada autorização explícita para reprodução no projeto independente. Por isso, a seção de galeria leva à ficha onde as imagens estão publicadas.

Não foram utilizadas imagens geradas por IA, bancos de imagens, fotos de outras padarias ou fotografias do Instagram. Qualquer fotografia incorporada futuramente deverá vir exclusivamente da ficha pública da Padaria Orinoko no Google Maps e ter reutilização autorizada pelo titular.

[Ver origem das imagens e auditoria](./IMAGE_SOURCES.md).

## Funcionalidades

- Layout responsivo e navegação por seções.
- Menu mobile com estado acessível, fechamento por Escape e retorno do foco.
- WhatsApp no header, hero, seção de sabores, CTA final e botão flutuante.
- Links de telefone e acesso à ficha correta no Google Maps.
- Mapa incorporado com carregamento adiado.
- Horários semanais conferidos e nota agregada com data de consulta.
- Dois trechos curtos de avaliações reais.
- Galeria externa no Google Maps.
- SEO local, Open Graph textual e JSON-LD `Bakery`.
- Página 404 personalizada e favicon provisório.
- Navegação disponível também sem JavaScript.

## Tecnologias

| Camada              | Tecnologia                                      |
| ------------------- | ----------------------------------------------- |
| Estrutura           | HTML5 semântico                                 |
| Apresentação        | CSS3, Grid, Flexbox e propriedades customizadas |
| Interações          | JavaScript, sem framework                       |
| Versionamento       | Git e GitHub                                    |
| Hospedagem prevista | GitHub Pages, branch `main`, diretório `/`      |
| Auditoria estática  | Python, biblioteca padrão                       |

O site não usa backend nem exige instalação de dependências para funcionar. Não foi atribuída licença de uso ao projeto: isso também não concede direitos sobre marcas, fotografias ou textos de terceiros.

## Estrutura do projeto

```text
Orinoko/
├── assets/
│   ├── icons/
│   │   └── favicon.svg
│   └── readme/
├── css/
│   └── style.css
├── docs/
│   ├── RESEARCH.md
│   └── VALIDATION.md
├── js/
│   └── main.js
├── scripts/
│   └── verify.py
├── .gitignore
├── .nojekyll
├── 404.html
├── IMAGE_SOURCES.md
├── README.md
└── index.html
```

Pastas de fotografias e de logotipo definitivo não foram criadas porque não há assets autorizados para preenchê-las. As capturas do projeto serão armazenadas em `assets/readme/`.

## Executando localmente

```bash
git clone https://github.com/GustavoL266/Orinoko.git
cd Orinoko
```

Abra `index.html` no navegador. Para usar um servidor local, caso tenha Python instalado:

```bash
python -m http.server 4173
```

Acesse `http://localhost:4173/`. A auditoria estática pode ser executada com:

```bash
python scripts/verify.py
node --check js/main.js
```

## Personalização

| Alteração                                                                     | Arquivo                                                                                                       |
| ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| Telefone, WhatsApp, mensagem inicial, endereço, horários e dados estruturados | `index.html`                                                                                                  |
| História, sabores e avaliações                                                | `index.html`, acompanhados de evidência em `docs/RESEARCH.md`                                                 |
| Cores, tipografia, espaçamentos e breakpoints                                 | `css/style.css`                                                                                               |
| Comportamento do menu e ano do rodapé                                         | `js/main.js`                                                                                                  |
| Instagram                                                                     | Adicionar em `index.html` somente depois de confirmar a conta oficial                                         |
| Fotografias                                                                   | Criar assets apenas após confirmar origem no Maps e autorização; registrar cada arquivo em `IMAGE_SOURCES.md` |
| Logotipo                                                                      | Substituir o wordmark e favicon após receber o arquivo oficial                                                |

Ao editar o telefone ou horários, mantenha os dados visíveis, links e JSON-LD consistentes. As notas e avaliações exibidas são registros da consulta, não uma integração em tempo real.

## Responsividade

O layout considera celulares, tablets, notebooks e desktops. A validação planejada contempla **320, 375, 390, 768, 1024 e 1440 px**, incluindo menu, largura do conteúdo e ausência de rolagem horizontal. Os resultados efetivos são registrados no [relatório de validação](./docs/VALIDATION.md).

## Performance e acessibilidade

- Fontes do sistema, sem downloads de fontes externas.
- CSS e JavaScript locais, sem framework e sem biblioteca de animação.
- Mapa com `loading="lazy"` e dimensões reservadas.
- Estrutura semântica, um único H1 e hierarquia de títulos.
- Link para pular ao conteúdo, foco visível e navegação por teclado.
- Respeito a `prefers-reduced-motion`.
- Metadados locais e dados estruturados factuais.
- Ausência de fotografias pesadas e de `og:image` sem origem autorizada.

O objetivo de Lighthouse é 90+ nas quatro categorias. Nenhuma nota é afirmada sem uma execução registrada; veja o relatório para medições e limitações.

## 📍 Padaria Orinoko

**Vila Industrial — Campinas/SP**

Av. Dr. Carlos de Campos, 327 · CEP 13035-610  
Telefone: [(19) 97411-1822](tel:+5519974111822)  
[Google Maps](https://www.google.com/maps?cid=2691141686588367925)

| Dias             | Horário consultado |
| ---------------- | ------------------ |
| Segunda a quarta | Fechado            |
| Quinta e sexta   | 16h–22h            |
| Sábado           | 14h–20h            |
| Domingo          | 9h–17h             |

Dados consultados em 26/09/2026. Instagram oficial não confirmado. O link de WhatsApp usa o número solicitado no briefing; o funcionamento do canal deve ser confirmado com a proprietária.

## Status

**Implementação pronta; publicação e validação visual em andamento.**

As limitações de fotografias e de informações ainda não confirmadas estão documentadas. Não se declara uma parceria ou aprovação institucional.

## Melhorias futuras

Possibilidades sujeitas à aprovação e às necessidades da empresa:

- Logotipo oficial e fotografias autorizadas que estejam na ficha do Maps.
- Domínio próprio e integração com a conta oficial do Instagram.
- Cardápio digital revisado pela proprietária.
- Catálogo, pedidos ou painel administrativo, se fizerem parte de uma nova etapa.

## Créditos

Projeto demonstrativo desenvolvido para apresentar uma proposta de presença digital à Padaria Orinoko. Fontes públicas e limites da pesquisa estão registrados em [docs/RESEARCH.md](./docs/RESEARCH.md).

> Este projeto é uma demonstração independente e não representa, até eventual aprovação, o website oficial da Padaria Orinoko.

---

**Desenvolvido com foco em design, performance e experiência do usuário.**
