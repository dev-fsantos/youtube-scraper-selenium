YouTube Scraper + Análise de Dados

Projeto em Python que coleta dados públicos de canais do YouTube via automação de navegador (Selenium) e analisa esses dados com pandas, comparando o engajamento entre diferentes canais.

💡 Ideia do projeto

Números absolutos de inscritos podem enganar na hora de comparar canais. Um canal com 15 milhões de inscritos não é necessariamente "melhor" que um com 10 milhões — depende de como esses inscritos se traduzem em visualizações reais.

Este projeto calcula a proporção:

visualizações totais do canal / inscritos

Isso permite comparar canais de forma mais justa, olhando o histórico de visualizações relativo ao tamanho atual da audiência, em vez de só o número bruto de inscritos.

🛠️ Tecnologias utilizadas
Python 3
Selenium — automação do navegador para coletar os dados diretamente das páginas do YouTube
pandas — organização e limpeza dos dados coletados
matplotlib — visualização gráfica das comparações entre canais
📁 Estrutura do projeto
├── automacao.py       # Coleta os dados dos canais via Selenium
├── analise.py         # Limpa os dados e calcula as métricas com pandas/matplotlib
├── dados_youtube.json # Dados coletados (gerado automaticamente)
└── .gitignore
⚙️ Como funciona
1. Coleta (automacao.py)

O script pergunta quais canais você quer analisar (você digita os handles do YouTube, separados por vírgula) e, para cada canal:

Abre a aba "Sobre" do canal (youtube.com/@canal/about)
Extrai o número de inscritos e o total de visualizações do canal
Salva tudo em dados_youtube.json, como uma lista com um registro por canal

A extração é feita varrendo todo o texto visível da página (incluindo dentro de Shadow DOM, uma técnica usada pelo YouTube que esconde parte da estrutura da página de buscas simples por seletor CSS), filtrando pelos textos que contêm "inscrito" ou "visualiza".

2. Análise (analise.py)

Lê o dados_youtube.json, transforma em um DataFrame do pandas, limpa os números (que vêm como texto, ex: "9,27 mi de inscritos") e calcula a métrica de engajamento (visualizações totais / inscritos) para cada canal. Os resultados também são exibidos em gráficos de barras comparando os canais.

▶️ Como rodar

Pré-requisitos:

bash
pip install selenium pandas matplotlib

Você também precisa do ChromeDriver compatível com sua versão do Chrome instalada.

Passo 1 — coletar os dados:

bash
python automacao.py

Quando solicitado, digite os handles dos canais (o que aparece depois do @ na URL do canal), separados por vírgula. Exemplo:

Digite os canais que deseja analisar, separados por vírgula: alanzoka, cellbit, akitando

Passo 2 — analisar os dados coletados:

bash
python analise.py
🚧 Limitações conhecidas
O YouTube muda a estrutura de suas páginas com frequência, o que pode exigir ajustes pontuais na coleta ao longo do tempo
Handles de canal inválidos ou digitados incorretamente fazem aquele canal específico ser pulado na coleta (sem travar o restante do processo)
🗺️ Próximos passos
 Coletar múltiplos vídeos por canal, não só dados gerais, para permitir comparação de distribuições
 Expandir a lista de métricas analisadas
 Refinar a limpeza de números para lidar com mais formatos de texto
