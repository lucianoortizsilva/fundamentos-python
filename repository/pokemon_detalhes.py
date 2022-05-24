from repository import database


##############################################
# https://www.mongodb.com/languages/python
##############################################
class PokemonDetalhesRepository:

    def __init__(self):
        self.db = database.get_connection_mongo_db()

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
