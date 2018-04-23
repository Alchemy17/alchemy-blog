import os

class Config:
    SECRET_KEY = 'laziness'

class ProdConfig(Config):
    pass
class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://alchemy:1012@localhost/post'
    

config_options ={"production":ProdConfig,"default":DevConfig}

