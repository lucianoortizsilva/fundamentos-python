import csv


##############################################
# https://docs.python.org/3/library/csv.html
##############################################
class PokemonRepository:

    def __init__(self):
        self.file = 'db/pokemon.csv'

    def find_all_pokemons(self):
        with open(self.file, mode="r", newline="", encoding="utf8") as f:
            pokemons = []
            reader = csv.reader(f)
            for row in reader:
                obj = dict({"id": int(row[0]), "nome": row[1]})
                pokemons.append(obj)
            return pokemons
