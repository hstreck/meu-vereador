# Metodologia dos indicadores, níveis e alertas
Domínio: cálculo e exibição de indicadores sobre vereadores | Redigido por: PromptArchitect em 23/10/2026 | Dono: Henrique | Status: proposta inicial, revisada em 17/11/2026 (decisões D12, D13 e D17 no 01); limiares precisam ser calibrados com dados reais na Fase 5 e revisados conforme o 06

## 1. Princípios (valem para todos os indicadores)
1. Indicador mede atividade registrada, não caráter. Nenhum indicador diz se o vereador é bom, honesto ou competente.
2. Cálculo aberto: cada barra ou nível tem um link "como calculamos" com a fórmula, as fontes, o período e o que o indicador não mede.
3. Sem nota geral única e sem ranking de "melhores e piores" na página inicial. Uma nota única esconde escolhas de peso e convida à leitura de julgamento moral. Cada indicador aparece separado. A única composição prevista, o índice de atividade (seção 3), está fora da primeira versão.
4. Comparação com a Câmara, não com uma régua inventada: mostrar o valor do vereador ao lado da mediana dos vereadores no mesmo período. A mediana é o valor do meio quando todos são postos em ordem; ela não é puxada por um caso extremo, como a média seria.
5. Normalizar pelo tempo de mandato: suplentes e quem assumiu no meio do período são comparados por mês de exercício.
6. Papéis diferentes: o presidente da Câmara vota só em situações específicas e costuma propor menos; líderes de bancada falam mais. Mostrar o papel ao lado dos indicadores e não penalizar o presidente nos itens que o cargo afeta.
7. Dados insuficientes: se o indicador depende de dados que não existem ou são poucos, o site mostra "dados insuficientes" e explica o que falta. Nunca mostrar zero onde o certo é "sem dado".
8. Todo número tem link para o documento de origem e a data de coleta.

## 2. Indicadores
Para cada um: pergunta que responde, cálculo, fonte, o que não mede.

**I1 Presença em sessões plenárias**
Pergunta: em quantas sessões ele estava presente? Cálculo: presenças registradas dividido pelas sessões do período em que estava em exercício; faltas justificadas aparecem separadas das não justificadas, se a fonte distinguir. Fonte: registro de presença por sessão da API do Portal Legislativo (02, seção 2.1), sem IA; as atas servem só de conferência. Mostrar o valor real (por exemplo, "presente em 92 de 100 sessões") ao lado da mediana. Não mede: participação no debate nem permanência até o fim da sessão.

**I2 Atuação em comissões**
Pergunta: de quais comissões participa e quanto trabalha nelas? Cálculo: comissões das quais é membro, presença nas reuniões, pareceres relatados. Fonte: portal legislativo, comissões. Não mede: qualidade dos pareceres.

**I3 Proposições por tipo**
Pergunta: o que ele apresenta? Cálculo: contagem por tipo, sempre separada: projetos de lei e de resolução; emendas a projetos; pedidos de informações e requerimentos de fiscalização; pedidos de providências (pedidos ao Executivo, como retirar entulho ou consertar uma rua; em outras Câmaras se chamam indicações); moções; homenagens e denominações (títulos, nomes de rua, datas comemorativas). Fonte: proposições. Não mede: relevância. Atenção: em Pelotas os pedidos de providências são de longe o tipo mais numeroso (em 23/10/2026 a numeração de 2026 já passava de 17.500, contra menos de 1.000 pedidos de informações). Somar tudo num total único transformaria quem faz mais pedidos de buraco em "mais produtivo". Nunca exibir só o total. Os nomes exatos dos tipos vêm da API (02, seção 2.1) e devem ser mapeados para estes grupos na Fase 2; a API também devolve INDICAÇÃO, EMENDA, PARECER e MEMORANDO, que precisam de grupo ou de exclusão justificada.
Autoria conjunta: uma proposição com mais de um autor conta inteira para cada autor e aparece marcada como "em conjunto com"; nunca é dividida em frações. Proposições de autoria da Mesa, de comissão ou do Executivo não contam para vereador individual.

**I4 Resultado das proposições**
Pergunta: o que aconteceu com o que ele propôs? Cálculo: por tipo, quantas foram aprovadas, viraram lei, estão em tramitação, foram arquivadas ou retiradas; tempo médio de tramitação. Fonte: proposições e legislação. Não mede: efeito da lei na vida real.

