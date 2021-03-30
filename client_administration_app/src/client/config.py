import os


class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite:///clients.db'
    JWT_SECRET = os.environ.get('JWT_SECRET', 'modify-super-secret')


class ProductionConfig(Config):
    DATABASE_URI = os.environ.get('DATABASE_URI',
                                  'sqlite:///../../client.sqlite.prod')


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig,
}