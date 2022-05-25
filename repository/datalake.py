import logging

from repository import database


##############################################
# https://www.mongodb.com/languages/python
##############################################
class DataLakeRepository:

    def __init__(self):
        self.collection_name = 'pokemons'

    def insert_pokemons(self, dados):
        connect = database.get_connection_mongodb_datalake()
        collection_pokemon_detalhes = connect[self.collection_name]
        try:
            logging.info('[MongoDB] - Inserindo pokemons [datalake_db]')
            pokemons = connect['pokemons']
            pokemons.delete_many({})
            pokemons.insert_many(dados)
            logging.info('[MongoDB] - Total de pokemons inseridos: ' + str(len(dados)))
        except Exception as e:
            logging.error(e)
