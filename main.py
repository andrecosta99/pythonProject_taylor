from flask import Flask, render_template, request
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

# Função para ler dados do CSV
def ler_dados_csv(caminho_arquivo):
    try:
        dados = pd.read_csv(caminho_arquivo)
        return dados
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return None

# Função para gerar gráfico
def gerar_grafico(dados):
    plt.figure()
    dados.plot(kind='bar')  # Exemplo de gráfico de barras
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return plot_url

@app.route('/', methods=['GET', 'POST'])
def index():
    dados = ler_dados_csv('data/taylor_swift_videos.csv')

    if request.method == 'POST':

        # filtrar por data de publicação
        data_inicio = request.form.get('data_inicio')
        data_fim = request.form.get('data_fim')
        if data_inicio and data_fim:
            dados = dados[(dados['published_at'] >= data_inicio) & (dados['published_at'] <= data_fim)]



    if dados is not None:
        plot_url = gerar_grafico(dados)
        return render_template('index.html', dados=dados, plot_url=plot_url)
    else:
        return "Erro ao carregar dados."


if __name__ == '__main__':
    app.run(debug=True)
