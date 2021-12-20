
import pandas as pd
import os
from pandas import json_normalize 
from flask import Flask, render_template

app = Flask(__name__)

#início raspagem -----------------------------------
!pip install GoogleNews #instala a biblioteca      
from GoogleNews import GoogleNews 
googlenews = GoogleNews()
googlenews.set_time_range(start='31/12/2019', end='17/12/2021') #seleciona a janela temporal da busca
googlenews.get_news("'preconceito amarelo'") #seta o primeiro termo de busca 
resultado = googlenews.result() 
df = pd.DataFrame(resultado)
df.drop(columns=['desc', 'datetime', 'img', 'media']) #elimina colunas que não interessam da tabela 
df

#fim raspagem---------------------------------------
@app.route("/")
def hello_world():
    return render_template("home.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")


@app.route("/youtube")
def youtube():
   dados_canal = dados_youtube()
   return render_template("youtube.html", dados=dados_canal)
  
 #início telegram ------------------------------------

from flask import request
import requests

@app.route("/telegram", methods=["POST"])
def telegram():
        
    #Robô processa mensagem
    token = os.environ["TELEGRAM_TOKEN"]
    update = request.json
    chat_id = update["message"]["chat"]["id"]
    text = update["message"]["text"].lower()
    if text in ["oi", "olá", "ola", "olar"]:
        answer = "Oi!Como vai?"
    elif text in ["bom dia", "boa tarde", "boa noite"]:
        answer = text 
    else: 
        answer = "Não entendi!"  
            
    #Robô responde no telegram 
    message = {"chat_id": chat_id, "text":answer}
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    requests.post(url, data=message)
    
    #Robô retorna ao telegram
    return "ok"


