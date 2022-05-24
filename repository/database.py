import logging
from decouple import config

logging.basicConfig(level=logging.INFO)


def get_connection_mongo_db():
    logging.info('>>> [Conectando MongoDB] pokemon-detalhes-db')

    print('############################')
    print(config('URL_CONEXAO_MONGODB'))
    print('############################')

    url_conexao = config('URL_CONEXAO_MONGODB')
    from pymongo import MongoClient
    client = MongoClient(url_conexao)
    return client['pokemon-detalhes-db'];


def get_connection_mysql_db():
    logging.info('>>> [Conectando MysqlDB] pokemon-habilidades-db')
