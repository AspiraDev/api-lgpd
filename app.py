from flask import Flask, jsonify
from urllib.request import urlopen
from bs4 import BeautifulSoup
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['DEBUG'] = True

@app.route('/')
def index():
    return '<h1>API que retorna os artigos da Lei Geral de Proteção de Dados Pessoais</p>'

@app.route('/artigo<int:artigo>/')

def hello(artigo):
   
    if artigo <= 6:
            capitulo = "Capítulo I - DISPOSIÇÕES PRELIMINARES"
            url = 'https://lgpd-brasil.info/capitulo_01/artigo_0' + str(artigo)

    elif artigo >= 7 and artigo <= 9:
            capitulo = "Capítulo II - DO TRATAMENTO DE DADOS PESSOAIS"
            url = 'https://lgpd-brasil.info/capitulo_02/artigo_0' + str(artigo)

    elif artigo >= 10 and artigo <= 16:
            capitulo = "Capítulo II - DO TRATAMENTO DE DADOS PESSOAIS"
            url = 'https://lgpd-brasil.info/capitulo_02/artigo_' + str(artigo)

    elif artigo >= 17 and artigo <= 22:
            capitulo = "Capítulo III - DOS DIREITOS DO TITULAR" 
            url = 'https://lgpd-brasil.info/capitulo_03/artigo_' + str(artigo)

    elif artigo >= 23 and artigo <= 32:
            capitulo = "Capítulo IV - DO TRATAMENTO DE DADOS PESSOAIS PELO PODER PÚBLICO"
            url = 'https://lgpd-brasil.info/capitulo_04/artigo_' + str(artigo)

    elif artigo >= 33 and artigo <= 36:
            capitulo = "Capítulo V - DA TRANSFERÊNCIA INTERNACIONAL DE DADOS"
            url = 'https://lgpd-brasil.info/capitulo_05/artigo_' + str(artigo)

    elif artigo >= 37 and artigo <= 45:
            capitulo = "Capítulo VI - DOS AGENTES DE TRATAMENTO DE DADOS PESSOAIS"
            url = 'https://lgpd-brasil.info/capitulo_06/artigo_' + str(artigo)

    elif artigo >= 46 and artigo <= 51:
            capitulo = "Capítulo VII - DA SEGURANÇA E DAS (BOAS) PRÁTICAS"
            url = 'https://lgpd-brasil.info/capitulo_07/artigo_' + str(artigo)

    elif artigo >= 52 and artigo <= 54:
            capitulo = "Capítulo VIII - DA FISCALIZAÇÃO"
            url = 'https://lgpd-brasil.info/capitulo_08/artigo_' + str(artigo)

    elif artigo >= 55 and artigo <= 59:
            capitulo = "Capítulo IX - DA AUTORIDADE NACIONAL DE PROTEÇÃO DE DADOS (ANPD) E DO CONSELHO NACIONAL DE PROTEÇÃO DE DADOS PESSOAIS E DA PRIVACIDADE"
            url = 'https://lgpd-brasil.info/capitulo_09/artigo_' + str(artigo)

    elif artigo >= 60 and artigo <= 65:
            capitulo = "Capítulo X - DISPOSIÇÕES FINAIS E TRANSITÓRIAS"
            url = 'https://lgpd-brasil.info/capitulo_10/artigo_' + str(artigo)
    
    elif artigo > 65:
            return '<h1>Pesquise por termos entre 1 e 65</p>'

    response = urlopen(url)
    html = response.read()

    soup = BeautifulSoup(html, 'html.parser')

    div = soup.find("div", { "class" : "text" })
    texto = div.find('p').get_text()

    try:
        titulo = soup.find("h2").text
    except:
        titulo = ""

    div2 = soup.find("div", { "class" : "text" })

    try:
        texto2 = div2.find_all('div')[0].get_text()
    except:
        texto2 = ""

    try:
        texto3 = div2.find_all('div')[1].get_text()
    except:
        texto3 = ""

    itens = []

    itens.append({
    "artigo":""+str(artigo)+"",
    "capitulo":capitulo,
    "titulo":titulo,
    "texto":str(texto)+str(texto2)+str(texto3)
    })

    app.config['JSON_AS_ASCII'] = False
    if artigo <= 65:
        return jsonify(itens)


app.run(host="0.0.0.0", port=8000)


