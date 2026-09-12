# YouTube Data Extraction & Analysis Pipeline

Pipeline automatizado em Python desenvolvido para extração, higienização e análise de dados de canais do YouTube, superando barreiras de renderização assíncrona e Web Components.

## 🛠️ Tecnologias Utilizadas
* **Linguagem**: Python 3
* **Automação Web**: Selenium WebDriver
* **Manipulação de DOM**: JavaScript Injection (Shadow DOM Traversal)
* **Engenharia de Dados**: Pandas, Regex, JSON

## 💡 Destaques Técnicos e Funcionalidades
* **Navegação Recursiva em Shadow DOM**: Injeção de script em JavaScript para atravessar recursivamente a estrutura de *ShadowRoot* do YouTube, acessando nós encapsulados que seletores CSS/XPath convencionais não alcançam.
* **Resiliência a Carregamento Assíncrono**: Validação de dados via Regex e checagens dinâmicas de texto, evitando falhas por *TimeoutException* ou leitura de avisos da interface.
* **Pipeline de Dados Desacoplado**:
  * `automacao.py`: Extração e persistência estruturada em formato JSON.
  * `analise.py`: Leitura do JSON, tratamento/normalização de strings métricas e preparação do dataset para análise via Pandas.

## 🚀 Como Executar o Projeto

1. Instale as dependências:
   ```bash
   pip install selenium pandas
