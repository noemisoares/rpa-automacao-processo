import pandas as pd

def tratar_dados():
    df = pd.read_csv("data/dados_extraidos.csv")

    df["Preco"] = df["Preco"].str.replace("$", "").astype(float)
    df["Preco_com_imposto"] = df["Preco"] * 1.10

    df.to_csv("data/dados_tratados.csv", index=False)
