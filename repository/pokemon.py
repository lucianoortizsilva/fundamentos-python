import csv
import logging


##############################################
# https://docs.python.org/3/library/csv.html
##############################################
class PokemonRepository:
    FILE = 'db/pokemon.csv'

    def find_all_pokemons(self):
        with open(self.FILE, mode="r", newline="", encoding="utf8") as f:
            pokemons = []
            reader = csv.reader(f)
            for row in reader:
                pokemons.append(tuple(row))
            logging.info('Total de pokemons encontrados: %s', len(pokemons))
            return pokemons
