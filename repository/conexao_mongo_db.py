import logging
import csv

logging.basicConfig(level=logging.INFO)


def get_database():
    logging.info('>>> [Conectando MongoDB] pokemon-detalhes-db')
    url_conexao = 'mongodb://localhost:27017/pokemon-detalhes-db'
    from pymongo import MongoClient
    client = MongoClient(url_conexao)
    return client['pokemon-detalhes-db'];


def inserir_carga_dados_inicial():
    logging.info('[pokemon-detalhes-db] - Carregando carga de dados')
    try:
        with open('db/pokemon_detalhe.csv', mode='r', newline='', encoding='utf8') as f:
            detalhes = []
            reader = csv.reader(f)
            for row in reader:
                obj = dict({'pokemon_id': int(row[0]), 'geracao': int(row[1]), 'lendario': bool(row[2])})
                detalhes.append(obj)
        db = get_database()
        pokemonDetalhes = db['pokemonDetalhes']
        pokemonDetalhes.delete_many({})
        pokemonDetalhes.insert_many(detalhes)
        logging.info('[pokemon-detalhes-db] - Dados inseridos com sucesso')
    except Exception:
        raise Exception('Erro ao tentar inserir carga dados inicial')
