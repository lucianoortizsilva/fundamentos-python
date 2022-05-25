import logging

from repository import database


##############################################
# https://www.mongodb.com/languages/python
##############################################
class PokemonDetalhesRepository:

    def __init__(self):
        self.collection_name = 'pokemonDetalhes'

    def find_all_detalhes(self):
        connect = database.get_connection_mongo_db()
        collection_pokemon_detalhes = connect[self.collection_name]
        try:
            cursorMongoDB = collection_pokemon_detalhes.find()
            detalhes = []
            for token in cursorMongoDB:
                pokemonID = int(token['pokemon_id'])
                geracao = int(token['geracao'])
                lendario = bool(token['lendario'])
                obj = dict({'pokemonId': pokemonID,'geracao': geracao,'lendario': lendario})
                detalhes.append(obj)
            return detalhes
        except Exception as e:
            logging.error(e)
