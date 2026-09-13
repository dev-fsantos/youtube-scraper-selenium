import json
import pandas as pd
import matplotlib.pyplot as plt

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

    try:
        numero = float(numero_texto)
    except ValueError:
        return None

    if "mi" in texto:
        numero = numero * 1_000_000
    elif "mil" in texto:
        numero = numero * 1_000

    return numero


with open("dados_youtube.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

df = pd.DataFrame(dados)

df["inscritos_num"] = df["inscritos_texto"].apply(limpar_numero)
df["visualizacoes_num"] = df["visualizacoes_texto"].apply(limpar_numero)

df["taxa_engajamento"] = df["visualizacoes_num"] / df["inscritos_num"]

colunas_interesse = ["canal_buscado", "inscritos_num", "visualizacoes_num", "taxa_engajamento"]
print(df[colunas_interesse].sort_values("taxa_engajamento", ascending=False))

df_ordenado = df.sort_values("taxa_engajamento", ascending=False)

plt.figure(figsize=(8, 5))
plt.bar(df_ordenado["canal_buscado"], df_ordenado["taxa_engajamento"], color="orange")
plt.title("Visualizações Totais / Inscritos por canal")
plt.ylabel("Proporção (views totais por inscrito)")
plt.xlabel("Canal")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


