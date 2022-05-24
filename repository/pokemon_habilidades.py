from repository import database


class PokemonHabilidadesRepository:

    def __init__(self):
        self.db = database.get_connection_mysql_db()

    def find_all_habilidades(self):
        print('Buscar habilidades ...')
