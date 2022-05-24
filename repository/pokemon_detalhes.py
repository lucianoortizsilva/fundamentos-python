from repository import conexao_mongo_db
import logging


##############################################
# https://www.mongodb.com/languages/python
##############################################
class PokemonDetalhesRepository:

    def __init__(self):
        self.db = conexao_mongo_db.get_database()

    def find_all_detalhes(self):
        collection_pokemon_detalhes = self.db['pokemonDetalhes']
        cursorMongoDB = collection_pokemon_detalhes.find()
        detalhes = []
        for token in cursorMongoDB:
            pokemonID = int(token['pokemon_id'])
            lendario = bool(token['lendario'])
            obj = dict({"pokemonId": pokemonID, "lendario": lendario})
            detalhes.append(obj)
        return detalhes
