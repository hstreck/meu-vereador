# Fontes de dados públicas sobre os vereadores de Pelotas
Domínio: coleta de dados | Mapeado por: PromptArchitect em 23/10/2026 (versão 2, com a API do Portal Legislativo e a imprensa local) | Dono: Henrique | Atualizado em 17/11/2026 com a confirmação técnica da Fase 1 (status de cada fonte nas seções 2 a 4; resumo na seção 8) | Revisar: a cada 3 meses, ou quando uma coleta falhar

Legenda de status:
- [link conferido] o endereço existe e foi encontrado em 23/10/2026; o conteúdo e o formato ainda não foram testados.
- [bloqueado para robôs] a ferramenta de leitura usada no mapeamento foi recusada pelo robots.txt do site em 23/10/2026.
- [a verificar] fonte conhecida por conhecimento geral, endereço não conferido nesta data.
- [API confirmada] dados lidos com sucesso por uma API pública em 23/10/2026.
- [confirmado em 17/11/2026] dados lidos na Fase 1; há amostra pequena em dados/brutos/amostras/.
- [parcial] parte foi confirmada; a observação diz o que falta.
- [não confirmado] não deu para testar na Fase 1; a observação diz o motivo.

## 1. Regras de acesso (valem para toda coleta)
- Antes de coletar, leia o robots.txt e os termos de uso do site. Se o robô for proibido, não force: use exportação oficial (CSV, planilha) se houver, ou peça os dados pelo SIC (seção 6).
- Intervalo mínimo de 2 segundos entre pedidos ao mesmo site, ou o que o robots.txt do site pedir, se for maior: SAPL antigo 60 segundos, dados abertos do TSE 10 segundos. Coleta fora do horário de sessão.
- Identificação do robô: nome do projeto, endereço do repositório e o e-mail do projeto, meuvereadorrs@gmail.com (01, D19). Nunca o e-mail pessoal do Henrique. Exemplo de identificação: "MeuVereadorBot/0.1 (+https://github.com/hstreck/meu-vereador; meuvereadorrs@gmail.com)".
- Dados pessoais: nunca pedir nem salvar CPF, e-mail pessoal, telefone ou data de nascimento, mesmo que a fonte entregue (seção 2.1 e 06, seção 3).
- Prefira, nesta ordem: API ou exportação oficial, página HTML, PDF. PDF escaneado precisa de OCR e conferência manual.
- Guarde o documento original (ou o link permanente e a data) de tudo que for coletado. O site sempre aponta para a fonte.
- O ambiente de nuvem do Claude Code bloqueia sites fora de uma lista de permissão. Cada domínio desta lista precisa ser liberado nas configurações de rede do ambiente (ver 05, Fase 0).

## 2. Câmara Municipal de Pelotas
| Fonte | Endereço | O que traz | Status | Observação |
|---|---|---|---|---|
| Site institucional | https://www.pelotas.rs.leg.br/ | Notícias, agenda, páginas institucionais e a lista dos 21 vereadores | [confirmado em 17/11/2026] | O robots.txt permite tudo, menos /viewer/. A página inicial lista os 21 vereadores com partido, cargo e o número de identificação da pessoa, o mesmo da API (amostra: vereadores_pagina_inicial.json). Não bloqueia leitura automática. Os dados estruturados (proposições, sessões, votações) não ficam nele, e sim no Portal Legislativo abaixo |
| Agenda legislativa | https://pelotas.rs.leg.br/agendas | Pautas e eventos | [link conferido] | |
| Portal Legislativo (Città, sistema EPROCLEG) | https://cmpelotas.cittatec.com.br/portal-legislativo/ | Sistema principal do processo legislativo | [confirmado em 17/11/2026] | A página é montada por JavaScript, mas é alimentada por uma API pública de dados abertos. Detalhes na seção 2.1. Fonte número 1 do projeto |
| Vereadores | https://cmpelotas.cittatec.com.br/portal-legislativo/vereadores | Perfis, partido, legislatura | [confirmado em 17/11/2026] | Não há consulta própria de vereadores na API. A lista vem da página inicial da Câmara e de parlamentaresSessao (id da pessoa, nome civil, partido e cargo em cada sessão). Os partidos mudam: o mesmo vereador pode constar com partido diferente no TSE (2024) e na Câmara (hoje) |
| Proposições | https://cmpelotas.cittatec.com.br/portal-legislativo/proposicoes/consulta | Projetos, pedidos de providências, pedidos de informações, requerimentos, moções, emendas, autoria, situação, resultado da votação | [confirmado em 17/11/2026] | Atualizada em tempo real: em 17/11/2026 já havia proposições protocoladas no mesmo dia. Detalhes na seção 2.2. O texto integral (PDF) não foi achado: ver 2.2 |
| Sessões plenárias | https://cmpelotas.cittatec.com.br/portal-legislativo/sessoes/plenarias | Sessões, presenças, votos de cada vereador, tempo de fala | [confirmado em 17/11/2026] | Presença e voto individual: sim. Tempo de fala: sim, mas só em parte das discussões. Pauta e ata: não vieram pela API (a lista de atividades da sessão vem vazia). Detalhes na seção 2.2 |
| Mesa Diretora | https://cmpelotas.cittatec.com.br/portal-legislativo/mesa | Composição da Mesa | [confirmado em 17/11/2026] | O cargo de cada vereador (PRESIDENTE, VICE_PRESIDENTE_1, SECRETARIO_1 etc.) vem em parlamentaresSessao, sessão a sessão. O presidente aparece com "sem voto" nas votações (ver 03, princípio 6) |
| Comissões | https://cmpelotas.cittatec.com.br/portal-legislativo/comissoes/ | Membros, reuniões, pareceres | [parcial] | Reuniões de comissão (CCJ, COF) aparecem na consulta de sessões, mas só 9 em 2026 e nenhuma em 2025. Existe o tipo PARECER COMISSÃO e o campo idRelator nas proposições (não testados). Não achei consulta com os membros de cada comissão. Falta confirmar com a Câmara (rascunho de pedido na seção 6.1) |
| Portal da Transparência (AVMB) | https://cmp.portaltransparencia.avmb.com.br/ | Provavelmente despesas, folha, diárias, contratos | [bloqueado para robôs] | Confirmado de novo em 17/11/2026: o robots.txt diz "Disallow: /" para todos. Não coletar por robô. Procurar botão de exportação pelo navegador; se não houver, pedir via SIC (seção 6). Os dados abertos do TCE-RS (seção 4.1) cobrem parte do que esse portal mostraria |
| Compras e licitações | https://www.pelotas.rs.leg.br/publicacoes-oficiais-subcategoria/transparencia/29b36a16b61442e392b6286c7c748f7f | Publicações de licitações | [link conferido] | |
| Publicações diversas | https://www.pelotas.rs.leg.br/publicacoes-oficiais-subcategoria/transparencia/5ee0fc765e1b48bb5ee35f0e13e39b86 | Atos e publicações | [link conferido] | |
| LicitaCon (TCE-RS), órgão Câmara | https://portal.tce.rs.gov.br/aplicprod/f?p=50500:4:::NO::F50500_CD_ORGAO,:54401,&cs=1v6RUv69tJi1anZXFMmlm9IhNBKc | Licitações e contratos da Câmara informados ao Tribunal de Contas | [bloqueado para robôs] | O robots.txt de portal.tce.rs.gov.br diz "Disallow: /aplicprod/", e este endereço está nessa pasta. Não coletar por aqui. Os mesmos dados saem em arquivo nos dados abertos do TCE-RS (seção 4.1) |
| Legislação da Câmara (Leis na Web) | https://leisnaweb.com.br/pesquisa-de-atos/?host=pelotas | Leis e atos | [link conferido] | Serve para saber quais proposições viraram lei |
| SAPL antigo | https://sapl.pelotas.rs.leg.br/ | Normas e matérias de anos anteriores (há PDFs de 2013 e 2014) | [confirmado em 17/11/2026] | A API devolve JSON paginado: 47.354 matérias, de maio de 2005 a fevereiro de 2021 (a mais recente da lista). Os anos de 2021 em diante estão no Portal Legislativo (a partir de 2019 há proposições lá, com numeração em outro formato). Abriu em 23/10/2026, inclusive /api/. O robots.txt pede 60 segundos entre pedidos e bloqueia só PDFs de documentos acessórios. Fonte do histórico anterior a 2025, que fica para depois (01, D15) |
| Lei Orgânica e Regimento Interno | https://pelotas.rs.leg.br/pagina/lei-organica-de-pelotas e https://pelotas.rs.leg.br/pagina/regimento-interno | Regras de funcionamento | [link conferido] | Usar para o glossário e para entender tipos de proposição e votação |
| Transmissões (Rede Câmara) | https://www.youtube.com/@redecamarapel | Vídeos das sessões | [link conferido] | Transcrever vídeo é caro e o YouTube costuma bloquear servidores de nuvem. Prefira as atas; vídeo só como link de referência |
| SIC e Ouvidoria | https://cmpelotas.cittaweb.com.br/citta/#/sic/formulario | Pedido formal de dados | [não confirmado] | O domínio é bloqueado pela rede do ambiente (17/11/2026), então o formulário não foi aberto. Ver seção 6 e os rascunhos da 6.1 |
| Redes sociais da Câmara | Instagram, Facebook e Flickr (@camarapelotas) | Comunicação institucional | [link conferido] | Baixa prioridade; não automatizar coleta em rede social |

