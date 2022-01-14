from GoogleNews import GoogleNews 

def get_google_news():
    googlenews = GoogleNews()
    googlenews.set_lang('pt-br')
    googlenews.set_time_range(start='31/12/2019', end='14/01/2022')

    googlenews.get_news("'vírus chinês'")
    googlenews.get_news("'preconceito amarelo'") 
    googlenews.get_news("'preconceito asiático'") 
    googlenews.get_news("'racismo asiático'")
    googlenews.get_news("'discriminação contra asiáticos'")
    googlenews.get_news("'ataques a asiáticos'")
    googlenews.get_news("'violência contra asiáticos'")
    googlenews.get_news("'violência contra orientais'")
    googlenews.get_news("'ódio contra asiáticos'")
    materias = googlenews.result() 

    dados_em_html = """<div class="row row-cols-1 row-cols-md-2 g-4">"""

    for materia in materias: 
        
        linha = f"""
        <div class="card" style="width: 18rem;">
            <a href="https://{materia['link']}"><img src="{materia['img']}" class="card-img-top" alt="{materia['title']}"></a>
            <div class="card-body">
                <p class="card-text">{materia['title']}</p>
                <ul class="list-group list-group-flush">
                <li class="list-group-item">{materia['site']}</li>
                <li class="list-group-item">{materia['date']}</li>
                </ul>
            </div>
        </div>
        """
        dados_em_html += linha

    dados_em_html += """"</div>"""

    return dados_em_html