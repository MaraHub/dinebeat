from app import db
from datetime import datetime
from flask_login import (LoginManager, UserMixin, login_required,
                           login_user, current_user, logout_user)

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    created_date = db.Column(db.DateTime)

    def __repr__(self):
        return '<User %r>' % (self.email)


class MenuVote(db.Model):
    event_code = db.Column('event_code',db.Integer,primary_key=True)
    voter = db.Column('voter',db.Unicode,primary_key=True)
    submenu = db.Column('submenu',db.Unicode,primary_key=True)
    item = db.Column('item',db.Unicode,primary_key=True)

    # def __init__(self,event_code,voter,submenu,item):
    #     self.event_code = event_code
    #     self.voter = voter
    #     self.submenu = submenu
    #     self.item = item


class MenuAvailable(db.Model):
    event_code = db.Column('event_code',db.Integer,primary_key=True)
    submenu = db.Column('submenu',db.Unicode,primary_key=True)
    dish = db.Column('dish',db.Unicode,primary_key=True)
    dish_desc = db.Column('dish_desc',db.Unicode)
    image_path = db.Column('image_path',db.Unicode)

    def __init__(self,event_code,submenu,dish,dish_desc,image_path):
        self.event_code = event_code
        self.submenu = submenu
        self.dish = dish
        self.dish_desc = dish_desc
        self.image_path = image_path


    # def __init__(self,event_code,submenu,dish,dish_desc,image_path):
    #     self.event_code = event_code
    #     self.submenu = submenu
    #     self.dish = dish
    #     self.dish_desc = dish_desc
    #     self.image_path = image_path