**I5 Temas de atuação**
Pergunta: com quais assuntos ele mais trabalha? Cálculo: distribuição das proposições, falas e votos nominais pelos temas da taxonomia (07), com a contagem de cada um. Fonte: classificação por IA revisada (07). Não mede: profundidade no tema.

**I6 Participação nos debates**
Pergunta: ele fala nas sessões, e sobre o quê? Cálculo: número de pronunciamentos registrados em ata por sessão e temas das falas, com resumo neutro de cada fala e link para a ata. Fonte, por ordem de preferência: lista de oradores e tempo de fala da API, se a Câmara preencher (a confirmar na Fase 1); atas. Quem falou e por quanto tempo nunca vem da IA quando a API tiver o dado. Resumos de fala seguem as travas do 07, seção 3. Não mede: qualidade do argumento. Depende do detalhe das atas (02, seção 5).

**I7 Como votou**
Pergunta: como ele votou em cada votação nominal? Cálculo: lista de votos nominais com o tema, o resultado e o voto dele; percentual de votos iguais à maioria da Câmara e iguais ao voto do líder do governo (quando houver líder registrado). Fonte: atas e registros de votação. Não mede: votações simbólicas, que não registram o voto individual; o site diz isso na página.

**I8 Gastos do mandato**
Pergunta: quanto e em que o gabinete gasta? Cálculo: soma por categoria e por mês (diárias, viagens, combustível, telefone, material, pessoal do gabinete, conforme o que a Câmara publicar), ao lado da mediana dos vereadores. Fonte: portal da transparência da Câmara ou pedido via SIC. Não mede: necessidade do gasto. Se a Câmara não publicar por vereador, o indicador mostra "dados insuficientes".

**I9 Emendas destinadas**
Pergunta: para onde ele mandou dinheiro do orçamento? Cálculo: valor por área, por beneficiário e por bairro, e situação de execução (empenhada, paga, não executada). Fonte: prefeitura (02, seção 3). Não mede: resultado da obra ou serviço. Atenção: emenda não é gasto do gabinete; mostrar em seção própria, com explicação do que é emenda impositiva.

**I10 Coerência entre pautas declaradas e atuação**
Fora do roteiro (01, D13): registrado como ideia para depois. A seção 5 fica guardada como ponto de partida, sem fase marcada.

**I11 Trajetória eleitoral e financiamento de campanha**
Pergunta: de onde veio o dinheiro da campanha e que patrimônio ele declarou em cada eleição? Cálculo: receitas por origem (partido, pessoa física, recursos próprios), maiores doadores em valor agregado, total de bens declarados em cada eleição, com link. O site não calcula nem exibe variação de patrimônio entre eleições: o valor é autodeclarado, não é atualizado a preço de mercado, e uma conta de diferença sugere algo que o dado não sustenta. Fonte: TSE. Sem nota; é informação de contexto. Não mede: origem lícita ou ilícita.

## 3. Índice de atividade parlamentar (fora da primeira versão)
Situação (01, D12): o índice não é calculado nem exibido na primeira versão. Volta à discussão na Fase 5, com pelo menos 12 meses de dados (pendência P3).
Por que saiu:
- Percentil é a posição de cada um na fila dos 21 vereadores, e fila sempre tem último lugar. Se todos tiverem entre 95% e 100% de presença, quem tem 95% apareceria "abaixo da faixa típica", o que é falso como descrição.
- Os pesos são opinião sobre o que importa, mesmo publicados.
- Um número único por vereador vira ranking no primeiro print que circular, o que o princípio 3 quer evitar.
Condições para voltar: usar valores reais em vez de percentil; só mostrar faixa quando a diferença para a mediana for grande em termos absolutos (limiar a definir com dados); testar o resultado com os dados de um ano antes de publicar; aprovação do Henrique.
A proposta original fica registrada abaixo, só como referência.

Pergunta: quanto ele participa das atividades registradas da Câmara, comparado aos colegas?
Proposta de pesos, a validar pelo Henrique (P3) antes de publicar:
- Presença em plenário (I1): 30%
- Atuação em comissões (I2): 15%
- Proposições ponderadas (I3): 30%, com estes pesos internos por tipo: projetos de lei e resolução 5; emendas 3; pedidos de informações e requerimentos de fiscalização 3; pedidos de providências 0,2 (peso baixo por causa do volume; calibrar com os dados reais); moções 1; homenagens e denominações 0,5
- Participação nos debates (I6): 15%
- Votos nominais registrados, sem contar o sentido do voto: 10%
Cada componente vira percentil entre os vereadores do mesmo período (0 a 100) antes de aplicar os pesos. Exibir como barra com marca da mediana e em três faixas descritas em palavras: "abaixo da faixa típica", "na faixa típica", "acima da faixa típica". O nome é "índice de atividade", nunca "nota de desempenho".
Alerta de falha: pesos mudam o resultado. Publicar os pesos, a data em que foram definidos e qualquer mudança no registro de correções.

