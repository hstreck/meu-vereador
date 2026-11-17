# Fontes de dados públicas sobre os vereadores de Pelotas
Domínio: coleta de dados | Mapeado por: PromptArchitect em 23/10/2026 (versão 2, com a API do Portal Legislativo e a imprensa local) | Dono: Henrique | Atualizado em 17/11/2026 com o teste de acesso de 23/10/2026 e a conferência da API de 10/11/2026 | Revisar: na Fase 1 (confirmação técnica) e depois a cada 3 meses, ou quando uma coleta falhar

Legenda de status:
- [link conferido] o endereço existe e foi encontrado em 23/10/2026; o conteúdo e o formato ainda não foram testados.
- [bloqueado para robôs] a ferramenta de leitura usada no mapeamento foi recusada pelo robots.txt do site em 23/10/2026.
- [a verificar] fonte conhecida por conhecimento geral, endereço não conferido nesta data.
- [API confirmada] dados lidos com sucesso por uma API pública em 23/10/2026.

## 1. Regras de acesso (valem para toda coleta)
- Antes de coletar, leia o robots.txt e os termos de uso do site. Se o robô for proibido, não force: use exportação oficial (CSV, planilha) se houver, ou peça os dados pelo SIC (seção 6).
- Intervalo mínimo de 2 segundos entre pedidos ao mesmo site, ou o que o robots.txt do site pedir, se for maior: SAPL antigo 60 segundos, dados abertos do TSE 10 segundos. Coleta fora do horário de sessão.
- Identificação do robô: nome do projeto, endereço do repositório e o e-mail exclusivo do projeto (01, D18). Nunca o e-mail pessoal do Henrique. Enquanto o e-mail do projeto não existir, usar nome e endereço do repositório.
- Dados pessoais: nunca pedir nem salvar CPF, e-mail pessoal, telefone ou data de nascimento, mesmo que a fonte entregue (seção 2.1 e 06, seção 3).
- Prefira, nesta ordem: API ou exportação oficial, página HTML, PDF. PDF escaneado precisa de OCR e conferência manual.
- Guarde o documento original (ou o link permanente e a data) de tudo que for coletado. O site sempre aponta para a fonte.
- O ambiente de nuvem do Claude Code bloqueia sites fora de uma lista de permissão. Cada domínio desta lista precisa ser liberado nas configurações de rede do ambiente (ver 05, Fase 0).

