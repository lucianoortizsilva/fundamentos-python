import logging

logging.basicConfig(level=logging.INFO)


def main():
    logging.info('>>> Inicializando app')
    __import__(name="api.pokemon")


# Executar na pasta raiz: pip freeze > requirements.txt
if __name__ == '__main__':
    main()
