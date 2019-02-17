from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config.DevConfig')
#app.config.from_envvar('DINEBEAT_SETTINGS')
#app.config.from_object("config['dev']")
db = SQLAlchemy(app)

from app import views,models
