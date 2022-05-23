from flask import jsonify
from flask_restful import Resource
from repository.pokemon import PokemonRepository
import logging

# https://flask-restful.readthedocs.io/en/latest/quickstart.html
# https://www.datacamp.com/tutorial/json-data-python

logging.basicConfig(level=logging.INFO)


class Pokemon(Resource):

    def __init__(self):
        logging.info('[GET] /api/pokemons')

    def get(self):
        logging.info('Buscando pokemons na base de dados CSV')
        repository = PokemonRepository()
        dados = repository.find_all_pokemons()
        pokemons = []
        for p in dados:
            obj = dict({"id": int(p[0]), "nome": p[1], "tipos": [p[2], p[3]]})
            pokemons.append(obj)
        return jsonify(pokemons)
