# Identidade visual do Portal Cidadão de Pelotas
Domínio: design e interface | Redigido por: PromptArchitect em 23/10/2026 | Dono: Henrique | Revisar: depois do primeiro protótipo (Fase 4)

## 1. Direção
Um portal cívico com cara de publicação séria da cidade, não de aplicativo de tecnologia. Referência de tom: um bom relatório público ou caderno especial de jornal, organizado para o celular. Limpo, com muito espaço em branco, números grandes e legíveis, texto curto. A identidade de Pelotas entra pelas cores da bandeira e do brasão, não por enfeite.

O site é parecido com Pelotas, mas não pode parecer o site oficial da Câmara: o cidadão precisa entender em segundos que é um projeto independente. Por isso, sem brasão do município, sem logomarca da Câmara e sem copiar o layout dela. O aviso "Projeto independente. Não é um site oficial da Câmara Municipal de Pelotas." aparece no topo de todas as páginas, junto do nome do site, e também no rodapé e na página "Sobre". Só no rodapé não basta: no celular quase ninguém chega lá, e o site usa as cores da Câmara.

## 2. Cores
Base medida no print do site da Câmara enviado pelo Henrique (23/10/2026):
| Token | Cor | Origem | Uso |
|---|---|---|---|
| azul-pelotas | #105EA8 | Barra de menu e cards da Câmara | Cor principal: links, botões, barras de gráfico |
| marinho | #0A3965 | Cards escuros e títulos da Câmara | Títulos, cabeçalho, alertas neutros |
| fundo | #F5F5F5 | Fundo da página da Câmara | Fundo de seções alternadas |
| branco | #FFFFFF | Faixa central da bandeira de Pelotas | Fundo principal |

Contraste calculado (padrão WCAG, mínimo 4,5 para texto): azul-pelotas sobre branco 6,6; marinho sobre branco 11,8; marinho sobre fundo 10,8. Os dois passam para texto comum.

Acentos do brasão de Pelotas (cruz vermelha e branca, coroa e ramos de arroz dourados, louro verde) podem entrar com moderação: um fio dourado em destaques, por exemplo. Os valores exatos desses acentos ainda não foram definidos; o Claude Code deve propor e medir contraste antes de usar. Dourado sobre branco quase sempre falha em contraste: usar só como detalhe, nunca em texto.

Vermelho não é usado para alertas sobre vereadores (03, seção 4). Pontos de atenção usam marinho com ícone neutro.

Gráficos com mais de uma série: tons de azul e marinho, mais um cinza, e um terceiro tom só se necessário; nunca depender só da cor para diferenciar (usar rótulo direto).

## 3. Tipografia
Proposta, a testar no protótipo: Public Sans para texto e interface (fonte criada para sites de governo, muito legível, de licença aberta) e uma serifada de leitura, como Source Serif 4, para títulos de página e números de destaque. Números em tabelas com algarismos tabulares, para alinhar.
Tamanho base de texto 18 px no celular; linhas de até 70 caracteres.
Os arquivos das fontes ficam guardados no próprio site, não carregados do Google Fonts: é mais rápido e não avisa um terceiro de cada visita.

## 4. Padrões que dão "cara de IA" e ficam proibidos
Nomeados para o Claude Code evitar, porque proibição genérica não funciona:
- Degradês roxo e azul, fundos com brilho, efeito vidro (glassmorphism).
- Emojis como ícones; ícones decorativos em todo título.
- Grade de cards iguais com cantos muito arredondados e sombra em tudo.
- Seção de destaque com frase de efeito ("Transparência ao seu alcance", "O futuro da cidadania").
- Botões em formato de pílula com degradê.
- Animações de entrada em cada bloco ao rolar a página.
- Contadores animados de números.
- Texto genérico de marketing em qualquer lugar; todo texto descreve dado real ou explica como usar.

## 5. Estrutura de páginas (versão 1)
- Início: busca por nome do vereador ou tema, lista dos vereadores com foto e partido, "Esta semana na Câmara" (pautas e votações recentes) e data da última atualização.
- Página do vereador: cabeçalho com foto, partido, mandato, comissões e papel; uma página de resumo com atalhos para páginas próprias, cada uma com seu endereço: "Propostas", "Votos", "Falas", "Gastos", "Emendas", "Trajetória", "Pontos de atenção". Não usar abas: oito abas não cabem no celular e escondem o conteúdo de quem chega por link. Só entra no ar a página que tiver dado; as outras não aparecem no menu.
- Propostas: lista com filtros em linguagem simples: "Sobre o quê?" (tema), "De quem?" (vereador), "Que tipo?" (tipo), "Em que situação?" (tramitando, aprovada, virou lei, arquivada), "Quando?" (período). Cada item com resumo, situação e links para o texto integral e a página da Câmara. Projetos, pedidos de informações, moções e requerimentos têm página própria; pedidos de providências aparecem só em listas, por vereador e por mês (01, D17).
- Votações: cada votação nominal com o resultado e o voto de cada vereador.
- A Câmara por dentro: gastos gerais, licitações e contratos da Câmara como instituição, com resumo em linguagem simples, filtros por ano e link para o LicitaCon e o portal da transparência.
- Como funciona a Câmara: glossário e explicações curtas.
- Como calculamos: metodologia completa (03), pesos, fontes e registro de correções.
- Sobre: quem faz, contato, aviso de independência, como pedir correção.

## 6. Acessibilidade e desempenho
- Meta WCAG 2.1 nível AA: contraste, navegação por teclado, textos alternativos nas fotos e nos gráficos, foco visível.
- Todo gráfico tem a tabela de dados acessível logo abaixo.
- Conteúdo principal funciona sem JavaScript; filtros podem usar JavaScript.
- Pensado primeiro para o celular, com área de toque confortável.
- Fotos oficiais dos vereadores com crédito da fonte.

## 7. Link compartilhado
O cidadão vai chegar por um link colado no WhatsApp ou no Instagram, não pela página inicial. Por isso:
- Cada vereador, projeto e votação tem endereço próprio, curto e estável.
- Cada página tem título claro e imagem de prévia (o cartão que aparece quando o link é colado numa conversa), gerada na construção do site, com nome, foto ou número e o aviso de independência.
- Botão "copiar link" nos itens de lista.
- Quem chega por link entende onde está sem passar pela página inicial: nome do site e aviso de independência no topo.

## 8. Como o desenho é aprovado
1. Antes de programar o site, fazer uma maquete de uma única página, a do vereador, no tamanho de celular, com dados reais de dois casos opostos: um vereador com milhares de pedidos de providências e o presidente da Câmara.
2. O Henrique aprova a maquete. Só então os componentes e as outras páginas são construídos.
3. Na Fase 4, testar com três moradores que não são da área: cada um tenta achar um vereador, filtrar as propostas por tema e abrir o texto original. O que travar é corrigido antes de seguir.
