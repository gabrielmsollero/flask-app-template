from dotenv import load_dotenv
import os

# Determine the folder of the top-level directory of this project
BASEDIR = os.path.abspath(os.path.dirname(__file__))

# Load variables from .env file.
load_dotenv()

class Config(object):
    # String to be used by ReefDB in mongo client creation.
    # Intentionally left with direct access so that application doesn't
    # start if this value isn't defined.
    DB_CONNECTION_STRING = os.environ['DB_CONNECTION_STRING']
    FLASK_ENV = 'development'
    DEBUG = False
    TESTING = False

class ProductionConfig(Config):
    FLASK_ENV = 'production'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    TEST_DB_NAME = 'TESTDB'
    TEST_DB_API_KEY = 'abcd1234'
