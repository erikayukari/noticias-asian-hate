
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
  googlenews.set_time_range(start='31/12/2019', end='14/01/2022') #seleciona a janela temporal da busca

  googlenews.get_news("'vírus chinês'") #seta o primeiro termo de busca 
  googlenews.get_news("'preconceito amarelo'") 
  googlenews.get_news("'preconceito asiático'") 
  googlenews.get_news("'racismo asiático'")
  googlenews.get_news("'discriminação contra asiáticos'")
  googlenews.get_news("'violência contra asiáticos'")
  googlenews.get_news("'ódio contra asiáticos'") #seta o último termo de busca 
  resultado = googlenews.result() 

  df = pd.DataFrame(resultado) #coloca o resultado em uma tabela
  dados_em_html = "" #cria uma lista vazia para inserir o resultado 
  for materia in df.itertuples(): #possibilita que o código manipule o formato em que os dados serão visualizados na lista 
    linha = f'<a href="https://{materia.link}">{materia.title}</a><br>' #coloca o título e o link em cada linha da lista
    dados = dados_em_html
    dados_em_html = dados + linha
  return render_template("noticias.html", dados = dados_em_html) # chama a variável lista_final para ser mostrada nesta seção do site 
  
  



