import logging

from repository import database


##############################################
# https://www.mongodb.com/languages/python
##############################################
class PokemonDetalhesRepository:

    def __init__(self):
        self.collection_name = 'detalhes'

    def find_all_detalhes(self):
        connect = database.get_connection_mongodb_pokemon()
        collection_pokemon_detalhes = connect[self.collection_name]
        try:
            cursorMongoDB = collection_pokemon_detalhes.find()
            detalhes = dict()
            for token in cursorMongoDB:
                pokemonID = int(token['pokemon_id'])
                geracao = int(token['geracao'])
                lendario = bool(token['lendario'])
                obj = dict({pokemonID: {'geracao': geracao, 'lendario': lendario}})
                detalhes.update(obj)
            return detalhes
        except Exception as e:
            logging.error(e)
