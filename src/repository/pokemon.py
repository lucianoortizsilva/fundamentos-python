import csv

import logging


##############################################
# https://docs.python.org/3/library/csv.html
##############################################
class PokemonRepository:

    def __init__(self):
        self.file = 'src/db/pokemon.csv'

    def find_all_pokemons(self):
        try:
            with open(self.file, mode="r", newline="", encoding="utf8") as f:
                pokemons = []
                reader = csv.reader(f)
                for row in reader:
                    obj = dict({'id': int(row[0]), 'nome': row[1], 'tipos': [row[2], row[3]]})
                    pokemons.append(obj)
                return pokemons
        except Exception as e:
            logging.error(e)
