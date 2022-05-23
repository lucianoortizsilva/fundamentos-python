import csv

##############################################
# https://www.mongodb.com/languages/python
##############################################
class PokemonDetalhesRepository:

    def find_all_detalhes(self):
        with open(self.FILE, mode="r", newline="", encoding="utf8") as f:
            pokemons = []
            reader = csv.reader(f)
            for row in reader:
                pokemons.append(tuple(row))
            return pokemons
