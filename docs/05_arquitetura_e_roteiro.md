# Arquitetura e roteiro de construção
Domínio: como o portal funciona e em que ordem construir | Redigido por: PromptArchitect em 23/10/2026 | Revisado em 17/11/2026 (decisões D14 a D18 no 01) | Dono: Henrique | Revisar: ao fim de cada fase

Marcação: [oficial] = confirmado na documentação do Claude Code (seção 2 conferida de novo em 10/11/2026; o resto em 23/10/2026) | [a confirmar] = escolha técnica baseada em conhecimento geral, que o guia confere na fase indicada.

## 1. Como as peças se encaixam
Pense no portal como uma pequena redação automática:
- Projeto Meu Vereador no Claude Code: a conversa onde o Henrique pede o trabalho. Um coordenador transforma cada pedido em threads, que são sessões do Claude Code na nuvem trabalhando no repositório, cada uma na sua branch, entregando um pull request (uma proposta de mudança que o Henrique aprova antes de entrar no site). Instruções e memória do projeto valem para todas as threads [oficial: https://code.claude.com/docs/en/claude-projects].
- Repositório no GitHub: o arquivo central. Guarda o código, os dados coletados e os textos de apoio. Cada mudança fica registrada com data, o que também serve de histórico público de alterações. Público, porque os dados já são públicos e isso reforça a transparência.
- Coleta (scripts em Python): robôs que visitam as fontes do 02 e salvam os dados em arquivos JSON na pasta dados/. Não usam IA: buscam e organizam. Assim os números nunca dependem de a IA "lembrar" algo. Cada consulta pede só os campos de uma lista permitida (02, seção 2.1), porque a API devolve dados pessoais que não podem ir para um repositório público.
- Enriquecimento (Claude): lê os itens novos que precisam de IA e escreve resumos simples, temas e resumos de falas, seguindo o 07. Pedidos de providências não passam por IA: o tema sai de regras (07, seção 1.1). O resultado vai para dados/ia/, separado dos dados originais, e só é publicado depois de passar pela validação mecânica do 07.
- Site estático: páginas geradas a partir dos arquivos JSON, sem banco de dados e sem servidor para manter. Proposta de ferramenta: Astro, com busca interna pelo Pagefind [a confirmar na Fase 4]. Página própria só para projetos, pedidos de informações, moções e requerimentos; pedidos de providências ficam em listas por vereador e por mês. Motivo: são cerca de 20 mil por ano, e uma página para cada um esbarra nos limites da hospedagem (site de até 1 GB e publicação que expira em 10 minutos no GitHub Pages).
- Hospedagem: GitHub Pages, gratuita para repositório público, publica o site sempre que o repositório muda [a confirmar na Fase 6].
- Atualização diária, em duas peças separadas (01, D14):
  - GitHub Actions (o robô gratuito do GitHub para repositórios públicos, que roda scripts em horário marcado): todo dia roda a coleta, os testes e, se os testes passarem, salva os dados e publica o site. Não usa IA nem o limite de uso da assinatura.
  - Tarefa agendada do Claude (antes chamada rotina): roda depois, só para o enriquecimento por IA dos itens novos, e abre o resultado para o Actions publicar. Se ela falhar ou bater no limite de uso, o site atualiza do mesmo jeito com os dados do dia, e o resumo chega no dia seguinte.
  - Condição: confirmar na Fase 2 que a API da Câmara responde aos servidores do GitHub. Se não responder, a coleta volta para a tarefa agendada do Claude, que roda no ambiente de nuvem já testado.
- Testes em todo pull request: o GitHub Actions roda os testes a cada proposta de mudança e mostra verde ou vermelho antes do botão de aprovar. O Henrique não lê código; esta é a rede de segurança dele. Quando houver site (Fase 4), cada pull request ganha também uma prévia para abrir no celular [como gerar a prévia: a confirmar na Fase 4].

## 2. Fatos sobre as tarefas agendadas do Claude Code que afetam o projeto [oficial, conferido em 10/11/2026]
- As rotinas passaram a se chamar tarefas agendadas (scheduled tasks). O nome antigo ainda aparece em alguns lugares, como o endereço claude.ai/code/routines.
- Disponíveis no plano Pro, em prévia de pesquisa: comportamento e limites podem mudar.
- Consomem o uso da assinatura como uma sessão normal. O limite publicado é de 100 execuções agendadas por hora por conta; a documentação não fala em limite diário. Uma execução por dia cabe com folga.
- Intervalo mínimo de 1 hora entre execuções. Marcar o horário alguns minutos depois da hora cheia (por exemplo 6h07), porque execuções na hora cheia podem atrasar.
- O ambiente padrão só acessa uma lista de sites de programação. Os domínios das fontes precisam ser liberados em Network access, opção Custom, mantendo marcada a lista padrão de gerenciadores de pacotes.
- A tarefa clona o repositório a cada execução e salva num ramo com prefixo claude/, a menos que o prompt mande outro. Quem controla onde ela pode salvar são as regras de proteção de ramo do GitHub. A documentação atual não traz a restrição sobre "commits de outros autores" que este documento citava, e por isso o GitHub Actions pode salvar dados no ramo principal (seção 1).
- Status de sucesso numa execução só quer dizer que a sessão terminou sem erro. Abrir a execução e conferir o que foi feito.
- Limite de uso: uma execução agendada que encontra o limite da assinatura esgotado é recusada até o limite renovar. Uma thread do projeto que bate no limite espera e continua sozinha quando ele renova (padrão, pode ser desligado nas configurações do projeto).
- Se a ligação com o GitHub expirar, a tarefa pula execuções por até 72 horas e depois se desliga.
- Documentação: https://code.claude.com/docs/en/web-scheduled-tasks e https://code.claude.com/docs/en/claude-projects

## 3. Estrutura do repositório (proposta)
- CLAUDE.md: regras permanentes para o Claude Code neste projeto (resumo do 03, 04 e 06 e onde fica cada coisa).
- PROGRESSO.md: memória do projeto. Fase atual, o que foi feito, decisões, pendências, pedidos via SIC.
- docs/: cópias dos arquivos 01 a 07 deste projeto.
- coleta/: um script por fonte, mais um comando que roda todos.
- .github/workflows/: as tarefas do GitHub Actions (testes em pull request; coleta e publicação diárias).
- dados/brutos/: o que foi coletado, com data, sem alterar o conteúdo dos campos pedidos. Só entram os campos da lista permitida (02, seção 2.1): CPF, e-mail, telefone e data de nascimento nunca são pedidos nem salvos.
- dados/tratados/: dados organizados no modelo da seção 4. Proposições e sessões em um arquivo por mês e por tipo, não num arquivo único, para o histórico do repositório não inchar a cada dia.
- dados/ia/: resumos e classificações, com indicação de modelo e data.
- site/: código do site.
- testes/: verificações automáticas dos dados (contagens, campos obrigatórios, links), mais duas travas: nenhum arquivo em dados/ com sequência no formato de CPF ou telefone, e nenhuma palavra da lista proibida do 03 nos textos do site.
- logs/: registro de cada execução diária.

## 4. Modelo de dados (entidades principais)
vereador, mandato (período, partido, suplência), proposicao (tipo, número, ano, ementa, autores, situação, tramitação, links), sessao (data, tipo, pauta, ata), presenca, votacao (matéria, tipo nominal ou simbólica, resultado), voto (vereador, sentido), fala (sessão, vereador, resumo, link), comissao e participacao, despesa (gabinete, categoria, fornecedor, valor, data, documento), emenda (vereador, valor, área, beneficiário, bairro, execução), candidatura (eleição, votos, receitas, bens), pauta_declarada (tema, evidência, data, fonte), alerta (regra, fatos, documentos, revisão). Todo registro guarda fonte_url e coletado_em.

## 5. Roteiro por fases
Cada fase termina com o critério "Pronto quando". O guia não avança sem ele.

**Fase 0. Preparação (1 a 2 sessões)**
O Henrique cria o repositório público no GitHub, instala o app Claude do GitHub nele e o adiciona ao projeto; cria o ambiente de nuvem com rede Custom liberando os domínios do 02 (lista no LEIA_ANTES). O Henrique também cria o e-mail exclusivo do projeto e ativa a verificação em duas etapas na conta do GitHub (01, D18): quem invadir a conta publica em nome dele. Uma thread copia os arquivos 01 a 07 da Biblioteca para docs/ e cria CLAUDE.md, PROGRESSO.md e a estrutura de pastas da seção 3. Depois disso, a versão que vale é a de docs/, e os arquivos da Biblioteca podem ser removidos para não haver duas versões.
Pronto quando: o pull request da preparação foi aprovado e uma thread devolve uma tabela com o resultado de acesso a cada domínio do 02 (acessou, bloqueado pela rede do ambiente, bloqueado pelo robots.txt).

**Fase 1. Mapeamento técnico das fontes**
Começar pela API pública do Portal Legislativo (02, seção 2.1), já encontrada: confirmar cada consulta, a paginação e desde quando há dados. Depois, para cada outra fonte: como os dados saem (API, exportação, HTML, PDF), quais campos existem, desde quando, com que frequência mudam, o que o robots.txt permite. Salvar amostras pequenas em dados/brutos/amostras/. Primeira pergunta: a API traz o voto de cada vereador e a lista de oradores? (02, seção 2.1). Verificar as fontes novas do 02 (dados abertos do TCE-RS, Querido Diário). Abrir pedidos via SIC para o que não for acessível. O recorte é a legislatura atual (01, D15).
Pronto quando: docs/02 atualizado com status confirmado de cada fonte e o Henrique sabe quais indicadores do 03 serão possíveis e quais ficam com "dados insuficientes".

**Fase 2. Coleta e dados tratados**
Um script por fonte, começando por vereadores, proposições e sessões. Dados no modelo da seção 4, com tabela de identidade ligando nome parlamentar e nome civil. Testes automáticos, rodando no GitHub Actions em todo pull request. Assim que o primeiro script existir, ligar a coleta diária no GitHub Actions (depois do teste de acesso da D14): quando o site for ao ar, a coleta já terá meses de uso.
Pronto quando: um único comando gera os dados desde o início do recorte sem erro, 3 conferências manuais (uma proposição, uma sessão, um vereador) batem com o site da Câmara, os testes rodam sozinhos em pull request e a coleta diária rodou 7 dias seguidos sem erro.

**Fase 3. Enriquecimento por IA**
Aplicar o prompt do 07 em lote, só aos tipos que passam por IA (07, seção 1.1). Começar por 30 proposições variadas; o Henrique revisa todas e o guia ajusta o prompt. Só depois processar o histórico, em lotes, ao longo de vários dias, para não estourar o limite de uso da assinatura.
Pronto quando: 30 resumos revisados com no máximo 2 correções de conteúdo, e a taxonomia de temas validada.

**Fase 4. Protótipo do site**
Primeiro a maquete da página do vereador, aprovada pelo Henrique (04, seção 8). Depois as páginas do 04, seção 5, com dados reais, seguindo o 04. Só indicadores objetivos (I1, I3, I4, I5, I7).
Pronto quando: o site roda no computador ou na prévia do Claude Code, funciona no celular, e o Henrique consegue achar um vereador, filtrar as propostas dele por tema e abrir o texto original em menos de 1 minuto. Três moradores que não são da área conseguem fazer o mesmo (04, seção 8). Teste de acessibilidade automático sem erros graves.

**Fase 5. Indicadores completos e pontos de atenção**
I2, I6, I8, I9, I11, depois os alertas A1 a A7. Decidir a P3 (se o índice de atividade volta, 01, D12) e a P4. A coerência (I10) está fora do roteiro (01, D13). Revisão de todos os textos com o 06.
Pronto quando: cada indicador tem página "como calculamos" e todos os alertas que vão ao ar foram conferidos à mão.

**Fase 6. Publicação**
Decidir P1 e P2. Configurar GitHub Pages e, se quiser, domínio próprio. Páginas Sobre, Como calculamos e Correções. Primeiro, mostrar só para algumas pessoas de confiança e corrigir o que aparecer.
Pronto quando: o site está no ar, com aviso de independência, contato e registro de correções, e passou por revisão jurídica (06).

**Fase 7. Atualização diária automática**
A coleta e a publicação diárias já rodam no GitHub Actions desde a Fase 2. Aqui entra a peça de IA: pedir ao coordenador que crie a tarefa agendada diária com o prompt do 07, seção 4; ela aparece em Tarefas agendadas do projeto. Marcar o horário para cedo da manhã, depois da coleta e longe dos horários de uso pesado do Henrique; se o limite de uso estiver esgotado, a execução é recusada e o site segue só com os dados do dia. Plano B: o Henrique escreve no projeto "rode a atualização de hoje". Mostrar no site a data e hora da última atualização bem-sucedida dos dados e, separado, dos resumos.
Pronto quando: a tarefa rodou 7 dias seguidos, o Henrique conferiu o registro de cada execução e o site mostra a atualização correta.

**Fase 8. Evolução**
Ideias do 01, seção 5, uma de cada vez.

## 6. Riscos conhecidos
- A API do Portal Legislativo é pública mas não documentada: a empresa pode mudar o formato sem aviso. Os testes precisam acusar mudança de formato, e o plano de contingência é ler as páginas com navegador automatizado, mais lento e frágil.
- Mudança no sistema da Câmara (troca de fornecedor de software) quebra a coleta. Os testes da pasta testes/ devem acusar isso e a rotina deve registrar o erro em logs/ e parar, sem apagar dados antigos.
- Tarefas agendadas em prévia podem mudar de regra ou limite. Por isso a coleta e a publicação não dependem delas (seção 1), e o plano B manual continua valendo para os resumos.
- O GitHub Actions pode ser recusado pela API da Câmara (servidores fora do Brasil). Testar na Fase 2; se acontecer, a coleta volta para a tarefa agendada do Claude.
- Uma só pessoa aprova tudo e não lê código. Os testes automáticos em pull request e a prévia do site são a proteção; sem eles, aprovar é só confiança.
- Limite de uso da assinatura Pro: o processamento do histórico inteiro por IA deve ser feito em lotes ao longo de dias.
