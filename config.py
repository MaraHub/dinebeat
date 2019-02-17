import os
basedir = os.path.abspath(os.path.dirname(__file__))




class Config(object):
    APP_NAME = "Test Google Login"
    SECRET_KEY = os.environ.get("SECRET_KEY") or "somethingsecret"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig(Config):
    DEBUG = True
    CLIENT_ID_G = ('1009864485884-1jlblcja4iegmr2r14224kfdmilhnka3.apps.googleusercontent.com')
    CLIENT_SECRET_G = '9xAxEnR_fM8RCPnddIlSAxC9'
    REDIRECT_URI_G = 'https://localhost:5000/google_login'
    REQUEST_AUTHORIZATION_G = 'https://accounts.google.com/o/oauth2/auth'
    TOKEN_URI_G = 'https://accounts.google.com/o/oauth2/token'
    USER_INFO_G = 'https://www.googleapis.com/oauth2/v1/userinfo'
    SCOPE_G = ['https://www.googleapis.com/auth/userinfo.email',
                    'https://www.googleapis.com/auth/userinfo.profile']

class ProdConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, "prod.db")


#
# config = {
# "dev": DevConfig,
# "prod": ProdConfig,
# "default": DevConfig
# }
