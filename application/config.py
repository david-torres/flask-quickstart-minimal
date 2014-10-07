class Config(object):
    DEBUG = False
    SECRET_KEY = ''

class ProductionConfig(Config):
    SECRET_KEY = ''

class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = ''
