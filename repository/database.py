import logging

logging.basicConfig(level=logging.INFO)


def get_connection_mongo_db():
    logging.info('>>> [Conectando MongoDB] pokemon-detalhes-db')
    url_conexao = 'mongodb://localhost:27017/pokemon-detalhes-db'
    from pymongo import MongoClient
    client = MongoClient(url_conexao)
    return client['pokemon-detalhes-db'];


def get_connection_mysql_db():
    logging.info('>>> [Conectando MysqlDB] pokemon-habilidades-db')