## 4. Pontos de atenção (alertas objetivos)
Substituem o antigo "grau de sintomas de práticas ilícitas" (decisão D3 no 01). Um ponto de atenção descreve um fato verificável que um cidadão pode querer perguntar ao vereador. Não é acusação.

Regras para todos os alertas:
- Cada alerta tem regra escrita, limiar, documentos de origem com link e data.
- Texto no modelo: "[fato com números]. Este dado, sozinho, não permite concluir nada sobre a conduta do vereador. Veja os documentos: [links]. [Espaço para manifestação do vereador, se houver.]" (A frase anterior usava "irregularidade", que esbarra na lista de palavras proibidas abaixo.)
- Palavras proibidas em qualquer texto do site sobre um vereador: suspeito, suspeita, irregular, ilícito, ilegal, desvio, corrupção, fraude, escândalo, farra, abusivo, exagerado, exacerbado, estranho, sintoma. Usar: "acima da mediana", "concentrado em", "coincide com", "ponto de atenção".
- Cor neutra (marinho ou cinza), sem vermelho; vermelho comunica culpa.
- Alertas marcados "revisão humana" só vão ao ar depois que o Henrique conferir os documentos.

Regras iniciais (limiares são propostas; calibrar com 12 meses de dados):
| ID | Regra | Limiar inicial | Revisão humana |
|---|---|---|---|
| A1 | Gasto do gabinete numa categoria acima da mediana dos vereadores no mesmo período | 2 vezes a mediana, com pelo menos 5 vereadores com dado na categoria | Não |
| A2 | Mesmo fornecedor concentra o valor de uma categoria do gabinete | 60% ou mais do valor da categoria em 12 meses, e valor acima de R$ 5.000 | Não |
| A3 | Diária ou viagem cujo período inclui data de sessão plenária | Qualquer ocorrência; mostrar a presença registrada nessa sessão | Não |
| A4 | Despesa sem documento de comprovação acessível no portal | Qualquer ocorrência | Não |
| A5 | Fornecedor do gabinete ou entidade beneficiária de emenda consta em cadastro de sanções (CEIS ou CNEP) | Sanção vigente na data do pagamento | Sim |
| A6 | Entidade beneficiária de emenda tem dirigente ou sócio que aparece como doador da campanha do mesmo vereador | Qualquer coincidência confirmada por CPF ou CNPJ | Sim, e só publicar após revisão jurídica (06) |
| A7 | Emenda destinada e não executada | Mais de 12 meses sem empenho | Não |
Fora de escopo: qualquer regra que dependa de adivinhar intenção, ou de notícias não confirmadas por documento.

## 5. Coerência entre pautas declaradas e atuação (ideia para depois, fora do roteiro)
Situação (01, D13): nada desta seção é construído nem exibido. O texto abaixo fica como ponto de partida, caso o Henrique decida retomar.
1. Pautas declaradas: lista de temas que o vereador disse defender, cada um com evidência (link, data, onde disse: campanha, entrevista, rede social, discurso). Curadoria humana; a IA só sugere.
2. Atuação: proposições, falas e votos nominais classificados nos mesmos temas (taxonomia do 07).
3. Exibição: duas colunas, "Disse que defenderia" e "O que fez no tema", com contagens e exemplos com link. Percentual descritivo: quanto da atuação dele cai nos temas que declarou.
4. Contradição: só registrar quando um voto nominal ou proposição for contrário a uma pauta declarada de forma explícita, com os dois links lado a lado e sem adjetivo.
5. Cobertura: com menos de 3 evidências independentes de pautas declaradas, ou com evidências todas de uma única fonte, o site mostra "cobertura insuficiente para avaliar coerência" e explica por quê. Isso evita punir quem a imprensa cobre menos.

## 6. Exibição de dados gerados por IA
Resumos, temas e resumos de falas levam o selo "resumo automático, confira o original" com link. Erros reportados por cidadãos entram no registro de correções.