### 2.1 API pública do Portal Legislativo (descoberta em 23/10/2026, conferida em 10/11/2026)
O próprio portal da Câmara busca os dados numa API de dados abertos do sistema EPROCLEG, da Città. Ela foi lida com sucesso pelo navegador em 23/10/2026.
- Endereço principal: https://cmpelotas.cittatec.com.br/api/open-data-leg/public/graphql (consultas do tipo GraphQL, enviadas por POST).
- Cabeçalho obrigatório: `ID-Tenant: cmpelotas`. Sem ele a API responde "Tenant recusado".
- Consultas disponíveis: processos, proposicoes, relacionados, timeline, eventosTimeline, sessoes, votacao, parlamentaresSessao, processosGeolocalizacao.
- Exemplo do que vem em proposicoes: id, título com tipo e número (ex.: "PEDIDO DE PROVIDÊNCIAS Nº 17598/2026"), descrição completa, datas de cadastro, protocolo e publicação, autores com id e nome, situação e situação da tramitação, id do documento.
- Outros endereços úteis vistos na mesma página: /api/open-data-leg/public/classificacoes, /reparticoes, /tramitacoes e /api/cidades/7965/bairros (lista de bairros, útil para o mapa por bairro).
- Uso responsável: é uma API pública, mas não documentada. Fazer poucas consultas, com intervalo, de preferência paginadas e só do que mudou desde a última coleta. Na Fase 1, mandar um e-mail ou pedido via SIC à Câmara perguntando se há documentação ou termos de uso dos dados abertos; se o formato mudar sem aviso, a coleta quebra e os testes (05) precisam acusar.
- Conferido em 10/11/2026 (poucas consultas, 2 segundos de intervalo):
  - A estrutura da API pode ser lida por introspecção, desde que a consulta seja leve (pedir a lista de campos uma vez só; a consulta pesada é recusada).
  - Paginação: no máximo 50 registros por página. Um ano de proposições leva cerca de 15 minutos para baixar.
  - Presença: a consulta parlamentaresSessao exige o filtro ID_SESSAO e devolve, por vereador, o campo estevePresente. Na sessão ordinária de 05/11/2026 havia 18 presentes de 21. O indicador de presença (03, I1) vem daqui, sem ata e sem IA.
  - A consulta sessoes lista também reuniões de comissão (CCJ, COF), com controle de frequência. Serve à atuação em comissões (03, I2).
  - Voto individual e tempo de fala: a estrutura prevê os dois (votacaoParlamentares; discussaoParlamentares com segundosDiscutidos) e há os endereços /api/open-data-leg/public/votacoes-parlamentares/{id}/votos e /discussoes/{id}/oradores. Mas a lista de atividades veio vazia nas sessões testadas e a consulta votacao exige ID_VOTACAO. Não confirmado se Pelotas preenche esses dados. É a primeira pergunta da Fase 1.
  - Volume: em 10/11/2026 a numeração estava em Pedido de Providências nº 18.315/2026, e 44 dos 50 itens mais recentes eram pedidos de providências. Metade das descrições tem até 280 caracteres, com abertura padrão.
  - Tipos vistos além dos previstos: INDICAÇÃO, EMENDA, PARECER, MEMORANDO.
  - Nomes: o autor da proposição vem com nome parlamentar ("VEREADOR JUNIOR FOX"); a presença vem com nome civil. A coleta mantém uma tabela de identidade que liga os dois pelo id.
