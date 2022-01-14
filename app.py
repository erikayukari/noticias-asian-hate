
import nltk
import pandas as pd
import os
from pandas import json_normalize 
from flask import Flask, render_template
from GoogleNews import GoogleNews 
from datetime import date
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
  googlenews.set_time_range(start='31/12/2019', end=date.today()) #seleciona a janela temporal da busca

  googlenews.get_news("'vírus chinês'") #seta o primeiro termo de busca 
  googlenews.get_news("'preconceito amarelo'") 
  googlenews.get_news("'preconceito asiático'") 
  googlenews.get_news("'racismo asiático'")
  googlenews.get_news("'discriminação contra asiáticos'")
  googlenews.get_news("'ataques a asiáticos'")
  googlenews.get_news("'violência contra asiáticos'")
  googlenews.get_news("'violência contra orientais'")
  googlenews.get_news("'ódio contra asiáticos'") #seta o último termo de busca 
  resultado = googlenews.result() 

  df = pd.DataFrame(resultado) #coloca o resultado em uma tabela
  dados_em_html = "" #cria uma lista vazia para inserir o resultado 
  for materia in df.itertuples(): #possibilita que o código manipule o formato em que os dados serão visualizados na lista 
    linha = f'{materia.date}______{materia.site}______<a href="https://{materia.link}">{materia.title}</a><br>' #coloca o título e o link em cada linha da lista
    dados = dados_em_html
    dados_em_html = dados + linha
  return render_template("noticias.html", dados = dados_em_html) # chama a variável lista_final para ser mostrada nesta seção do site 
  
  
@app.route('/analise')

def analises():
    return render_template("analises.html")
    nltk.download('punkt') 
    
    #String text pega todos os títulos do arquivo
    text = ''
    for index, row in dataframe.iterrows():
        text = text + row['title'].lower() + ' ' 
        
    from nltk.tokenize import word_tokenize
    tokenized_word=word_tokenize(text)
    print(tokenized_word)
    
    from nltk.probability import FreqDist
    fdist = FreqDist(tokenized_word)
    print(fdist)
    fdist.most_common(2)
    
    
    # Frequency Distribution Plot
    import matplotlib.pyplot as plt
    fdist.plot(30,cumulative=False)
    plt.show()
    
    nltk.download('stopwords')
    from nltk.corpus import stopwords
    stop_words=set(stopwords.words("portuguese"))
    print(stop_words)
    
    
    #tokenized_sent = ['Hello', 'Mr.', 'Smith', ',', 'how', 'are', 'you', 'doing', 'today', '?']
    tokenized_sent = tokenized_word
    filtered_sent=[]
    for w in tokenized_sent:
    if w not in stop_words:
        filtered_sent.append(w)
    print("Tokenized Sentence:",tokenized_sent)
    print("Filterd Sentence:",filtered_sent)
    
    # Frequency Distribution Plot
    fdist = FreqDist(filtered_sent)
    print(fdist)
    fdist.plot(30,cumulative=False)
    plt.show()

    filtered_sent=[]
    for w in tokenized_sent:
    if w not in stop_words:
        filtered_sent.append(w)
# Frequency Distribution Plot
    fdist = FreqDist(filtered_sent)
    fdist.plot(30,cumulative=False)
    plt.show()

