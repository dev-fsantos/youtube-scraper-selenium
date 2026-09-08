from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

navegador = webdriver.Chrome()

navegador.maximize_window()

entrayt = navegador.get("https://youtube.com.br")

time.sleep(5)

pesquisar = navegador.find_element("name", "search_query")

pesquisar.send_keys("Alanzoka", Keys.ENTER)
time.sleep(2)

navegador.execute_script("window.scrollBy(0, 500)")

primeiro_video = WebDriverWait(navegador, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "ytd-video-renderer a#video-title"))
)

primeiro_video.click()
time.sleep(2)

def coleta_dados():
    nome_canal = navegador.find_element("css selector", "#channel-name").text
    titulo_video = navegador.find_element(By.CSS_SELECTOR, "h1.ytd-watch-metadata").text
    num_inscritos = navegador.find_element(By.ID, "owner-sub-count").text
    visualizacoes = WebDriverWait(navegador, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#info span, #info-text span"))
    ).text

    navegador.execute_script("window.scrollBy(0, 500)")
    time.sleep(2)

    comentarios = navegador.find_elements(By.CSS_SELECTOR, "#content-text")

    return {
    "canal": nome_canal,
    "inscritos": num_inscritos,
    "video": titulo_video,
    "visualizacoes": visualizacoes,
    "comentarios": [comentario.text for comentario in comentarios[:5]]
}

dados = coleta_dados()

print("Nome do canal:", dados["canal"], "Nº de inscritos:", dados["inscritos"], "Título do vídeo:", dados["video"], "Nº de visualizações:", dados["visualizacoes"])

for comentario in dados["comentarios"]:
    print("-", comentario)
