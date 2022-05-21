from flask import Flask, jsonify
from repository.pokemon import PokemonRepository
import logging

# https://flask-restful.readthedocs.io/en/latest/quickstart.html
# https://www.datacamp.com/tutorial/json-data-python

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)


@app.route('/pokemons')
def get_pokemons():
    logging.info('Buscando pokemons na base de dados CSV')
    repository = PokemonRepository()
    dados = repository.find_all_pokemons()
    pokemons = []
    for p in dados:
        obj = dict({"id": p[0], "nome": p[1], "tipos": [p[2], p[3]]})
        logging.info('Pokemon encontrado: {}'.format(obj))
        pokemons.append(obj)
    return jsonify(pokemons)


if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)