- Campos proibidos: o tipo Pessoa devolve documento (CPF completo, nos 21 vereadores), email e, para alguns, fone, além de nascimento. A coleta nunca pede esses campos (nessa API basta não listá-los na consulta) e nunca os salva. Campos permitidos de Pessoa: id, nome, imagem, biografia. Um teste automático recusa qualquer arquivo em dados/ com sequência no formato de CPF ou telefone (05, seção 3).
- Fase 1 (17/11/2026): as perguntas pendentes foram respondidas na seção 2.2.

### 2.2 O que a API entrega de fato (Fase 1, conferido em 17/11/2026)
Foram poucos pedidos, 2 segundos de intervalo, identificação do robô com o e-mail do projeto. As amostras estão em dados/brutos/amostras/camara/ e o script que as gera é coleta/amostras_fase1.py.

**Primeira pergunta: a API traz o voto de cada vereador e a lista de oradores? Sim para os dois, com limites.**

*Como cada consulta funciona*
- sessoes: lista sessões (filtros ANO, PROCESSO, DATA_SESSAO e outros; o valor do filtro é um texto só, por exemplo `{key:ANO,value:"2026"}`). Cada sessão traz data, início, fim, tipo (ordinária, extraordinária, solene, representativa, reunião de comissão) e situação. O campo atividades vem sempre vazio (0 de 323 sessões de 2025 e 2026), então a pauta e as matérias votadas em cada sessão não saem por aqui.
- parlamentaresSessao (filtro ID_SESSAO): os 21 vereadores da sessão, com id da pessoa, nome civil, partido, cargo na Mesa e estevePresente (verdadeiro ou falso). É a fonte da presença (03, I1).
- proposicoes (filtros ANO_DOCUMENTO, CLASSIFICACAO, AUTOR_PESSOA, DATA_PROTOCOLO, STATUS, FULLTEXT e outros): o filtro CLASSIFICACAO recebe o id do tipo, não o nome (lista na tabela abaixo). Traz título, número, ano, descrição, datas, tipo, situação, situação da tramitação, resultado da votação (APROVADO, AGUARDANDO etc.) e autores com participação (AUTOR ou COAUTOR; em 50 projetos de lei de 2025, 2 tinham mais de um autor).
- votacao (filtro ID_VOTACAO, obrigatório): totais da votação (favoráveis, contrários, abstidos, ausentes) e o voto de cada parlamentar. Não existe consulta que liste as votações de uma sessão: os números de votação são percorridos em sequência.
- Endereços REST na mesma API, mais completos para votos: `/api/open-data-leg/public/votacoes-parlamentares/{id}/votos` (título da votação, indicador de votação simbólica ou secreta, id da sessão e o voto de cada vereador) e `/api/open-data-leg/public/discussoes/{id}/oradores` (quem falou e por quanto tempo). Atenção: o endereço REST de votos devolve e-mail e outros dados pessoais do vereador dentro de cada voto (conferido). O coletor tem de descartar esses campos antes de gravar qualquer coisa. Se houver caminho pelo GraphQL (que deixa escolher os campos), ele é preferível; o título da votação e o id da sessão só saem pelo REST.
- Tipos de proposição (id do filtro): projeto de lei ordinária 25; projeto de lei complementar 29; projeto de resolução 26; projeto de decreto legislativo 30; projeto de emenda à Lei Orgânica 39; requerimento 10; pedido de informações 34; pedido de providências 33; indicação 32; moção 31; emenda impositiva 270; ofício de emenda 266; emenda 36; voto de congratulações 49; requerimento de CPI 284; parecer de comissão 73; lei ordinária 81; mensagem 28; veto total 40; veto parcial 41. A lista completa tem 53 tipos (alguns marcados "INATIVO", como "requerimento de concessão de diárias"). A lista vem de `/api/open-data-leg/public/classificacoes?modulo=LEGISLATIVO`.

*Voto individual (03, I7)*
- Em todas as 90 votações sondadas entre fev/2025 e jun/2026, o voto de cada vereador estava registrado e nenhuma era simbólica ou secreta.
- Valores do voto: FAVORAVEL, CONTRARIO, ABSTIDO, SEM_VOTO (aparece só para o presidente) e AUSENTE.
- Cuidado 1: AUSENTE no voto não quer dizer falta na sessão. Na amostra, a mediana foi de 7 AUSENTE por votação, mas só 2 vereadores não estavam presentes na sessão. Quem estava na sessão e não registrou voto também aparece como AUSENTE. Por isso o site deve mostrar "sem voto registrado" e nunca "faltou" a partir do voto. A mediana foi de 13 votos expressos (favorável, contrário ou abstido) por votação.
- Cuidado 2: 12 das 90 votações eram "VOTAÇÃO AGRUPADA" (várias matérias de uma vez), e o voto individual não diz quais matérias eram. Nas demais, o título tem o tipo e o número da matéria (por exemplo "PEDIDO DE INFORMAÇÕES Nº 1014/2026"), no mesmo formato do título da proposição. A ligação voto-proposição pelo título ainda precisa ser testada na Fase 2.
- Só 18 das 90 votações tiveram algum voto contrário ou abstenção. Votações sem divergência dizem pouco sobre posição: o indicador precisa mostrar isso.
- Desde quando: as votações começam em fevereiro de 2022 (número 100 = 16/02/2022). A legislatura atual começa por volta do número 2.700 (25/02/2025) e vai até cerca de 5.100 (10/11/2026). São uns 2.400 números a percorrer (cerca de 80 minutos na primeira carga, com 2 s de intervalo) e depois só os novos a cada dia. Dos 99 números sondados, 9 vieram vazios.
- A sessão de cada votação sai do REST (campo sessaoPlenaria do parlamentar).

