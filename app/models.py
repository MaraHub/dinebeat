from app import db
from datetime import datetime
from flask_login import (LoginManager, UserMixin, login_required,
                           login_user, current_user, logout_user)

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    username = db.Column(db.String(64), index=True, unique=True)
    created_ts = db.Column(db.DateTime)
    menu = db.relationship('Menu', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % (self.email)


class MenuVote(db.Model):
    event_code = db.Column(db.Integer,primary_key=True)
    voter = db.Column(db.Unicode,primary_key=True)
    submenu = db.Column(db.Unicode,primary_key=True)
    item = db.Column(db.Unicode,primary_key=True)
    created_ts = db.Column(db.DateTime,primary_key=True)
    #user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # def __init__(self,event_code,voter,submenu,item):
    #     self.event_code = event_code
    #     self.voter = voter
    #     self.submenu = submenu
    #     self.item = item


class Menu(db.Model):
    event_code = db.Column(db.Integer,primary_key=True)
    event_desc=db.Column(db.Unicode,primary_key=True)
    submenu = db.Column(db.Unicode,primary_key=True)
    dish = db.Column(db.Unicode,primary_key=True)
    dish_desc = db.Column(db.Unicode)
    created_ts = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # def __init__(self,event_code,submenu,dish,dish_desc,image_path):
    #     self.event_code = event_code
    #     self.submenu = submenu
    #     self.dish = dish
    #     self.dish_desc = dish_desc
    #     self.image_path = image_path


    # def __init__(self,event_code,submenu,dish,dish_desc,image_path):
    #     self.event_code = event_code
    #     self.submenu = submenu
    #     self.dish = dish
    #     self.dish_desc = dish_desc
    #     self.image_path = image_path
