# Arquitetura e roteiro de construção
Domínio: como o portal funciona e em que ordem construir | Redigido por: PromptArchitect em 23/10/2026 | Dono: Henrique | Revisar: ao fim de cada fase

Marcação: [oficial] = confirmado na documentação do Claude Code em 23/10/2026 | [a confirmar] = escolha técnica baseada em conhecimento geral, que o guia confere na fase indicada.

## 1. Como as peças se encaixam
Pense no portal como uma pequena redação automática:
- Projeto Meu Vereador no Claude Code: a conversa onde o Henrique pede o trabalho. Um coordenador transforma cada pedido em threads, que são sessões do Claude Code na nuvem trabalhando no repositório, cada uma na sua branch, entregando um pull request (uma proposta de mudança que o Henrique aprova antes de entrar no site). Instruções e memória do projeto valem para todas as threads [oficial: https://code.claude.com/docs/en/claude-projects].
- Repositório no GitHub: o arquivo central. Guarda o código, os dados coletados e os textos de apoio. Cada mudança fica registrada com data, o que também serve de histórico público de alterações. Público, porque os dados já são públicos e isso reforça a transparência.
- Coleta (scripts em Python): robôs que visitam as fontes do 02 e salvam os dados em arquivos JSON na pasta dados/. Não usam IA: buscam e organizam. Assim os números nunca dependem de a IA "lembrar" algo.
- Enriquecimento (Claude): lê os itens novos e escreve resumos simples, temas e resumos de falas, seguindo o 07. O resultado vai para dados/ia/, separado dos dados originais.
- Site estático: páginas geradas a partir dos arquivos JSON, sem banco de dados e sem servidor para manter. Proposta de ferramenta: Astro, com busca interna pelo Pagefind [a confirmar na Fase 4].
- Hospedagem: GitHub Pages, gratuita para repositório público, publica o site sempre que o repositório muda [a confirmar na Fase 6].
- Atualização diária: uma rotina criada dentro do projeto, que roda como thread num horário marcado, faz a coleta e o enriquecimento e salva no repositório; a publicação acontece sozinha em seguida [oficial para rotinas em projetos; detalhes na Fase 7].

## 2. Fatos sobre as rotinas do Claude Code que afetam o projeto [oficial, 23/10/2026]
- Disponíveis no plano Pro, em prévia de pesquisa: comportamento e limites podem mudar.
- Consomem o uso da assinatura como uma sessão normal e têm um limite diário de execuções por conta. O número exato aparece em claude.ai/code/routines; uma execução por dia cabe com folga, pelo que se sabe hoje.
- Intervalo mínimo de 1 hora entre execuções.
- O ambiente padrão só acessa uma lista de sites de programação. Os domínios das fontes precisam ser liberados em Network access, opção Custom, mantendo marcada a lista padrão de gerenciadores de pacotes.
- A rotina clona o repositório a cada execução e salva em ramos com prefixo claude/. Ela consegue salvar direto no ramo principal se o prompt mandar, desde que o ramo não seja protegido e não tenha commits de outros autores. Consequência: não misturar commits automáticos de outros robôs (como o GitHub Actions) no ramo principal; o GitHub Actions só publica, não salva dados.
- Status verde numa execução só quer dizer que a sessão rodou sem erro de infraestrutura. Abrir a execução e conferir o que foi feito.
- Documentação: https://code.claude.com/docs/en/web-scheduled-tasks

## 3. Estrutura do repositório (proposta)
- CLAUDE.md: regras permanentes para o Claude Code neste projeto (resumo do 03, 04 e 06 e onde fica cada coisa).
- PROGRESSO.md: memória do projeto. Fase atual, o que foi feito, decisões, pendências, pedidos via SIC.
- docs/: cópias dos arquivos 01 a 07 deste projeto.
- coleta/: um script por fonte, mais um comando que roda todos.
- dados/brutos/: o que foi coletado, sem alteração, com data.
- dados/tratados/: dados organizados no modelo da seção 4.
- dados/ia/: resumos e classificações, com indicação de modelo e data.
- site/: código do site.
- testes/: verificações automáticas dos dados (contagens, campos obrigatórios, links).
- logs/: registro de cada execução diária.

## 4. Modelo de dados (entidades principais)
vereador, mandato (período, partido, suplência), proposicao (tipo, número, ano, ementa, autores, situação, tramitação, links), sessao (data, tipo, pauta, ata), presenca, votacao (matéria, tipo nominal ou simbólica, resultado), voto (vereador, sentido), fala (sessão, vereador, resumo, link), comissao e participacao, despesa (gabinete, categoria, fornecedor, valor, data, documento), emenda (vereador, valor, área, beneficiário, bairro, execução), candidatura (eleição, votos, receitas, bens), pauta_declarada (tema, evidência, data, fonte), alerta (regra, fatos, documentos, revisão). Todo registro guarda fonte_url e coletado_em.

## 5. Roteiro por fases
Cada fase termina com o critério "Pronto quando". O guia não avança sem ele.

**Fase 0. Preparação (1 a 2 sessões)**
O Henrique cria o repositório público no GitHub, instala o app Claude do GitHub nele e o adiciona ao projeto; cria o ambiente de nuvem com rede Custom liberando os domínios do 02 (lista no LEIA_ANTES). Uma thread copia os arquivos 01 a 07 da Biblioteca para docs/ e cria CLAUDE.md, PROGRESSO.md e a estrutura de pastas da seção 3. Depois disso, a versão que vale é a de docs/, e os arquivos da Biblioteca podem ser removidos para não haver duas versões.
Pronto quando: o pull request da preparação foi aprovado e uma thread devolve uma tabela com o resultado de acesso a cada domínio do 02 (acessou, bloqueado pela rede do ambiente, bloqueado pelo robots.txt).

**Fase 1. Mapeamento técnico das fontes**
Começar pela API pública do Portal Legislativo (02, seção 2.1), já encontrada: confirmar cada consulta, a paginação e desde quando há dados. Depois, para cada outra fonte: como os dados saem (API, exportação, HTML, PDF), quais campos existem, desde quando, com que frequência mudam, o que o robots.txt permite. Salvar amostras pequenas em dados/brutos/amostras/. Abrir pedidos via SIC para o que não for acessível. Decidir P5 (recorte histórico).
Pronto quando: docs/02 atualizado com status confirmado de cada fonte e o Henrique sabe quais indicadores do 03 serão possíveis e quais ficam com "dados insuficientes".

**Fase 2. Coleta e dados tratados**
Um script por fonte, começando por vereadores, proposições e sessões. Dados no modelo da seção 4. Testes automáticos.
Pronto quando: um único comando gera os dados desde o início do recorte sem erro, e 3 conferências manuais (uma proposição, uma sessão, um vereador) batem com o site da Câmara.

**Fase 3. Enriquecimento por IA**
Aplicar o prompt do 07 em lote. Começar por 30 proposições variadas; o Henrique revisa todas e o guia ajusta o prompt. Só depois processar o histórico, em lotes, ao longo de vários dias, para não estourar o limite de uso da assinatura.
Pronto quando: 30 resumos revisados com no máximo 2 correções de conteúdo, e a taxonomia de temas validada.

**Fase 4. Protótipo do site**
Páginas do 04, seção 5, com dados reais, seguindo o 04. Só indicadores objetivos (I1, I3, I4, I5, I7).
Pronto quando: o site roda no computador ou na prévia do Claude Code, funciona no celular, e o Henrique consegue achar um vereador, filtrar as propostas dele por tema e abrir o texto original em menos de 1 minuto. Teste de acessibilidade automático sem erros graves.

**Fase 5. Indicadores completos e pontos de atenção**
I2, I6, I8, I9, I11, índice de atividade, depois os alertas A1 a A7 e por último a coerência (I10). Decidir P3 e P4. Revisão de todos os textos com o 06.
Pronto quando: cada indicador tem página "como calculamos" e todos os alertas que vão ao ar foram conferidos à mão.

**Fase 6. Publicação**
Decidir P1 e P2. Configurar GitHub Pages e, se quiser, domínio próprio. Páginas Sobre, Como calculamos e Correções. Primeiro, mostrar só para algumas pessoas de confiança e corrigir o que aparecer.
Pronto quando: o site está no ar, com aviso de independência, contato e registro de correções, e passou por revisão jurídica (06).

**Fase 7. Atualização diária automática**
Pedir ao coordenador que crie a rotina diária com o prompt do 07, seção 4; ela aparece na aba Rotinas do projeto e roda como thread. Atenção: uma thread de rotina que bate no limite de uso não espera, para com erro; marcar o horário para cedo da manhã, longe dos horários de uso pesado do Henrique. Plano B: o Henrique escreve no projeto "rode a atualização de hoje". Mostrar no site a data e hora da última atualização bem-sucedida.
Pronto quando: a rotina rodou 7 dias seguidos, o Henrique conferiu o registro de cada execução e o site mostra a atualização correta.

**Fase 8. Evolução**
Ideias do 01, seção 5, uma de cada vez.

## 6. Riscos conhecidos
- A API do Portal Legislativo é pública mas não documentada: a empresa pode mudar o formato sem aviso. Os testes precisam acusar mudança de formato, e o plano de contingência é ler as páginas com navegador automatizado, mais lento e frágil.
- Mudança no sistema da Câmara (troca de fornecedor de software) quebra a coleta. Os testes da pasta testes/ devem acusar isso e a rotina deve registrar o erro em logs/ e parar, sem apagar dados antigos.
- Rotinas em prévia podem mudar de regra ou limite. O plano B manual existe por isso.
- Limite de uso da assinatura Pro: o processamento do histórico inteiro por IA deve ser feito em lotes ao longo de dias.