*Oradores e tempo de fala (03, I6)*
- O endereço de oradores traz, por discussão: vereador (id da pessoa), ordem, início e fim, segundos concedidos e segundos usados. O campo assunto veio vazio nos 260 registros vistos.
- Dos 267 números de discussão sondados (de 3.500 a 7.500, com passo de 15), 87 tinham oradores, entre março de 2025 e novembro de 2026, em média 3 oradores por discussão e uns 220 segundos por orador (mediana). Os números chegam a cerca de 6.900 (nov/2026); a primeira carga percorre uns 3.400 números (cerca de 2 horas). A discussão não traz a sessão nem a matéria: a ligação com a sessão terá de ser feita pela data e hora (a testar na Fase 2).
- Não sabemos se falas de Tribuna e pronunciamentos fora da discussão de matéria são registradas aqui. Pergunta para a Câmara (6.1). Quem falou e por quanto tempo vem da API, sem IA. O que foi dito não vem.

*Textos e atas*
- Cada proposição e cada sessão têm um documento (identificador do tipo UUID). Não achei endereço público para baixar o PDF entre os que testei; a ata de cada sessão também não saiu pela API. Sem isso, o resumo por IA (07) de projetos e as falas (03, I6) ficam sem o texto integral. Pergunta para a Câmara (6.1) e verificação com navegador na Fase 2.
- A descrição da proposição pode ser curta demais para resumir (por exemplo, "projeto de lei"). As emendas impositivas trazem o destino e, às vezes, o valor no texto da descrição.

*Autoria e identidade*
- O id do autor numa proposição (por exemplo, 133) é de um cadastro do gabinete, e não o id da pessoa (por exemplo, 2315). O filtro AUTOR_PESSOA aceita o id da pessoa e devolveu as proposições certas, então a tabela de identidade pode ser montada por consulta e não só por nome. O nome do autor vem como "VEREADOR NOME CIVIL" ou nome parlamentar, o da presença vem com nome civil.

*Quantidade de proposições (último número usado no ano, em 17/11/2026)*
| Tipo | 2025 | 2026 (até 17/11) |
|---|---|---|
| Pedido de providências | 27.824 | 19.116 |
| Pedido de informações | 748 | 1.050 |
| Requerimento | 303 | 239 |
| Moção | 196 | 138 |
| Projeto de lei ordinária | 158 | 155 |
| Indicação | 117 | 137 |
| Projeto de decreto legislativo | 63 | 38 |
| Emenda impositiva | 456 | 1 |
| Projeto de resolução | 23 | 13 |
| Projeto de lei complementar | 6 | 3 |
| Requerimento de CPI | sem registro | 9 |
O último número do ano é uma boa estimativa da quantidade, mas pode haver falhas na numeração. Em 2025 os pedidos de providências passaram de 27 mil (o 01, D17, e o 05 falam em cerca de 20 mil por ano; a ordem de grandeza vale, mas o número é maior). Em 2025 a Câmara registrou as emendas impositivas ao orçamento de 2026 como proposições; em 2026 aparece só 1.
- Sessões: 171 em 2025 (139 ordinárias, 19 extraordinárias, 6 solenes, 6 representativas, 1 de instalação) e 152 em 2026 até 17/11 (116 ordinárias, sendo uma em andamento no dia, 17 extraordinárias, 4 solenes, 6 representativas e 9 reuniões de comissão).
- Presença: a regra de quais tipos de sessão contam para a frequência vem do campo contabilizaFrequencia de cada tipo (verdadeiro nos tipos vistos); conferir tipo a tipo na Fase 2.
- Fora do ar ou lento: a API respondeu sempre; uma consulta pesada de introspecção é recusada (BadFaithIntrospection), como já anotado.
- Documentação e termos de uso: não achei. O pedido à Câmara está no rascunho 1 da seção 6.1.

