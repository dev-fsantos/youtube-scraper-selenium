from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import json
import time
import re

navegador = webdriver.Chrome()

navegador.maximize_window()

navegador.get("https://youtube.com.br")

time.sleep(5)

pesquisar = navegador.find_element("name", "search_query")

pesquisar.send_keys("Alanzoka", Keys.ENTER)
time.sleep(2)

navegador.execute_script("window.scrollBy(0, 100)")
try:
    primeiro_video = WebDriverWait(navegador, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-video-renderer #video-title"))
    )
    navegador.execute_script("arguments[0].click();", primeiro_video)
except Exception as e:
    print("Erro ao tentar abrir o vídeo:", e)
time.sleep(2)


def esperar_texto(by, valor, timeout=15):
    def condicao(navegador):
        try:
            elemento = navegador.find_element(by, valor)
            texto = elemento.text.strip()
            return elemento if texto != "" else False
        except:
            return False
    return WebDriverWait(navegador, timeout).until(condicao)


def listar_todos_aria_labels(navegador):
    script = """
    function coletarLabels(root, lista) {
        const elementos = root.querySelectorAll('*');
        for (const el of elementos) {
            const label = el.getAttribute && el.getAttribute('aria-label');
            if (label) {
                lista.push(label);
            }
            if (el.shadowRoot) {
                coletarLabels(el.shadowRoot, lista);
            }
        }
        return lista;
    }
    return coletarLabels(document, []);
    """
    return navegador.execute_script(script)


def buscar_label_likes_video(navegador):
    todos = listar_todos_aria_labels(navegador)
    candidatos = [
        label for label in todos
        if "gostei" in label.lower() and "coment" not in label.lower()
    ]
    return candidatos[0] if candidatos else None


def extrair_numero_do_texto(texto):
    if not texto:
        return None
    match = re.search(r"\d[\d.,]*", texto)
    if match:
        return match.group()
    return None


def coleta_dados():
    try:
        elemento = esperar_texto(By.CSS_SELECTOR, "h1.ytd-watch-metadata, #title h1")
        titulo_video = elemento.text.strip()
    except Exception as e:
        print("Falhou título:", e)
        titulo_video = "Não identificado"

    try:
        elemento = esperar_texto(By.CSS_SELECTOR, "ytd-channel-name #text-container")
        nome_canal = elemento.text.strip()
    except Exception as e:
        print("Falhou canal:", e)
        nome_canal = "Não identificado"

    try:
        elemento = esperar_texto(By.ID, "owner-sub-count")
        num_inscritos = elemento.text.strip()
    except Exception as e:
        print("Falhou inscritos:", e)
        num_inscritos = "Não identificado"

    try:
        label_likes = buscar_label_likes_video(navegador)
        likes = extrair_numero_do_texto(label_likes)
        if likes is None:
            likes = "Não identificado"
    except Exception as e:
        print("Falhou likes:", e)
        likes = "Não identificado"

    navegador.execute_script("window.scrollBy(0, 600)")
    time.sleep(3)

    comentarios = navegador.find_elements(By.CSS_SELECTOR, "#content-text")

    return {
        "canal": nome_canal,
        "inscritos": num_inscritos,
        "video": titulo_video,
        "likes": likes,
        "comentarios": [comentario.text for comentario in comentarios[:5] if comentario.text]
    }


dados = coleta_dados()

print("Nome do canal:", dados["canal"], "Nº de inscritos:", dados["inscritos"], "Título do vídeo:", dados["video"], "Nº de likes:", dados["likes"])

for comentario in dados["comentarios"]:
    print("-", comentario)

with open("dados_youtube.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, ensure_ascii=False, indent=4)

print("Dados salvos com sucesso no arquivo dados_youtube.json")