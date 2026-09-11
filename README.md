# YouTube Web Scraper com Selenium

Automação em Python desenvolvida para raspagem de dados e comentários de vídeos do YouTube usando Selenium WebDriver.

Algumas funcionalidades: 
Navegação Dinâmica: Realiza pesquisas no YouTube e acessa vídeos utilizando seletores CSS/ID precisos, dispensando coordenadas de tela.

Coleta de Metadados: Extrai automaticamente o nome do canal, total de inscritos, título do vídeo e número de visualizações.

Raspagem de Comentários: Rola a página para acionar o carregamento dinâmico e captura os 5 principais comentários.

Tratamento de Tempo Dinâmico: Implementa WebDriverWait para aguardar a renderização correta dos elementos no navegador antes de tentar a leitura.

Tecnologias Utilizadas: Python 3, Selenium WebDriver (Módulos By, WebDriverWait, expected_conditions)
