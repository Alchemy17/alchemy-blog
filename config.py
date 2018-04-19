class Config:
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://alchemy:1012@localhost/watchlist'


config_options ={"production":ProdConfig,"default":DevConfig}

