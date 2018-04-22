import os

class Config:
    SECRET_KEY = 'laziness'

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig(Config):
    DEBUG = True


config_options ={"production":ProdConfig,"default":DevConfig}