### 2.3 Busca adicional por outras fontes (17/11/2026, a pedido do Henrique)
Objetivo: ver se os dados que faltam (gastos por gabinete, atas, comissões) estão em outro lugar, antes de pedir à Câmara.
- Site da Câmara (www.pelotas.rs.leg.br): o mapa do site tem 1.156 endereços. Não há página de despesas, diárias, folha, verba de gabinete ou ressarcimentos por vereador. O que existe na área de transparência: compras e licitações, editais, concursos, publicações diversas (2 itens recentes), a relação nominal de estagiários (nomes de pessoas comuns, não coletar) e o link para o portal AVMB. A agenda tem audiências públicas por vereador, que podem virar um dado a mais (a avaliar). O Portal do Servidor (cittaweb) é bloqueado pela rede do ambiente.
- Portal da Transparência da Câmara (AVMB): a busca na internet não achou nada sobre ele além do próprio link; o robots.txt continua proibindo robôs. O único caminho aberto é a exportação ou o pedido formal.
- TCE-RS: não achei folha de pagamento de servidores municipais como dado aberto (só os empenhos, contratos, licitações e balancetes da seção 4.1). A folha de assessores, portanto, não sai por ali.
- Imprensa e outras fontes: nenhuma notícia ou documento sobre gasto de gabinete de vereadores de Pelotas. A Câmara noticiou uma sessão representativa sobre o não pagamento de emendas (https://pelotas.rs.leg.br/noticia/sessao-representativa-discute-nao-pagamento-de-emendas/135041b251394e2ca710c899021dc655), que mostra que a execução das emendas é assunto de interesse e reforça o pedido à prefeitura. O SAPL antigo publica relatórios de votação nominal em PDF, mas só do período anterior.
- Conclusão: para gastos por gabinete (assessores, material, verba) e para o texto de atas e comissões não há outra fonte aberta além do que está nas seções 2 a 4. Os dados abertos do TCE-RS continuam sendo o único substituto parcial para gastos. Se o Henrique mudar de ideia, o item 6 do rascunho 1 é o que mais vale enviar sozinho.

## 3. Prefeitura de Pelotas
| Fonte | Endereço | O que traz | Status | Observação |
|---|---|---|---|---|
| Manual de emendas impositivas | https://www.pelotas.com.br/transparencia/manual_emendas | Regras das emendas individuais dos vereadores | [confirmado em 17/11/2026] | A página redireciona para o PDF /arquivos/manual_emendas_impositivas.pdf. Em 2025, valor por vereador de R$ 1.335.559,76; metade obrigatoriamente para saúde; limite de 2% da receita corrente líquida |
| Lista de emendas por vereador | https://transparencia.pelotas.rs.gov.br/emendas/impositivas | Destino, valor, beneficiário, execução | [parcial] | Localizada em 17/11/2026 (lida pelo navegador do computador do Henrique). A página tem busca por secretaria, bancada, parlamentar e ano, e links para as relações de 2024 e 2025 (documentos), relatório de execução das emendas de 2025, impedimentos técnicos e respostas dos vereadores. O filtro de parlamentar lista os vereadores da legislatura anterior e o de ano mostra só 2024. O arquivo emendas.csv (storage01.pelotas.com.br) respondeu erro 500 nesta data e a tabela da busca não foi lida. Falta: confirmar se as emendas de 2025 e 2026 aparecem por vereador, com valor e execução. Rascunho de pedido na seção 6.1 |
| Legislação municipal | https://leismunicipais.com.br/prefeitura/rs/pelotas | Leis sancionadas | [bloqueado para robôs] | Em 23/10/2026 o site respondeu com verificação anti-robô. Usar o Leis na Web (seção 2) no lugar |
| Portal da transparência da prefeitura | https://transparencia.pelotas.rs.gov.br/ (o endereço antigo, www.pelotas.com.br/transparencia, é a página de entrada e redireciona) | Receitas, despesas, convênios e transferências, emendas, licitações | [parcial] | O robots.txt permite tudo. Bloqueado pela rede do ambiente de nuvem; o navegador do computador do Henrique abre. A página de despesas e de convênios não foi lida nesta fase. Diário Oficial da prefeitura: redireciona para https://www.diariomunicipal.com.br/famurs (bloqueado pela rede do ambiente) |

## 4. Fontes externas
| Fonte | Endereço | O que traz | Status | Observação |
|---|---|---|---|---|
| TSE, DivulgaCandContas | https://divulgacandcontas.tse.jus.br | Candidatura, bens declarados, receitas e despesas de campanha | [bloqueado para robôs] | Em 23/10/2026 o site recusou o acesso automático. Usar o Portal de Dados Abertos abaixo |
| TCE-RS, dados abertos | https://dados.tce.rs.gov.br | Empenhos, liquidações e pagamentos da Câmara por credor, licitações, contratos, balancetes | [confirmado em 17/11/2026] | A hipótese se confirmou em parte: traz despesas por credor, inclusive pagamentos em nome de vereadores, e contorna o portal da Câmara. Atraso de vários meses no ano corrente. Detalhes na seção 4.1. Domínio ainda bloqueado pela rede do ambiente de nuvem (preciso do Henrique para liberar) |
| Querido Diário (Open Knowledge Brasil) | https://queridodiario.ok.org.br (hoje queridodiario.org.br; API em api.queridodiario.ok.org.br) | Diários oficiais de municípios, com busca e API | [não confirmado] | Em 17/11/2026 o site abre, mas a API devolveu erro 503 ("no available server") e o domínio é bloqueado pela rede do ambiente. Não deu para saber se Pelotas está coberta. O robots.txt do site tem aviso de sinais de conteúdo que precisa ser lido antes de coletar. Refazer o teste depois; o diário da prefeitura (Famurs) é outra fonte possível |
| TSE, Portal de Dados Abertos | https://dadosabertos.tse.jus.br | Os mesmos dados em arquivos para download, por eleição | [confirmado em 17/11/2026] | O robots.txt pede 10 segundos entre pedidos e bloqueia /api/ e buscas: só download de arquivos. Os arquivos ficam em cdn.tse.jus.br (acessível). Detalhes e amostra na seção 4.2 |
| Receita Federal, CNPJ em dados abertos | [a verificar] | Sócios de empresas | [não confirmado] | Só na fase avançada, para cruzar fornecedores e beneficiários; alerta derivado exige revisão humana (03) |
| Cadastros de sanções CEIS e CNEP (Portal da Transparência federal) | [a verificar] | Empresas punidas | [não confirmado] | Os domínios portaldatransparencia.gov.br e dadosabertos.rfb.gov.br são bloqueados pela rede do ambiente (17/11/2026); não testados. Só importam para os alertas A5 e A6, que ficam para a Fase 5 |
| A Hora do Sul | https://ahoradosul.com.br/ | Notícias de Pelotas e região, política local | [confirmado em 17/11/2026] | O robots.txt permite tudo e indica o mapa do site (https://ahoradosul.com.br/sitemap_index.xml, abre). O RSS está em /feed (responde com redirecionamento 301). Falta a Fase 5 testar o conteúdo. | Jornal do Grupo A Hora, que abriu operação em Pelotas em junho de 2024, depois do fim do Diário Popular (12/06/2024). O mesmo grupo comprou a Rádio Pelotense em 2025. Principal candidato a fonte de imprensa |
| Pelotas Agora | https://pelotasagora.com.br/ | Notícias locais | [confirmado em 17/11/2026] | O robots.txt permite tudo, menos /admin, /api/ e /auth/. Não tem RSS em /feed (erro 404). Avaliar na Fase 5 |
| Outros portais locais | Levantar na Fase 5 com o Henrique (P4) | Falas públicas, pautas declaradas, contexto | [a verificar] | Critério de entrada: veículo identificado, com expediente e data nas matérias. Para cada um, verificar se tem RSS ou mapa do site, que permitem coleta leve; ler robots.txt e termos. Guardar só título, data, link e um resumo próprio, nunca o texto da matéria (direito autoral) |
| Perfis públicos dos vereadores em redes sociais | Instagram, Facebook, X, TikTok dos vereadores | Pautas declaradas, falas públicas | [a verificar] | Não automatizar: as redes exigem login, bloqueiam robôs e os termos de uso proíbem coleta automática. Curadoria manual: o Henrique registra a postagem relevante (link, data, tema, frase curta) num formulário ou planilha do projeto, que alimenta as "pautas declaradas" do 03. Sites próprios dos vereadores, se houver, podem ser coletados normalmente |
| Referência de método | Operação Serenata de Amor (projeto cívico que analisou reembolsos de deputados federais com robô) | Inspiração para alertas objetivos | [a verificar] | Estudar como ela descrevia suspeitas sem acusar, antes da Fase 5 |

### 4.1 TCE-RS, dados abertos (Fase 1, 17/11/2026)
Lido pelo navegador do computador do Henrique, porque o domínio é bloqueado pela rede do ambiente de nuvem (seção 7). É um portal CKAN (modelo comum de portais de dados abertos) com 73.440 conjuntos. O robots.txt pede 10 segundos entre pedidos e proíbe /api/ e algumas páginas internas. O coletor deve usar só as páginas de conjunto e os links diretos dos arquivos, nunca /api/. (Uma única consulta a /api/3 foi feita por engano durante o teste, sem repetir.)
- Para Pelotas há 284 conjuntos. Os da Câmara (código do órgão 54401, nome "CM DE PELOTAS"): despesa orçamentária por empenhos (um por ano, de 2004 a 2026; o de 2015 não apareceu na lista), balancete de verificação (um por ano, vários anos) e, sem ano, contratos e licitações.
- Link direto, com padrão estável: `https://dados.tce.rs.gov.br/dados/municipal/empenhos/AAAA/54401.csv.zip` (também em .7z). O arquivo de 2025 tem 37 KB compactados e 8.584 linhas; o de 2026 tem 1.018 linhas. CSV com separador vírgula, UTF-8, uma linha por operação (empenho E, liquidação L ou pagamento P).
- Campos (48): órgão e unidade orçamentária, tipo de operação, datas, número do empenho, função e subfunção, programa, elemento e rubrica de despesa, fonte de recurso, credor (código, nome, tipo de pessoa, CPF ou CNPJ), histórico, valores de empenho, liquidação e pagamento, e licitação e contrato quando há. O histórico é texto livre.
- Atraso: o arquivo de 2026 foi atualizado em 08/11/2026, mas a última operação nele é de 27/02/2026 (campo mes_recebimento = 2). O de 2025 está completo (mes_recebimento = 12, até 29/12/2025). Ou seja, o TCE publica com vários meses de atraso, e o indicador de gastos não é "ao vivo".
- Dados pessoais: o campo CPF ou CNPJ do credor traz CPF de pessoas físicas (servidores, assessores, vereadores). Não salvar. O nome do credor pessoa física também é dado de pessoa: guardar só o que for do vereador e de pessoa jurídica, e nunca o histórico sem revisão (pode ter nome de terceiros).
- O que se vê nos gastos da Câmara em 2025: 93 rubricas. Em 5 rubricas o credor tem o nome civil de algum dos 21 vereadores (conferência só pelo nome, ainda a validar): diárias no país (620 de 2.477 linhas, 18 vereadores, R$ 342,7 mil pagos em nome deles), combustíveis e lubrificantes (485 de 593 linhas), serviços de cópias e reprodução (393 de 396), comunicação de dados (108 de 233) e telecomunicações (105 de 147), além de passagens e material para festividades. Isso sugere ressarcimento de despesas do gabinete pagas em nome do vereador, mas não confirmei o que cada rubrica significa nem se o histórico traz o período. O pagamento de subsídios (R$ 5,1 milhões em 2025) não aparece por vereador (credor agregado). Gastos com assessores e materiais do gabinete não são separados por vereador.
- Amostra: dados/brutos/amostras/tce_rs/empenhos_cm_pelotas_2025_amostra.json (4 linhas, sem credor e sem histórico).
- Contratos e licitações da Câmara: existem como conjuntos próprios (formato ZIP); a estrutura não foi aberta nesta fase.

### 4.2 TSE, dados abertos (Fase 1, 17/11/2026)
- Funciona direto do ambiente de nuvem. As páginas de conjunto ficam em dadosabertos.tse.jus.br (robots.txt: 10 s entre pedidos, sem /api/) e os arquivos em cdn.tse.jus.br, sem robots.txt (o endereço devolve "não encontrado").
- Candidatos 2024 (`.../odsele/consulta_cand/consulta_cand_2024.zip`, 64 MB, atualizado em 17/11/2026): um CSV por estado, separador ponto e vírgula, codificação Latin-1. Em Pelotas houve 257 candidaturas a vereador: 21 eleitos (14 por quociente partidário e 7 por média), 151 suplentes, 80 não eleitos e 5 nulos. O arquivo traz CPF, e-mail, data de nascimento e título de eleitor: o coletor só pode ler as colunas da lista permitida (código do candidato, nome, nome de urna, partido, cargo, situação).
- Bens declarados (`.../odsele/bem_candidato/bem_candidato_2024.zip`, 44 MB): tipo, descrição e valor de cada bem, ligados ao candidato pelo código. Dos 21 eleitos, 19 têm bens no arquivo e 2 não têm (isso vale como "sem registro", não como zero).
- Prestação de contas (`.../odsele/prestacao_contas/prestacao_de_contas_eleitorais_candidatos_2024.zip`, 1,3 GB): contém receitas (87 MB só no RS), despesas pagas e contratadas e doador originário. Colunas de receita confirmadas (origem, espécie, doador, valor, data). O arquivo traz CPF e CNPJ de doadores: guardar só valores agregados e doadores que sejam empresas ou partidos, ou o que o 06, seção 3, permitir. Para não baixar 1,3 GB, dá para ler só o arquivo do RS por leitura parcial do ZIP (testado: funciona com 5 pedidos).
- Eleições anteriores (2020 e 2016) seguem a mesma estrutura; não foram baixadas. Votos por candidato e zona ficam em outro conjunto, não testado.
- Amostra: dados/brutos/amostras/tse/eleitos_pelotas_2024.json (21 eleitos, só campos permitidos).

## 5. Lacunas conhecidas (atualizadas na Fase 1, 17/11/2026)
- Gastos individuais por vereador: a Câmara não publica por gabinete em formato que um robô possa ler (o portal da transparência proíbe robôs). Os dados abertos do TCE-RS mostram pagamentos feitos em nome do vereador (diárias e outras rubricas, seção 4.1), mas sem o que cada rubrica significa, sem os gastos com assessores e com atraso de meses no ano corrente. O indicador de gastos fica limitado a isso, e o site diz isso.
- Votações: a API traz o voto de cada vereador nas votações da legislatura atual (nenhuma simbólica na amostra). "Sem voto registrado" não é falta (seção 2.2). Votações agrupadas não dizem quais matérias eram.
- Falas: a API traz quem falou e por quanto tempo, em parte das discussões, mas não o assunto nem o texto. As atas não saíram pela API.
- Texto integral dos documentos: não achei endereço público para baixar o PDF de proposições e atas. Sem ele, o resumo por IA depende de a Câmara informar o caminho (6.1) ou de a Fase 2 achar um jeito com navegador.
- Comissões: membros e pareceres relatados sem confirmação (seção 2).
- Execução das emendas: a prefeitura publica relatório de execução e uma página de busca, mas o arquivo em CSV deu erro e a tabela não foi lida (seção 3).
- Querido Diário, Receita Federal e cadastros de sanções: não testados (seção 4 e 7).
- Ainda não testado: se a API da Câmara responde aos servidores do GitHub Actions (D14; testar na Fase 2).

## 6. Pedido de dados via SIC (Lei de Acesso à Informação)
Quando uma fonte não tiver exportação e o robô for proibido, faça um pedido formal pelo SIC pedindo os dados em formato aberto (CSV ou planilha). Modelo de pedido, a ajustar:
"Com base na Lei 12.527/2011, solicito, em formato aberto e legível por máquina (CSV ou planilha), [conjunto de dados] da Câmara Municipal de Pelotas, de [período], contendo [campos]. Solicito também informar se esses dados são publicados periodicamente e em qual endereço."
Registre cada pedido no PROGRESSO.md com data, número de protocolo e prazo de resposta.

### 6.1 Rascunhos de pedido (preparados na Fase 1)
Situação em 17/11/2026: nenhum dos dois foi enviado. O rascunho 1 (Câmara) foi descartado pelo Henrique, que preferiu antes procurar outras fontes (seção 2.3, que não achou outro caminho para os gastos por gabinete). O rascunho 2 (prefeitura) segue aguardando a decisão dele. Os pedidos saem com o e-mail do projeto (meuvereadorrs@gmail.com). O SIC da Câmara fica em https://cmpelotas.cittaweb.com.br/citta/#/sic/formulario (o ambiente de nuvem não abre esse endereço; abra pelo seu navegador). Depois de enviar, registrar no PROGRESSO.md a data, o protocolo e o prazo.

**Rascunho 1, Câmara Municipal de Pelotas (SIC ou e-mail institucional)**
"Com base na Lei 12.527/2011, solicito à Câmara Municipal de Pelotas, em formato aberto e legível por máquina (CSV, planilha ou JSON), e informação sobre:
1. A API pública de dados abertos do Portal Legislativo (endereço cmpelotas.cittatec.com.br/api/open-data-leg/public): se existe documentação e termos de uso, e se há restrição a consultas automatizadas diárias, com intervalo de 2 segundos entre pedidos.
2. Como obter, pela API ou por arquivo, o texto integral (PDF) das proposições e as atas das sessões plenárias de 2025 em diante.
3. Como obter a relação das votações de cada sessão plenária (pauta e matérias votadas) e o que significa, nos registros de votação, o valor "ausente" para vereador presente na sessão.
4. Se o registro de oradores (tempo de fala) inclui pronunciamentos de Tribuna e de Explicações Pessoais, ou só a discussão de matérias.
5. A relação de membros de cada comissão permanente, por período, com as reuniões realizadas e a frequência.
6. As despesas de cada gabinete de vereador (diárias, combustível, cópias, telefonia, passagens, assessoria e outras), por vereador, mês e categoria, de janeiro de 2025 até o mês mais recente, com fornecedor, valor e documento de comprovação; e a explicação do que significa, nos dados enviados ao TCE-RS, o pagamento em nome do próprio vereador nessas categorias.
Solicito também informar se esses dados são publicados periodicamente e em qual endereço."

**Rascunho 2, Prefeitura de Pelotas (SIC da prefeitura)**
"Com base na Lei 12.527/2011, solicito, em formato aberto e legível por máquina (CSV ou planilha), a relação das emendas impositivas municipais de 2025 (execução em 2026) e de 2026 (execução em 2027), por vereador autor, contendo: número da emenda, valor, objeto, secretaria, entidade beneficiária (nome e CNPJ), situação de execução (empenhado, liquidado, pago, impedimento técnico) com datas e valores. Informo que o arquivo emendas.csv do Portal da Transparência (transparencia.pelotas.rs.gov.br/emendas/impositivas) retornou erro 500 em 17/11/2026. Solicito também informar se essa relação é publicada periodicamente e em qual endereço."

## 7. Resultado do teste de acesso a partir do ambiente de nuvem (23/10/2026, 10/11/2026 e 17/11/2026)
Resultado de 17/11/2026, feito pela thread da Fase 1 (a rede do ambiente de nuvem responde 403 quando o domínio não está liberado; o navegador do computador do Henrique não tem essa restrição).
- Acessam: cmpelotas.cittatec.com.br (sem robots.txt: o endereço devolve a página do sistema), www.pelotas.rs.leg.br (robots.txt permite tudo, menos /viewer/), sapl.pelotas.rs.leg.br, www.pelotas.com.br (robots.txt permite tudo), dadosabertos.tse.jus.br e cdn.tse.jus.br, leisnaweb.com.br (robots.txt bloqueia só pastas técnicas), ahoradosul.com.br, pelotasagora.com.br, portal.tce.rs.gov.br (agora respondeu; o robots.txt proíbe /aplicprod/).
- Bloqueado pelo robots.txt: cmp.portaltransparencia.avmb.com.br ("Disallow: /"), portal.tce.rs.gov.br/aplicprod/ (LicitaCon).
- O site recusa robôs: leismunicipais.com.br, divulgacandcontas.tse.jus.br (resultado de 23/10/2026; não repetido).
- Bloqueados pela rede do ambiente (o Henrique libera em Configurações do projeto, ambiente, Network access): dados.tce.rs.gov.br, queridodiario.ok.org.br e api.queridodiario.ok.org.br, cmpelotas.cittaweb.com.br (SIC e Portal do Servidor), transparencia.pelotas.com.br e transparencia.pelotas.rs.gov.br (portal da prefeitura), storage01.pelotas.com.br (arquivos do portal da prefeitura), www.diariomunicipal.com.br, www.portaldatransparencia.gov.br, www.youtube.com, dadosabertos.rfb.gov.br, web.archive.org (os três últimos vêm do teste de 10/11/2026 e não foram repetidos). Para continuar a Fase 2 sem depender do navegador do Henrique, liberar ao menos: dados.tce.rs.gov.br, transparencia.pelotas.rs.gov.br e storage01.pelotas.com.br.
- Lidos pelo navegador do computador do Henrique (poucos pedidos, só leitura): dados.tce.rs.gov.br (com 10 s entre páginas), queridodiario.org.br (site e API, esta com erro 503), github.com (página de código do Querido Diário, sem login), transparencia.pelotas.rs.gov.br.
- GitHub Actions: ainda não testado se a API da Câmara responde aos servidores do GitHub (condição da D14 no 01; testar na Fase 2).

## 8. O que dá para mostrar no site, indicador por indicador (resumo da Fase 1, 17/11/2026)
Leitura rápida: "Sim" quer dizer que a fonte entrega o dado e o recorte da legislatura 2025-2028 (D15) está coberto. "Em parte" quer dizer que dá para mostrar uma parte e o resto aparece como "dados insuficientes", com a explicação. "Não" quer dizer que hoje o site mostraria só "dados insuficientes".

| Indicador (docs/03) | Dá para mostrar? | De onde vem | O que falta ou limita |
|---|---|---|---|
| I1 Presença em sessões plenárias | Sim | Câmara: presença por sessão (parlamentaresSessao), sem IA | Falta confirmar se a API separa falta justificada da não justificada, e quais tipos de sessão contam para a frequência |
| I2 Atuação em comissões | Em parte | Câmara: reuniões de comissão e proposições do tipo parecer | Só há 9 reuniões de comissão em 2026 e nenhuma em 2025; não achei a lista de membros. Mostrar "dados insuficientes" até a Câmara responder |
| I3 Proposições por tipo | Sim | Câmara: proposições, com tipo, autoria e coautoria | Pedidos de providências são cerca de 28 mil por ano; ficam em lista por vereador e por mês (D17) |
| I4 Resultado das proposições | Em parte | Câmara: situação e resultado da votação de cada proposição | "Aprovada" e "em tramitação" saem direto. "Virou lei" e tempo de tramitação precisam de teste (lei ordinária é outro tipo de documento; a consulta de linha do tempo não foi testada) |
| I5 Temas de atuação | Sim, depende da IA | Câmara: descrição das proposições; classificação pela IA (07) | O texto integral não saiu pela API; a descrição às vezes é curta demais ("projeto de lei"). Pedidos de providências ficam com tema por regras |
| I6 Participação nos debates | Em parte | Câmara: oradores e tempo de fala | Sai quem falou, quando e por quanto tempo, só nas discussões registradas (cerca de um terço dos números sondados). O que foi dito e o assunto não saem: "dados insuficientes" para o conteúdo. Falas de Tribuna não confirmadas |
| I7 Como votou | Sim, com avisos | Câmara: votos individuais (nenhuma votação simbólica na amostra) | "Sem voto registrado" não é falta. Votações agrupadas não dizem as matérias. Só 20% das votações tiveram divergência. Voto igual ao do líder do governo: não há líder registrado na API, então essa metade fica em "dados insuficientes". A ligação voto-proposição é pelo título e precisa de teste |
| I8 Gastos do mandato | Em parte | TCE-RS: pagamentos da Câmara por credor (dados abertos), 2025 completo | Atraso de meses (2026 vai só até fevereiro). Aparecem pagamentos em nome de cada vereador (diárias, combustível, cópias, telefonia, passagens), mas o significado das rubricas e o nome do credor precisam de confirmação. Gastos com assessores e materiais do gabinete não saem por vereador: "dados insuficientes". Rascunho de SIC na 6.1 |
| I9 Emendas destinadas | Em parte | Câmara: emendas impositivas como proposição (456 em 2025). Prefeitura: relatório de execução | Destino e autor saem do texto da emenda; o valor nem sempre está no texto. A execução (empenhado, pago) não foi lida: "dados insuficientes" até confirmar a tabela e o CSV da prefeitura ou o SIC. As emendas de 2026 aparecem quase vazias na Câmara (1 registro) |
| I11 Trajetória eleitoral e financiamento | Sim | TSE: candidatura e bens de 2024 (21 eleitos), receitas de campanha | Reeleitos precisam das eleições de 2020 e 2016 (mesma estrutura, não baixadas). Doadores pessoa física: só valores agregados (06). Sem cálculo de variação de patrimônio (D16) |

Alertas do 03, seção 4:
| Alerta | Dá para fazer? | Por quê |
|---|---|---|
| A1 Gasto acima da mediana | Só em diárias | Precisa de 5 ou mais vereadores com dado na categoria; diárias têm 18 em 2025. As outras categorias não são separadas por vereador |
| A2 Mesmo fornecedor concentra a categoria | Não | Os gastos de gabinete com fornecedores não saem por vereador |
| A3 Diária no dia de sessão | Em parte | A data que a fonte traz é a do pagamento, não a da viagem. Só se o histórico do empenho trouxer o período (não lido). Revisão do 06 antes de usar |
| A4 Despesa sem comprovante | Não | O portal da Câmara que mostra o comprovante proíbe robôs |
| A5 Fornecedor em cadastro de sanções | Não agora | Cadastros federais não testados (domínio bloqueado) |
| A6 Emenda para entidade ligada a doador | Não agora | Depende de sócios (Receita Federal, não testado) e de doadores do TSE (disponível); revisão humana e jurídica |
| A7 Emenda sem execução em 12 meses | Não agora | Depende da execução publicada pela prefeitura (não lida) |

Resumo em uma frase: com o que já foi confirmado, dá para publicar a presença, as proposições, o resultado delas, os votos, o tempo de fala e a trajetória eleitoral; gastos e emendas saem pela metade; comissões, conteúdo das falas e quase todos os alertas ficam em "dados insuficientes" até haver resposta da Câmara e da prefeitura.