## 2. Câmara Municipal de Pelotas
| Fonte | Endereço | O que traz | Status | Observação |
|---|---|---|---|---|
| Site institucional | https://www.pelotas.rs.leg.br/ | Notícias, agenda, páginas institucionais | [link conferido] | Não bloqueia leitura automática: foi lido normalmente em 23/10/2026 e não tem robots.txt com proibições. Os dados estruturados (proposições, sessões, votações) não ficam nele, e sim no Portal Legislativo abaixo |
| Agenda legislativa | https://pelotas.rs.leg.br/agendas | Pautas e eventos | [link conferido] | |
| Portal Legislativo (Città, sistema EPROCLEG) | https://cmpelotas.cittatec.com.br/portal-legislativo/ | Sistema principal do processo legislativo | [API confirmada] | A página é montada por JavaScript, mas é alimentada por uma API pública de dados abertos. Detalhes na seção 2.1. Fonte número 1 do projeto |
| Vereadores | https://cmpelotas.cittatec.com.br/portal-legislativo/vereadores | Perfis, partido, legislatura | [link conferido] | Provavelmente pela mesma API (consulta parlamentaresSessao e autores das proposições) |
| Proposições | https://cmpelotas.cittatec.com.br/portal-legislativo/proposicoes/consulta | Projetos, pedidos de providências, pedidos de informações, requerimentos, moções, autoria, situação, tramitação | [API confirmada] | Atualizada em tempo real: em 23/10/2026 a API já trazia proposições protocoladas na mesma manhã |
| Sessões plenárias | https://cmpelotas.cittatec.com.br/portal-legislativo/sessoes/plenarias | Pautas, atas, votações, presenças | [link conferido] | A API tem consultas de sessões, votação e parlamentares por sessão; confirmar na Fase 1 se trazem voto nominal e presença |
| Mesa Diretora | https://cmpelotas.cittatec.com.br/portal-legislativo/mesa | Composição da Mesa | [link conferido] | Presidente tem papel diferente nos indicadores (ver 03) |
| Comissões | https://cmpelotas.cittatec.com.br/portal-legislativo/comissoes/ | Membros, reuniões, pareceres | [link conferido] | |
| Portal da Transparência (AVMB) | https://cmp.portaltransparencia.avmb.com.br/ | Provavelmente despesas, folha, diárias, contratos | [bloqueado para robôs] | Confirmado em 23/10/2026: o robots.txt diz "Disallow: /" para todos. Não coletar por robô. Procurar botão de exportação pelo navegador; se não houver, pedir via SIC (seção 6). Antes disso, verificar os dados abertos do TCE-RS (seção 4) |
| Compras e licitações | https://www.pelotas.rs.leg.br/publicacoes-oficiais-subcategoria/transparencia/29b36a16b61442e392b6286c7c748f7f | Publicações de licitações | [link conferido] | |
| Publicações diversas | https://www.pelotas.rs.leg.br/publicacoes-oficiais-subcategoria/transparencia/5ee0fc765e1b48bb5ee35f0e13e39b86 | Atos e publicações | [link conferido] | |
| LicitaCon (TCE-RS), órgão Câmara | https://portal.tce.rs.gov.br/aplicprod/f?p=50500:4:::NO::F50500_CD_ORGAO,:54401,&cs=1v6RUv69tJi1anZXFMmlm9IhNBKc | Licitações e contratos da Câmara informados ao Tribunal de Contas | [link conferido] | Verificar se o TCE-RS oferece download em dados abertos |
| Legislação da Câmara (Leis na Web) | https://leisnaweb.com.br/pesquisa-de-atos/?host=pelotas | Leis e atos | [link conferido] | Serve para saber quais proposições viraram lei |
| SAPL antigo | https://sapl.pelotas.rs.leg.br/ | Normas e matérias de anos anteriores (há PDFs de 2013 e 2014) | [link conferido] | Abriu em 23/10/2026, inclusive /api/. O robots.txt pede 60 segundos entre pedidos e bloqueia só PDFs de documentos acessórios. Fonte do histórico anterior a 2025, que fica para depois (01, D15) |
| Lei Orgânica e Regimento Interno | https://pelotas.rs.leg.br/pagina/lei-organica-de-pelotas e https://pelotas.rs.leg.br/pagina/regimento-interno | Regras de funcionamento | [link conferido] | Usar para o glossário e para entender tipos de proposição e votação |
| Transmissões (Rede Câmara) | https://www.youtube.com/@redecamarapel | Vídeos das sessões | [link conferido] | Transcrever vídeo é caro e o YouTube costuma bloquear servidores de nuvem. Prefira as atas; vídeo só como link de referência |
| SIC e Ouvidoria | https://cmpelotas.cittaweb.com.br/citta/#/sic/formulario | Pedido formal de dados | [link conferido] | Ver seção 6 |
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
- Pendente para a Fase 1: confirmar voto individual e oradores; confirmar o formato das demais consultas; avisar a Câmara sobre a exposição de CPF (01, P6).

## 3. Prefeitura de Pelotas
| Fonte | Endereço | O que traz | Status | Observação |
|---|---|---|---|---|
| Manual de emendas impositivas | https://www.pelotas.com.br/transparencia/manual_emendas | Regras das emendas individuais dos vereadores | [link conferido] | Em 2025, valor por vereador de R$ 1.335.559,76; metade obrigatoriamente para saúde; limite de 2% da receita corrente líquida |
| Lista de emendas por vereador | Não localizada | Destino, valor, beneficiário, execução | [a verificar] | Procurar no portal da transparência da prefeitura e na Lei Orçamentária Anual; se não houver em formato aberto, pedir via SIC da prefeitura. É a melhor fonte para "para onde o vereador mandou dinheiro público" |
| Legislação municipal | https://leismunicipais.com.br/prefeitura/rs/pelotas | Leis sancionadas | [bloqueado para robôs] | Em 23/10/2026 o site respondeu com verificação anti-robô. Usar o Leis na Web (seção 2) no lugar |
| Portal da transparência da prefeitura | https://www.pelotas.com.br/transparencia | Execução orçamentária, convênios | [a verificar] | Cruzar execução das emendas |

