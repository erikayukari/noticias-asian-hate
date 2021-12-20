
import pandas as pd
import os
from pandas import json_normalize 
from flask import Flask, render_template
from GoogleNews import GoogleNews 
app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("home.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route('/noticias')
def news():
  googlenews = GoogleNews()
  googlenews.set_lang('pt-br') #seleciona apenas resultados  língua portuguesa
  googlenews.set_time_range(start='31/12/2019', end='31/12/2021') #seleciona a janela temporal da busca
  googlenews.get_news("'preconceito amarelo'") #seta o primeiro termo de busca 
  googlenews.get_news("'preconceito asiático'") 
  googlenews.get_news("'vírus chinês'")
  googlenews.get_news("'violência contra asiáticos'")
  googlenews.get_news("'ódio contra asiáticos'") #seta o último termo de busca 
  resultado = googlenews.result() 
  df = pd.DataFrame(resultado) #coloca o resultado em uma tabela 
  #lista = df['link'].tolist() # seleciona apenas a coluna de links de notícias da tabela e os insere em uma lista
  #lista_final = ''.join(lista) # transforma coluna de links em uma única string [texto] para importá-la e apresentá-la no site 
  return render_template("noticias.html", dados = resultado.to_html()) # chama a variável lista_final para ser mostrada nesta seção do site 
  



