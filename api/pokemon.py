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
        logging.info('--------------------------------------------')

    def get(self):
        logging.info('[CSV] 1º Passo')
        logging.info('[CSV] Extraindo pokemons')
        repository = PokemonRepository()
        pokemons = repository.find_all_pokemons()
        logging.info('[CSV] Total de pokemons encontrados: %s', len(pokemons))
        logging.info('--------------------------------------------')

        logging.info('[MongoDB] 2º Passo')
        logging.info('[MongoDB] Extraindo detalhes')
        repository = PokemonDetalhesRepository()
        detalhes = repository.find_all_detalhes()
        logging.info('[MongoDB] Total de detalhes encontrados: %s', len(detalhes))
        logging.info('--------------------------------------------')

        logging.info('[MySQL] 3º Passo')
        logging.info('[MySQL] Extraindo habilidades')
        repository = PokemonHabilidadesRepository()
        habilidades = repository.find_all_habilidades()
        logging.info('[MySQL] Total de habilidades encontrados: %s', len(habilidades))

        resultado = merge(pokemons=pokemons, detalhes=detalhes, habilidades=habilidades)

        return jsonify(resultado)


class Response:

    def __init__(self):
        self.id = None
        self.nome = ""
        self.lendario = False
        self.velocidade = None


def merge(pokemons, detalhes, habilidades):
    resultado = []
    for p in pokemons:
        response = Response()
        response.id = int(p['id'])
        response.nome = p['nome']

        for d in detalhes:
            if response.id == d["pokemonId"]:
                response.lendario = d["lendario"]

        pokemon = response.__dict__
        resultado.append(pokemon)

    return resultado
