# Pedido original e decisões do Portal Cidadão de Pelotas
Domínio: escopo do projeto | Dono: Henrique | Criado em: 23/10/2026 | Atualizar: a cada decisão nova (acrescente na seção "Decisões", com data)

Como usar este arquivo: o pedido original abaixo é a lista completa de desejos do Henrique e serve para nada se perder. As decisões que vêm depois valem mais que o pedido onde os dois discordarem.

## 1. Pedido original (texto do Henrique, na íntegra, 22/10/2026)

> Quero fazer um projeto aqui no claude para criar um site que, a partir dos dados disponíveis publicamente no site da câmara municipal de pelotas (https://www.pelotas.rs.leg.br/), pegue tudo que for necessário de lá, como licitações, contratos, portal da transparência, legislação da câmara, proposições, documentos das sessões plenárias, comissões, e tudo que for importante mais, pra fazer um portal da transparência melhorado, só que com resumos, links para acessos ao texto na íntegra e ao site da câmara, mas facilitando tudo pro cidadão, classificando propostas em categorias, áreas onde cada vereador mais trabalha, o que ele fala nas reuniões, o que ele mais propõe, quais os ideias dele a partir dos dados disponíveis publicamente, onde ele gasta mais, no que ele gasta, classificação dos gastos, tudo fácil de entender. Quero um site limpo, fácil de usar, sem cara de IA, nas cores da câmara de pelotas, nas cores de Pelotas, pra ficar parecido, só que facilitando MUITO mais a visualização de tudo por parte dos cidadãos saberem tudo sobre cada vereador, de forma simplificada, bem categorizada, separadinha, por tempo, com filtragem fácil de entender. É para analisar as propostas e implementações desses vereadores na câmara de pelotas ao vivo diariamente e atualizar o site. Pro cidadão de pelotas poder acompanhar sempre, cada um dos vereadores tudo que eles fazem, categorizadamente, pra todo cidadão poder ver, consultando algum site público, notícias entre outros. Quero que escreva o prompt desse projeto pra fazer esse site, instruções, o que preciso colocar no contexto dele, se algum arquivo algo assim, pra esse site ser criado. A ideia também é ter graus calculados com transparência nesse site com esse cruzamento de todas informações disponíveis, seja nesse site da câmara ou outros sites públicos sobre esses vereadores, não só com as infos do site da câmara, mas de outros disponíveis, cruzar dados, informações e oferecer barras e níveis de participação, pontuação de participação, de atuação nas pautas defendidas por cada um na sua trajetória pública e política (consultando outros sites, notícias, etc.) e ver se cada vereador está sendo coerente com suas pautas e falas públicas, tendo níveis também, grau, de gastos exacerbados, estranhos, sintomas de práticas ilícitas ou irregulares nas suas ações, pra poderem ser cobrados. Tendo também os projetos aprovados na sua trajetória histórica, quantidade deles, resumo, tópicos gerais dos projetos, como ajudou, e também os que estão tramitando, pendentes, mas que partiram deles. Como eles votaram em pautas específicas. Tudo que for de ideia boa pra essa plataforma também deve ser sugerido nesse projeto. Faça pra mim.

## 2. Lista de requisitos extraída do pedido
Use como checklist do que o site precisa cobrir até a versão completa.
- R1 Dados da Câmara: licitações, contratos, transparência, legislação, proposições, documentos das sessões, comissões.
- R2 Resumos em linguagem simples, com link para o texto integral e para a página original da Câmara.
- R3 Proposições classificadas por tema; áreas em que cada vereador mais atua; o que mais propõe.
- R4 O que cada vereador fala nas sessões; suas ideias, a partir de dados públicos.
- R5 Gastos: onde e em que gasta, classificados.
- R6 Filtros simples por vereador, tema, tipo, situação e período.
- R7 Atualização diária automática.
- R8 Cruzamento com fontes externas (TSE, prefeitura, tribunal de contas, notícias).
- R9 Barras e níveis de participação e atuação, com cálculo aberto.
- R10 Coerência entre pautas defendidas em público e atuação.
- R11 Pontos de atenção sobre gastos (ver decisão D3).
- R12 Trajetória histórica: projetos aprovados, quantidade, resumo, temas, efeito; e os em tramitação.
- R13 Como cada um votou em pautas específicas.
- R14 Visual limpo, moderno, sem cara de IA, nas cores de Pelotas e da Câmara.
- R15 Sugestões de ideias boas para a plataforma (ver seção 4).

## 3. Decisões
- D1 (23/10/2026) Ferramentas: assinatura Claude Pro. Este projeto do Claude é o guia; o site é construído com o Claude Code, de preferência na web, ligado a um repositório no GitHub. Lovable não será usado.
- D2 (23/10/2026) Atualização diária: automática por rotinas do Claude Code (recurso em prévia de pesquisa) e coleta agendada; plano B é o Henrique rodar a atualização manualmente. Detalhes no 05.
- D3 (23/10/2026) O "grau de sintomas de práticas ilícitas ou irregulares" foi substituído por alertas objetivos e verificáveis, sempre com link para o documento e sem adjetivos. Motivo: uma nota automática de "sinais de ilegalidade" sobre pessoas com nome e foto gera falsos positivos que podem virar processo por calúnia ou difamação. Regras no 03 e no 06.
- D4 (23/10/2026) Coerência com pautas e uso de notícias: quando faltarem fontes ou elas forem inconclusivas, o site mostra o aviso de cobertura insuficiente em vez de uma nota. Motivo: a cobertura da imprensa é desigual entre vereadores.
- D5 (23/10/2026) Nível técnico do Henrique: básico, com terminal já usado. Todo passo vem explicado.
- D6 (23/10/2026) Visual nas cores de Pelotas e da Câmara, sem copiar a identidade oficial: o site precisa deixar claro que é independente.
- D7 (23/10/2026) Não havia material prévio além do site da Câmara. As fontes do 02 foram mapeadas pelo PromptArchitect em 23/10/2026 e precisam de confirmação técnica na Fase 1.
- D8 (23/10/2026) O Henrique assina o site publicamente, como pessoa física. Cuidados no 06, seção 2.
- D9 (23/10/2026) Fonte principal: a API pública de dados abertos do Portal Legislativo (02, seção 2.1), que já entrega proposições em tempo real. O site institucional da Câmara não bloqueia leitura automática. Redes sociais entram só por curadoria manual.
- D10 (23/10/2026) Imprensa: A Hora do Sul é a primeira candidata a fonte de notícias; outros portais locais serão levantados na Fase 5.
- D11 (23/10/2026) O trabalho roda num projeto da nova versão de Projetos do Claude Code, chamado Meu Vereador: um coordenador recebe os pedidos do Henrique e abre threads na nuvem que trabalham no repositório e entregam pull requests. Isso substitui o arranjo de D1, em que um chat explicava e o Henrique colava prompts no Claude Code. "Meu Vereador" é o nome de trabalho; o nome público final continua em P1.

- D12 (17/11/2026) O índice de atividade parlamentar fica fora da primeira versão do site. Motivo: por usar percentil (posição na fila dos 21 vereadores), ele sempre coloca alguém "abaixo da faixa típica", mesmo quando todos têm números parecidos, e um número único por vereador vira ranking. Os indicadores separados continuam, com valor real e mediana. O índice volta à discussão na Fase 5, com dados reais. Regras no 03, seção 3.
- D13 (17/11/2026) A coerência entre pautas declaradas e atuação (I10) sai do roteiro e vira ideia para depois (seção 5). Motivo: depende de curadoria manual contínua de 21 vereadores e a palavra "contradição" é a de maior risco do site. O indicador de temas de atuação (I5) cobre a maior parte da necessidade.
- D14 (17/11/2026) Atualização diária: a coleta, os testes e a publicação rodam no GitHub Actions (o robô gratuito do GitHub para repositórios públicos, que executa scripts em horário marcado). A tarefa agendada do Claude fica só com o enriquecimento por IA. Se ela falhar, o site atualiza do mesmo jeito. Condição: um teste na Fase 2 confirmar que a API da Câmara responde aos servidores do GitHub; se não responder, vale o arranjo anterior. Isto ajusta a D2. Detalhes no 05.
- D15 (17/11/2026) Recorte inicial: a legislatura atual (2025 a 2028). O histórico anterior, que depende do SAPL antigo, entra depois. Resolve a P5.
- D16 (17/11/2026) Dados pessoais: a API da Câmara devolve CPF, e-mail e telefone dos vereadores. A coleta só pede campos de uma lista permitida e um teste automático recusa qualquer arquivo de dados com formato de CPF ou telefone. Regras no 02, seção 2.1, e no 06, seção 3.
- D17 (17/11/2026) Pedidos de providências (cerca de 20 mil por ano) não passam por resumo de IA nem ganham página própria: o tema sai de regras escritas e eles aparecem em listas por vereador e por mês. Projetos, pedidos de informações, moções e requerimentos seguem com resumo por IA e página própria. Regras no 07, seção 1.1, e no 05.
- D18 (17/11/2026) O e-mail exclusivo do projeto e a verificação em duas etapas da conta do GitHub passam da Fase 6 para a Fase 0. O e-mail identifica o robô, assina os pedidos via SIC e recebe pedidos de correção.

- D19 (17/11/2026) E-mail exclusivo do projeto criado pelo Henrique: meuvereadorrs@gmail.com. É o contato público do site (página Sobre, pedidos de correção), a identificação do robô de coleta e o remetente dos pedidos via SIC.
- D20 (17/11/2026) O projeto não vai avisar a Câmara de que a API pública expõe o CPF dos vereadores. A regra de nunca pedir nem salvar esses campos (D16) continua valendo.

Origem de D12 a D18: análise crítica de 10/11/2026 (documento "Meu Vereador: análise crítica e melhorias"), que o Henrique mandou implementar em 17/11/2026. D12, D13, D14 e D15 mudam escopo e podem ser revertidas por ele a qualquer momento.

## 4. Decisões pendentes (o guia pergunta na fase indicada)
- P1 Nome do site e domínio (Fase 6).
- P2 Resolvida em D8.
- P3 Se o índice de atividade volta e com que regra e pesos (Fase 5; ver D12 e o 03, seção 3).
- P4 Lista final de veículos de imprensa local (Fase 5; ponto de partida em D10).
- P5 Resolvida em D15.
- P6 Resolvida em D20.

## 5. Ideias para o portal (registradas, não priorizadas)
- Seguir um vereador: aviso por e-mail ou RSS quando ele propõe, vota ou gasta algo novo.
- Comparar dois vereadores lado a lado.
- Mapa por bairro: indicações de obras, emendas e locais citados nas proposições.
- Busca "como votou meu vereador" por tema.
- Página "Como funciona a Câmara" e glossário cidadão (o que é indicação, requerimento, moção, votação nominal).
- Resumo semanal da Câmara em linguagem simples.
- Agenda da semana com as pautas das sessões.
- Download dos dados tratados em CSV, para jornalistas e pesquisadores.
- Registro público de correções e espaço para o vereador enviar contexto sobre um dado.
- Versão em leitura fácil para cada página de vereador.
- Entrada por bairro: "o que pediram para o meu bairro". A API tem lista de bairros e filtro por bairro; conferir na Fase 1 se há dado suficiente (na amostra de 10/11/2026 nenhum item tinha coordenada, então talvez dê lista por bairro e não mapa de pontos).
- Tempo de fala por vereador, se a API preencher a lista de oradores (a confirmar na Fase 1).
- Coerência entre pautas declaradas e atuação (antigo I10; ver D13 e o 03, seção 5).
- Aviso de novidades por RSS por vereador (barato num site estático); aviso por e-mail só depois, porque exige guardar dados de leitores.
