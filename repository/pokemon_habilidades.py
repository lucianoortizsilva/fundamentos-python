import logging
from decouple import config

from repository import database


############################################
# https://realpython.com/python-mysql/
############################################
class PokemonHabilidadesRepository:

    def __init__(self):
        self.database_name = config('MYSQL_DATABASE')

    def find_all_habilidades(self):
        connect = database.get_connection_mysql_db()
        connect.database = self.database_name
        habilidades = []
        try:
            select = "SELECT * FROM pokemon_habilidades"
            with connect.cursor() as cursor:
                cursor.execute(select)
                result = cursor.fetchall()
                for row in result:
                    pokemonID = int(row[0])
                    ataque = int(row[1])
                    defesa = int(row[2])
                    velocidade = int(row[3])
                    obj = dict({'pokemonID': pokemonID,
                                'ataque': ataque,
                                'defesa': defesa,
                                'velocidade': velocidade})
                    habilidades.append(obj)
            return habilidades
        except Exception as e:
            logging.error(e)
        finally:
            if connect.is_connected():
                cursor.close()
                connect.close()
                logging.info('[MySQL] Conexão fechada')
