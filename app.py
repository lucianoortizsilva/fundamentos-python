from flask import Flask, jsonify
from flask_restful import Api
from waitress import serve  # https://pypi.org/project/waitress/
from repository import conexao_mongo_db
from api.pokemon import Pokemon

import logging

app = Flask(__name__)


def config_log():
    logging.basicConfig(level=logging.INFO)


def config_server():
    with app.app_context():
        conexao_mongo_db.inserir_carga_dados_inicial()
    api = Api(app)
    api.add_resource(Pokemon, '/api/pokemons')


# https://flask.palletsprojects.com/en/2.1.x/api/
def init():
    logging.info('>>> Iniciando App ...')
    config_log()
    config_server()


# Executar na pasta raiz: pip freeze > requirements.txt
if __name__ == '__main__':
    init()
    serve(app, host="0.0.0.0", port=5000)
