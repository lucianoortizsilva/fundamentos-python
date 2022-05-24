import logging

logging.basicConfig(level=logging.INFO)


def get_database():
    logging.info('>>> [Conectando MongoDB] pokemon-detalhes-db')
    url_conexao = 'mongodb://localhost:27017/pokemon-detalhes-db'
    from pymongo import MongoClient
    client = MongoClient(url_conexao)
    return client['pokemon-detalhes-db'];