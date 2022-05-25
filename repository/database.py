import logging
from decouple import config
from mysql import connector


logging.basicConfig(level=logging.INFO)


def get_connection_mongo_db():
    logging.info('>>> [Conectando MongoDB] pokemon-detalhes-db')
    url_conexao = config('URL_CONEXAO_MONGODB')
    from pymongo import MongoClient
    client = MongoClient(url_conexao)
    return client['pokemon-detalhes-db'];


def get_connection_mysql_db():
    try:
        host = config('MYSQL_HOST')
        user = config('MYSQL_USER')
        password = config('MYSQL_PASSWORD')
        connect = connector.connect(user=user, password=password, host=host)
        logging.info('>>> [MysqlDB] Conexão aberta')
        return connect
    except Exception as e:
        logging.error(e)
