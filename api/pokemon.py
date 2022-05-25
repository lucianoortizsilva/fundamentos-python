from flask import jsonify
from flask_restful import Resource
from repository.pokemon import PokemonRepository
from repository.pokemon_detalhes import PokemonDetalhesRepository
from repository.pokemon_habilidades import PokemonHabilidadesRepository
from repository.datalake import DataLakeRepository
import logging


# https://flask-restful.readthedocs.io/en/latest/quickstart.html
# https://www.datacamp.com/tutorial/json-data-python
class Pokemon(Resource):

    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        logging.info('[GET] /api/pokemons')

    @staticmethod
    def get():
        try:
            logging.info('################')
            logging.info('##### EXTRACT')
            logging.info('################')
            pokemons = extract_pokemons()
            detalhes = extract_detalhes()
            habilidades = extract_habilidades()

            logging.info('################')
            logging.info('##### TRANSFORM')
            logging.info('################')
            dados = transform(pokemons=pokemons, detalhes=detalhes, habilidades=habilidades)

            logging.info('################')
            logging.info('##### LOAD')
            logging.info('################')
            load(dados)

            return jsonify({'status': 'Processo finalizado com sucesso'})
        except Exception as e:
            logging.error(e)
            return jsonify({'status': 'Ops! Não foi desta vez'})


class Response:

    def __init__(self):
        self.id = None
        self.nome = ""
        self.lendario = False
        self.velocidade = None


def extract_pokemons():
    logging.info('[CSV] 1º Passo')
    logging.info('[CSV] Extraindo pokemons')
    repository = PokemonRepository()
    pokemons = repository.find_all_pokemons()
    logging.info('[CSV] Total de pokemons encontrados: %s', len(pokemons))
    logging.info('--------------------------------------------')
    return pokemons


def extract_detalhes():
    logging.info('[MongoDB] 2º Passo')
    logging.info('[MongoDB] Extraindo detalhes')
    repository = PokemonDetalhesRepository()
    detalhes = repository.find_all_detalhes()
    logging.info('[MongoDB] Total de detalhes encontrados: %s', len(detalhes))
    logging.info('--------------------------------------------')
    return detalhes


def extract_habilidades():
    logging.info('[MySQL] 3º Passo')
    logging.info('[MySQL] Extraindo habilidades')
    repository = PokemonHabilidadesRepository()
    habilidades = repository.find_all_habilidades()
    logging.info('[MySQL] Total de habilidades encontrados: %s', len(habilidades))
    return habilidades


def transform(pokemons, detalhes, habilidades):
    logging.info('Transformando pokemons - inicio!!!')
    resultado = []
    for p in pokemons:
        response = Response()
        response.id = int(p['id'])
        response.nome = p['nome']
        response.lendario = detalhes[int(p['id'])]['lendario']
        response.velocidade = habilidades[int(p['id'])]['velocidade']
        resultado.append(response.__dict__)
    logging.info('Transformando pokemons - final!!!')
    return resultado


def load(dados):
    logging.info('Load datalake - inicio!!!')
    repository = DataLakeRepository()
    repository.insert_pokemons(dados=dados)
    logging.info('Load datalake - final!!!')