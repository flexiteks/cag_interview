from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class Config:
    """Base config."""
    SECRET_KEY = environ.get('SECRET_KEY')
    FLASK_DEBUG = environ.get('FLASK_DEBUG')
    PROPAGATE_EXCEPTIONS = environ.get('PROPAGATE_EXCEPTIONS')
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL')

class ProdConfig(Config):
    FLASK_DEBUG = 'production'
    DEBUG = False
    TESTING = False

class DevConfig(Config):
    FLASK_DEBUG = 'development'
    DEBUG = True
    TESTING = True