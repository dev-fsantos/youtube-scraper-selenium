import json
import pandas as pd

with open("dados_youtube.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

def limpar_numero(texto):
    if not isinstance(texto, str):
        return None

    texto = texto.lower().strip()
    partes = texto.split()
    numero_texto = partes[0]

    if "," in numero_texto:
        numero_texto = numero_texto.replace(".", "").replace(",", ".")
    else:
        numero_texto = numero_texto.replace(".", "")

    numero = float(numero_texto)

    if "mi" in texto:
        numero = numero * 1_000_000
    elif "mil" in texto:
        numero = numero * 1_000

    return numero
