class Config(object):
    DEBUG = False
    TESTING = False
    DB_SERVER = "localhost"
    DB_NAME = "test"
    DB_USER = "postgres"
    DB_PASSWORD = "123456"
    DB_POST = 5432
    SECRET_KEY = "SUSIRA"
class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False
   


class TestingConfig(Config):    
    pass
