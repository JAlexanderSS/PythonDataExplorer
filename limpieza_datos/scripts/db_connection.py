from sqlalchemy import create_engine
from configparser import ConfigParser


def conectar_bd():
    """Conecta a la base de datos usando configuración desde config.ini."""
    config = ConfigParser()
    config.read('config/config.ini')

    db_url = config['database']['url']
    return create_engine(db_url)
