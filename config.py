import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False


class Config:
    APP_NAME = "Test Google Login"
    SECRET_KEY = os.environ.get("SECRET_KEY") or "somethingsecret"
class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, "test.db")
class ProdConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, "prod.db")

config = {
"dev": DevConfig,
"prod": ProdConfig,
"default": DevConfig
}
