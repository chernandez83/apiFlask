class Config:
    pass

class DevelopmentConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:1983@localhost/apiFlask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}