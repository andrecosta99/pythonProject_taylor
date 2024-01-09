import pandas as pd

def ler_dados_csv(caminho_arquivo):
    try:
        dados = pd.read_csv(caminho_arquivo)
        return dados
    except FileNotFoundError:
        print("Erro")
        return None