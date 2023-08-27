from flask import jsonify
from flask_restful import Resource
from repository.datalake import DataLakeRepository
import logging


# https://flask-restful.readthedocs.io/en/latest/quickstart.html
# https://www.datacamp.com/tutorial/json-data-python
class Datalake(Resource):

    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        logging.info('[GET] /api/datalake/pokemons')

    @staticmethod
    def get():
        try:
            repository = DataLakeRepository()
            pokemons = repository.find_all_pokemons()
            return jsonify(pokemons)
        except Exception as e:
            logging.error(e)
            return jsonify({'status': 'Ops! Não foi desta vez'})