from datetime import datetime, timedelta
import math

from flask import request, jsonify, make_response
from GoogleNews import GoogleNews 

def get_google_news():
    googlenews = GoogleNews()
    googlenews.set_lang('pt-br')
    if request.args:

        date_init = str(request.args.get('di'))
        date_end = str(request.args.get('de'))
        counter = int(request.args.get('c'))

        if counter > 0:
            return make_response(jsonify({}), 200)

        date_init = datetime.strptime(date_init, r"%Y-%m-%d")
        date_end = datetime.strptime(date_end, r"%Y-%m-%d")

        googlenews.get_news("'vírus chinês'")
        googlenews.get_news("'preconceito amarelo'") 
        googlenews.get_news("'preconceito asiático'") 
        googlenews.get_news("'racismo asiático'")
        googlenews.get_news("'discriminação contra asiáticos'")
        googlenews.get_news("'ataques a asiáticos'")
        googlenews.get_news("'violência contra asiáticos'")
        googlenews.get_news("'violência contra orientais'")
        googlenews.get_news("'ódio contra asiáticos'")
        
        googlenews.set_time_range(start=date_init, end=date_end)
    
        results = googlenews.result() 
        
        for result in results:
            try:
                if math.isnan(result['datetime']):
                    result['datetime'] = 'null'
            except TypeError:
                pass

        res = make_response(jsonify(results), 200)
            
    return res