## 4. Fontes externas
| Fonte | Endereço | O que traz | Status | Observação |
|---|---|---|---|---|
| TSE, DivulgaCandContas | https://divulgacandcontas.tse.jus.br | Candidatura, bens declarados, receitas e despesas de campanha | [bloqueado para robôs] | Em 23/10/2026 o site recusou o acesso automático. Usar o Portal de Dados Abertos abaixo |
| TCE-RS, dados abertos | https://dados.tce.rs.gov.br | Possivelmente empenhos e pagamentos da Câmara por credor, licitações e contratos | [a verificar] | Hipótese a testar na Fase 1: se trouxer despesas por credor, contorna o Portal da Transparência da Câmara, que proíbe robôs. Domínio bloqueado pela rede do ambiente em 10/11/2026; precisa ser liberado |
| Querido Diário (Open Knowledge Brasil) | https://queridodiario.ok.org.br | Diários oficiais de municípios, com busca e API | [a verificar] | Verificar se cobre Pelotas. Serviria para atos como diárias e nomeações |
| TSE, Portal de Dados Abertos | https://dadosabertos.tse.jus.br | Os mesmos dados em arquivos para download, por eleição | [link conferido] | Abriu em 23/10/2026. O robots.txt pede 10 segundos entre pedidos e bloqueia /api/ e buscas: só download de arquivos |
| Receita Federal, CNPJ em dados abertos | [a verificar] | Sócios de empresas | [a verificar] | Só na fase avançada, para cruzar fornecedores e beneficiários; alerta derivado exige revisão humana (03) |
| Cadastros de sanções CEIS e CNEP (Portal da Transparência federal) | [a verificar] | Empresas punidas | [a verificar] | Cruzar com fornecedores e entidades beneficiárias |
| A Hora do Sul | https://ahoradosul.com.br/ | Notícias de Pelotas e região, política local | [link conferido] | Jornal do Grupo A Hora, que abriu operação em Pelotas em junho de 2024, depois do fim do Diário Popular (12/06/2024). O mesmo grupo comprou a Rádio Pelotense em 2025. Principal candidato a fonte de imprensa |
| Pelotas Agora | https://pelotasagora.com.br/ | Notícias locais | [link conferido] | Avaliar na Fase 5 |
| Outros portais locais | Levantar na Fase 5 com o Henrique (P4) | Falas públicas, pautas declaradas, contexto | [a verificar] | Critério de entrada: veículo identificado, com expediente e data nas matérias. Para cada um, verificar se tem RSS ou mapa do site, que permitem coleta leve; ler robots.txt e termos. Guardar só título, data, link e um resumo próprio, nunca o texto da matéria (direito autoral) |
| Perfis públicos dos vereadores em redes sociais | Instagram, Facebook, X, TikTok dos vereadores | Pautas declaradas, falas públicas | [a verificar] | Não automatizar: as redes exigem login, bloqueiam robôs e os termos de uso proíbem coleta automática. Curadoria manual: o Henrique registra a postagem relevante (link, data, tema, frase curta) num formulário ou planilha do projeto, que alimenta as "pautas declaradas" do 03. Sites próprios dos vereadores, se houver, podem ser coletados normalmente |
| Referência de método | Operação Serenata de Amor (projeto cívico que analisou reembolsos de deputados federais com robô) | Inspiração para alertas objetivos | [a verificar] | Estudar como ela descrevia suspeitas sem acusar, antes da Fase 5 |

## 5. Lacunas conhecidas
- Gastos individuais por vereador: não se sabe ainda se a Câmara publica despesas por gabinete (diárias, combustível, telefone, assessores). Se publicar só o total da Câmara, o indicador de gastos individuais fica limitado ao que existir, e o site diz isso.
- Votações: votação simbólica não registra o voto de cada vereador. Só votações nominais entram em "como votou".
- Falas: dependem do nível de detalhe das atas. Se as atas forem resumidas, as falas ficam limitadas.

## 6. Pedido de dados via SIC (Lei de Acesso à Informação)
Quando uma fonte não tiver exportação e o robô for proibido, faça um pedido formal pelo SIC pedindo os dados em formato aberto (CSV ou planilha). Modelo de pedido, a ajustar:
"Com base na Lei 12.527/2011, solicito, em formato aberto e legível por máquina (CSV ou planilha), [conjunto de dados] da Câmara Municipal de Pelotas, de [período], contendo [campos]. Solicito também informar se esses dados são publicados periodicamente e em qual endereço."
Registre cada pedido no PROGRESSO.md com data, número de protocolo e prazo de resposta.

## 7. Resultado do teste de acesso a partir do ambiente de nuvem (23/10/2026 e 10/11/2026)
- Acessam: www.pelotas.rs.leg.br (instável na primeira tentativa; sem robots.txt), cmpelotas.cittatec.com.br (sem robots.txt), sapl.pelotas.rs.leg.br, www.pelotas.com.br, leisnaweb.com.br, dadosabertos.tse.jus.br, ahoradosul.com.br, pelotasagora.com.br.
- Bloqueado pelo robots.txt: cmp.portaltransparencia.avmb.com.br.
- O site recusa robôs: leismunicipais.com.br, divulgacandcontas.tse.jus.br.
- Bloqueados pela rede do ambiente (o Henrique libera em Configurações do projeto, ambiente, Network access): www.youtube.com, cmpelotas.cittaweb.com.br, portaldatransparencia.gov.br, dadosabertos.rfb.gov.br, web.archive.org, dados.tce.rs.gov.br.
- Inconclusivo: portal.tce.rs.gov.br (a conexão cai).
- Ainda não testado: se a API da Câmara responde aos servidores do GitHub Actions (condição da D14 no 01; testar na Fase 2).
