from repository import database
from decouple import config
from distutils import util
import logging
import csv


def inserir_carga_dados_inicial():
    insert_mongodb()
    insert_mysql()


def insert_mongodb():
    try:
        with open('db/pokemon_detalhe.csv', mode='r', newline='', encoding='utf8') as f:
            detalhes = []
            reader = csv.reader(f)
            for row in reader:
                pokemon_id = int(row[0])
                geracao = int(row[1])
                lendario = bool(util.strtobool(row[2]))
                obj = dict({'pokemon_id': pokemon_id, 'geracao': geracao, 'lendario': lendario})
                detalhes.append(obj)
        db = database.get_connection_mongo_db()
        logging.info('[pokemon-detalhes-db] - Carregando carga de dados')
        pokemonDetalhes = db['pokemonDetalhes']
        pokemonDetalhes.delete_many({})
        pokemonDetalhes.insert_many(detalhes)
        logging.info('[pokemon-detalhes-db] - Dados inseridos com sucesso')
    except Exception:
        raise Exception('Erro ao tentar inserir carga dados inicial')


def insert_mysql():
    logging.info('[pokemon-detalhes-db] - Carregando carga de dados')
    create_data_base_mysql()
    create_table_pokemon_habilidades()
    insert_pokemon_habilidades()
    logging.info('[pokemon-detalhes-db] - Dados inseridos com sucesso')


def create_data_base_mysql():
    connect = database.get_connection_mysql_db()
    database_name = config('MYSQL_DATABASE')
    logging.info('Criando database pokemon-habilidades-db')
    create_db = 'CREATE DATABASE IF NOT EXISTS ' + str(database_name)
    try:
        with connect.cursor() as cursor:
            cursor.execute("SHOW DATABASES")
            logging.info('DATABASES: ')
            for db in cursor:
                logging.info(str(db))
    except Exception as e:
        logging.error(e)
    finally:
        if connect.is_connected():
            cursor.close()
            connect.close()
            logging.info('[MySQL] Conexão fechada')


def create_table_pokemon_habilidades():
    connect = database.get_connection_mysql_db()
    connect.database = config('MYSQL_DATABASE')
    create_table = '''
        CREATE TABLE IF NOT EXISTS pokemon_habilidades(
            pokemon_id int primary key,
            attack int null,
            defense int null,
            speed int null
    ) ENGINE=INNODB;'''
    logging.info('Criando tabela pokemon_habilidades')
    try:
        with connect.cursor() as cursor:
            cursor.execute(create_table)
            connect.commit()
    except Exception as e:
        logging.error(e)
    finally:
        if connect.is_connected():
            cursor.close()
            connect.close()
            logging.info('[MySQL] Conexão fechada')


def insert_pokemon_habilidades():
    connect = database.get_connection_mysql_db()
    connect.database = config('MYSQL_DATABASE')
    delete = 'DELETE FROM pokemon_habilidades'
    insert = 'INSERT INTO pokemon_habilidades(pokemon_id, attack, defense, speed) VALUES( %s, %s, %s, %s)'
    try:
        logging.info('Insert tabela pokemon_habilidades')
        with open('db/pokemon_habilidade.csv', mode='r', newline='', encoding='utf8') as f:
            habilidades = []
            reader = csv.reader(f)
            for row in reader:
                pokemon_id = int(row[0])
                attack = int(row[1])
                defense = int(row[2])
                speed = int(row[3])
                habilidade = [pokemon_id, attack, defense, speed]
                habilidades.append(habilidade)
        with connect.cursor() as cursor:
            cursor.execute(delete)
            cursor.executemany(insert, habilidades)
            connect.commit()
    except Exception:
        raise Exception('Erro ao inserir na table pokemon_habilidades')
    finally:
        if connect.is_connected():
            cursor.close()
            connect.close()
            logging.info('[MySQL] Conexão fechada')
