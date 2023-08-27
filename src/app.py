from flask import Flask
from flask_restful import Api
from waitress import serve
from repository import setup
from api.legado import Legado
from api.datalake import Datalake

import logging

app = Flask(__name__)


def config_log():
    logging.basicConfig(level=logging.INFO)


def config_server():
    with app.app_context():
        setup.inserir_carga_dados_inicial()
    api = Api(app)
    api.add_resource(Legado, '/api/legado/etl')
    api.add_resource(Datalake, '/api/datalake/pokemons')


def init():
    logging.info('>>> Iniciando App ...')
    config_log()
    config_server()


# https://flask.palletsprojects.com/en/2.1.x/api/
# https://pypi.org/project/waitress/
# Executar na pasta raiz: pip freeze > requirements.txt
if __name__ == '__main__':
    init()
    serve(app, host="0.0.0.0", port=5000)
