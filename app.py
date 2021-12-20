
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

@app.route('/noticias', methods=("POST", "GET"))
def noticias():
  googlenews = GoogleNews()
  googlenews.set_time_range(start='31/12/2019', end='17/12/2021') #seleciona a janela temporal da busca
  googlenews.get_news("'preconceito amarelo'") #seta o primeiro termo de busca 
  googlenews.get_news("'preconceito asiático'") 
  googlenews.get_news("'vírus chinês'")
  googlenews.get_news("'violência contra asiáticos'")
  googlenews.get_news("'ódio contra asiáticos'")
  resultado = googlenews.result() 
  df = pd.DataFrame(resultado)
  df1= df.drop(columns=['desc', 'datetime', 'img', 'media']) #elimina colunas que não interessam da tabela 
  df1
  return render_template('noticias.html', tables=[df1.to_html(classes='data', header="true")])




