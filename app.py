
import pandas as pd
import os
from pandas import json_normalize 
from flask import Flask, render_template

app = Flask(__name__)

def dados_youtube():
    chave= os.environ["YOUTUBE_API_KEY"]
    canal="UCqRBKOf_OvnNNvmbhVVbX-A"
    url_canal = f"https://www.googleapis.com/youtube/v3/channels?part=id%2Csnippet%2CcontentDetails%2Cstatistics&id={canal}&key={chave}"
    resposta = requests.get(url_canal)
    dados_canal = resposta.json()
    return dados_canal

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


