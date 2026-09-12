from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import json
import time
import re

def esperar_texto(by, valor, timeout=15):
    def condicao(navegador):
        try:
            elemento = navegador.find_element(by, valor)
            texto = elemento.text.strip()
            return elemento if texto != "" else False
        except:
            return False
    return WebDriverWait(navegador, timeout).until(condicao)

def listar_todos_textos(navegador):
    script = """
    function coletarTextos(root, lista) {
        const elementos = root.querySelectorAll('*');
        for (const el of elementos) {
            const tag = el.tagName ? el.tagName.toLowerCase() : '';
            if (tag === 'script' || tag === 'style') {
                continue;
            }
            if (el.children.length === 0 && el.innerText && el.innerText.trim() !== '' && el.innerText.length < 200) {
                lista.push(el.innerText.trim());
            }
            if (el.shadowRoot) {
                coletarTextos(el.shadowRoot, lista);
            }
        }
        return lista;
    }
    return coletarTextos(document, []);
    """
    return navegador.execute_script(script)

def buscar_texto_com_termo(lista_textos, termo):
    for texto in lista_textos:
        if termo in texto.lower():
            return texto
    return None

def extrair_numero_do_texto(texto):
    if not texto:
        return None
    match = re.search(r"\d[\d.,]*", texto)
    if match:
        return match.group()
    return None

def buscar_visualizacoes(lista_textos):
    for texto in lista_textos:
        texto_limpo = texto.lower()

        if "visualiza" in texto_limpo and extrair_numero_do_texto(texto):
            return texto

    return None

def coleta_dados_canal(canal_buscado):
    time.sleep(2)

    todos_textos = listar_todos_textos(navegador)
    texto_inscritos = buscar_texto_com_termo(todos_textos, "inscrit")
    texto_visualizacoes = buscar_visualizacoes(todos_textos)

    return {
        "canal_buscado": canal_buscado,
        "inscritos_texto": texto_inscritos if texto_inscritos else "Não identificado",
        "visualizacoes_texto": texto_visualizacoes if texto_visualizacoes else "Não identificado"
    }

def pedir_canais():
    entrada = input("Digite os canais que deseja analisar, separados por vírgula: ")
    lista_canais = entrada.split(",")
    lista_canais_limpa = [canal.strip() for canal in lista_canais]
    return lista_canais_limpa

canais = pedir_canais()
navegador = webdriver.Chrome()  
navegador.maximize_window()
todos_dados = []

for canal in canais:
    print(f"\n--- Coletando dados de {canal}")

    navegador.get(f"https://www.youtube.com/@{canal}/about")
    time.sleep(5)

    dados = coleta_dados_canal(canal)
    todos_dados.append(dados)


with open("dados_youtube.json", "w", encoding="utf-8") as arquivo:
    json.dump(todos_dados, arquivo, ensure_ascii=False, indent=4)

print("\n Dados de todos os canais salvos com sucesso!")

navegador.quit()

