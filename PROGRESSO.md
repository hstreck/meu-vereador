# Progresso do projeto

## Fase atual
Fase 1. Mapeamento técnico das fontes (docs/05, seção 5): feito, aguardando a aprovação do pull request pelo Henrique. A Fase 0 ainda tem pendências dele (ver Pendente).

## Feito
- 2026-10-23: docs 01 a 07 copiados da Biblioteca para docs/; criados CLAUDE.md, PROGRESSO.md e a estrutura de pastas.
- 2026-10-23: teste de acesso aos domínios do docs/02 a partir do ambiente de nuvem. Resultado no docs/02, seção 7.
- 2026-11-10: análise crítica do projeto e conferência da API da Câmara (presença por sessão confirmada; CPF dos vereadores exposto pela API).
- 2026-11-17: melhorias da análise aplicadas em docs/ (decisões D12 a D18 no docs/01), no CLAUDE.md e neste arquivo (pull request 2, com merge).
- 2026-11-17: e-mail do projeto criado (meuvereadorrs@gmail.com) e decidido não avisar a Câmara sobre o CPF na API (docs/01, D19 e D20).
- 2026-11-17: Fase 1. Todas as fontes do docs/02 testadas ou com o motivo de não terem sido; status confirmado nas seções 2 a 4, tabela de indicadores na seção 8 e rascunhos de pedido (SIC) na 6.1. Amostras em dados/brutos/amostras/ (sem CPF, e-mail ou telefone), script coleta/amostras_fase1.py e teste testes/test_amostras.py.
  - Resposta à primeira pergunta: a API da Câmara traz o voto de cada vereador (votações a partir de fev/2022; legislatura atual por volta do número 2.700 em diante) e a lista de oradores com tempo de fala (só em parte das discussões, sem assunto nem texto). Atenção: "ausente" no voto não é falta na sessão.
  - O TCE-RS tem dados abertos de pagamentos da Câmara por credor, com pagamentos em nome dos vereadores (2025 completo; 2026 só até fevereiro). Cobre parte do indicador de gastos, não os assessores.
  - Não confirmados: Querido Diário (API fora do ar, erro 503), ata e texto integral em PDF, membros de comissões, execução das emendas pela prefeitura (CSV deu erro 500), cadastros federais de sanções e Receita Federal (domínios bloqueados pela rede do ambiente).
  - Dois pontos de método a registrar: (1) uma única consulta a /api/ do dados.tce.rs.gov.br foi feita por engano no teste (o robots.txt desaconselha), sem repetir; (2) as fontes bloqueadas pela rede do ambiente foram lidas pelo navegador do computador do Henrique, com poucos pedidos.

## Pendente
Do Henrique:
- Ativar a verificação em duas etapas na conta do GitHub (docs/01, D18), se ainda não estiver ativa.
- Liberar na rede do ambiente: dados.tce.rs.gov.br, portal.tce.rs.gov.br, cmpelotas.cittaweb.com.br (docs/02, seção 7).
- Depois da aprovação, remover os documentos da Biblioteca, para não haver duas versões.

Do Henrique, da Fase 1:
- Decidir se envia o pedido à prefeitura (rascunho 2, docs/02, seção 6.1).
- Rede do ambiente: dados.tce.rs.gov.br, transparencia.pelotas.rs.gov.br e storage01.pelotas.com.br liberados em 17/11/2026 (conferido; o storage01 responde erro 500 do lado da prefeitura). Opcional: api.queridodiario.ok.org.br, para refazer o teste do Querido Diário.

Próxima fase (Fase 2: coleta e dados tratados), em thread nova, quando o Henrique pedir. Pontos que a Fase 2 deve resolver primeiro (docs/02, seções 2.2 e 8):
- Ligar cada votação à sessão e à proposição (pelo título) e testar; ligar oradores à sessão por data e hora.
- Tabela de identidade das pessoas (filtro AUTOR_PESSOA da API devolve as proposições pelo id da pessoa).
- Conferir o significado das rubricas do TCE-RS e o nome do credor antes de exibir gastos.
- Testar se a API da Câmara responde aos servidores do GitHub Actions (D14).

## Decisões
Ver docs/01.

## Pedidos via SIC
- Nenhum pedido enviado até 17/11/2026.
- Pedido à Câmara (rascunho 1): descartado pelo Henrique em 17/11/2026. A busca adicional (docs/02, seção 2.3) não achou outra fonte para gastos por gabinete.
- Pedido à prefeitura (rascunho 2, emendas impositivas por vereador): aguardando a decisão do Henrique de enviar ou não.
