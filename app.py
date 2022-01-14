import logging

from flask import Flask, render_template

from utils.news import get_google_news

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route('/noticias')
def news():
    dados_em_html = get_google_news()
    return render_template("noticias.html", dados = dados_em_html)
  