# Identidade visual do Portal Cidadão de Pelotas
Domínio: design e interface | Redigido por: PromptArchitect em 23/10/2026 | Dono: Henrique | Revisar: depois do primeiro protótipo (Fase 4)

## 1. Direção
Um portal cívico com cara de publicação séria da cidade, não de aplicativo de tecnologia. Referência de tom: um bom relatório público ou caderno especial de jornal, organizado para o celular. Limpo, com muito espaço em branco, números grandes e legíveis, texto curto. A identidade de Pelotas entra pelas cores da bandeira e do brasão, não por enfeite.

O site é parecido com Pelotas, mas não pode parecer o site oficial da Câmara: o cidadão precisa entender em segundos que é um projeto independente. Por isso, sem brasão do município, sem logomarca da Câmara e sem copiar o layout dela. Faixa fixa no rodapé e na página "Sobre": "Projeto independente. Não é um site oficial da Câmara Municipal de Pelotas."

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
Proposta, a testar no protótipo: Public Sans para texto e interface (fonte criada para sites de governo, muito legível, disponível no Google Fonts) e uma serifada de leitura, como Source Serif 4, para títulos de página e números de destaque. Números em tabelas com algarismos tabulares, para alinhar.
Tamanho base de texto 18 px no celular; linhas de até 70 caracteres.

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
- Página do vereador: cabeçalho com foto, partido, mandato, comissões e papel; abas "Resumo", "Propostas", "Votos", "Falas", "Gastos", "Emendas", "Trajetória", "Pontos de atenção". Linha do tempo filtrável.
- Propostas: lista com filtros em linguagem simples: "Sobre o quê?" (tema), "De quem?" (vereador), "Que tipo?" (tipo), "Em que situação?" (tramitando, aprovada, virou lei, arquivada), "Quando?" (período). Cada item com resumo, situação e links para o texto integral e a página da Câmara.
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
