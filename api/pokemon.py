from flask import jsonify
from flask_restful import Resource
from repository.pokemon import PokemonRepository
from repository.pokemon_detalhes import PokemonDetalhesRepository
from repository.pokemon_habilidades import PokemonHabilidadesRepository

import logging

# https://flask-restful.readthedocs.io/en/latest/quickstart.html
# https://www.datacamp.com/tutorial/json-data-python

logging.basicConfig(level=logging.INFO)


class Pokemon(Resource):

    def __init__(self):
        logging.info('[GET] /api/pokemons')

    def get(self):
        logging.info('1º > Buscando pokemons na base de dados [CSV]')
        repository = PokemonRepository()
        pokemons = repository.find_all_pokemons()
        logging.info('Total de pokemons encontrados: %s', len(pokemons))

        logging.info('--------------------------------------------')

        logging.info('2º > Buscando detalhes na base de dados [MongoDB]')
        repository = PokemonDetalhesRepository()
        detalhes = repository.find_all_detalhes()
        logging.info('Total de detalhes encontrados: %s', len(detalhes))

        logging.info('--------------------------------------------')

        logging.info('3º > Buscando habilidades na base de dados [Mysql]')
        repository = PokemonHabilidadesRepository()
        habilidades = repository.find_all_habilidades()
        logging.info('Total de habilidades encontrados: %s', len(habilidades))

        return jsonify(pokemons)