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
        try:
            logging.info('[MongoDB] - Inserindo pokemons [datalake_db]')
            collectionPokemons = connect[self.collection_name]
            collectionPokemons.delete_many({})
            collectionPokemons.insert_many(dados)
            logging.info('[MongoDB] - Total de pokemons inseridos: ' + str(len(dados)))
        except Exception as e:
            logging.error(e)

    def find_all_pokemons(self):
        connect = database.get_connection_mongodb_datalake()
        try:
            logging.info('[MongoDB] - Buscando pokemons [datalake_db]')
            collectionPokemons = connect[self.collection_name]
            cursor = collectionPokemons.find()
            pokemons = []
            for pokemon in cursor:
                pokemons.append(pokemon)
            return pokemons
        except Exception as e:
            logging.error(e)
