import logging
from decouple import config
from mysql import connector

logging.basicConfig(level=logging.INFO)


def get_connection_mongodb_pokemon():
    try:
        url_conexao = config('URL_CONEXAO_MONGODB_POKEMON')
        from pymongo import MongoClient
        client = MongoClient(url_conexao)
        logging.info('[MongoDB] Conexão aberta')
        return client['pokemon_db']
    except Exception as e:
        logging.error(e)


def get_connection_mongodb_datalake():
    try:
        url_conexao = config('URL_CONEXAO_MONGODB_DATALAKE')
        from pymongo import MongoClient
        client = MongoClient(url_conexao)
        logging.info('[MongoDB] Conexão aberta')
        return client['datalake_db']
    except Exception as e:
        logging.error(e)


def get_connection_mysql_db():
    try:
        host = config('MYSQL_HOST')
        user = config('MYSQL_USER')
        password = config('MYSQL_PASSWORD')
        connect = connector.connect(user=user, password=password, host=host)
        logging.info('[MySQL] Conexão aberta')
        return connect
    except Exception as e:
        logging.error(e)
