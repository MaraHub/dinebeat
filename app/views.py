from flask import Flask,render_template,request,jsonify,redirect, url_for,session
from app import app,db
import json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_
#import pandas as pd
from collections import defaultdict
from sqlalchemy.inspection import inspect
import random
import os
from werkzeug.utils import secure_filename
from flask_login import LoginManager, login_required, login_user, \
    logout_user, current_user, UserMixin
from requests_oauthlib import OAuth2Session
from requests.exceptions import HTTPError
import datetime
from .models import User,Menu,MenuVote
import pandas as pd
from sqlalchemy import create_engine
from collections import OrderedDict
#######################################################
############### Main Page ##########################
#######################################################
@app.route('/')
def mainpage():
    return render_template('mainpage_2.html')

@app.route('/')
def epikoinwnia():
    return render_template('epikoinwnia.html')

#################################################
########## Menu Submition ######################
#################################################
#@app.route('/submit_menu/<username>')
@app.route('/submit_menu/')
@login_required
def submit_menu(username=None):
    return render_template('submit_menu.html',username=current_user.username)
    #return render_template('submit_menu.html')

@app.route('/test_form/')
#@login_required
def test_form():

    return render_template('test_form.html')




@app.route('/receiver2',methods=['POST','GET'])
def receiver2():
    if request.method=='POST':
        print("hello from Receiver2")

        session['dish_starter'] = json.loads(request.form['dish_starter'])
        session['desc_starter'] = json.loads(request.form['desc_starter'])
        session['dish_main'] = json.loads(request.form['dish_main'])
        session['desc_main'] = json.loads(request.form['desc_main'])
        session['dish_desserts'] = json.loads(request.form['dish_desserts'])
        session['desc_desserts'] = json.loads(request.form['desc_desserts'])
        session['drinks'] = json.loads(request.form['drinks'])
        session['desc_drinks'] = json.loads(request.form['desc_drinks'])
        session['event_desc'] = json.loads(request.form['event_desc'])[0]['value']

        return jsonify(dict(redirect=url_for('submit_menu_confirmation')))


@app.route('/submit_menu_confirmation')
def submit_menu_confirmation():
    print('hello from confirmation')

    return render_template('sbmt_menu_cnfrm_page.html',
    event_desc=session.get('event_desc',None),
    starter = session.get('dish_starter',None),
    starter_desc = session.get('desc_starter',None),
    main=session.get('dish_main',None),main_desc = session['desc_main'],
    desserts=session['dish_desserts'],desserts_desc = session['desc_desserts'],
    drinks=session['drinks'],drinks_desc=session['desc_drinks'])


@app.route('/change_input')
def change_input():
    return render_template('change_menu_input.html',
    event_desc=session.get('event_desc',None),
    starter = session.get('dish_starter',None),
    starter_desc = session.get('desc_starter',None),
    main=session.get('dish_main',None),main_desc = session['desc_main'],
    desserts=session['dish_desserts'],desserts_desc = session['desc_desserts'],
    drinks=session['drinks'],drinks_desc=session['desc_drinks'])


@app.route('/display_event_code')
def display_event_code():
    #while User.query.filter_by(email=email).first()
    event_code = random.randint(100000,1000000)
    event_desc = session['event_desc']
    dish_starter = session['dish_starter']
    desc_starter = session['desc_starter']
    dish_main = session['dish_main']
    desc_main = session['desc_main']
    dish_desserts = session['dish_desserts']
    desc_desserts = session['desc_desserts']
    drinks = session['drinks']
    desc_drinks = session['desc_drinks']
    u = current_user
    menu = Menu()
    g=0
    for dish in dish_starter:
        if dish['value'] :

            new_entry = Menu(event_code=event_code,
                            event_desc=event_desc,
                              submenu='starter',
                              dish=dish['value'],
                              dish_desc=desc_starter[g]['value'],
                              created_ts=datetime.datetime.utcnow(),
                              author=u)
            db.session.add(new_entry)
            #db.session.commit()
        g+=1
    g=0
    for dish in dish_main:
        if  dish['value']:
            new_entry = Menu(event_code=event_code,
            event_desc=event_desc,
                          submenu='main',
                          dish=dish['value'],
                          dish_desc=desc_main[g]['value'],
                          created_ts=datetime.datetime.utcnow(),
                          author=u)
            db.session.add(new_entry)        #db.session.commit()
        g+=1
    g=0
    for dish in dish_desserts:
        if  dish['value']:
            new_entry = Menu(event_code=event_code,
            event_desc=event_desc,
                          submenu='desserts',
                          dish=dish['value'],
                          dish_desc=desc_desserts[g]['value'],
                          created_ts=datetime.datetime.utcnow(),
                          author=u)
            db.session.add(new_entry)        #db.session.commit()
        g+=1
    g=0
    for dish in drinks:
        if  dish['value']:
            new_entry = Menu(event_code=event_code,
            event_desc=event_desc,
                          submenu='drinks',
                          dish=dish['value'],
                          dish_desc=desc_drinks[g]['value'],
                      created_ts=datetime.datetime.utcnow(),
                          author=u)
        #db.session.commit()
            db.session.add(new_entry)
        g+=1
    db.session.commit()


    return render_template('display_event_code.html',event_code=event_code,
    event_desc=event_desc)










#######################################################
############### User Login ############################
#######################################################
## Login stuff
login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = "login"
login_manager.session_protection = "strong"
app.secret_key = os.urandom(24)


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
############### Google #################
def get_google_auth(state=None, token=None):
    # If this function has token returns an OAuth2session
    # with token, is state with state
    #if it has nothing it creates a new OAuth2session object
    # with the CLIENT_ID,redirect_uri and scope
    if token:
        return OAuth2Session(app.config['CLIENT_ID_G'], token=token)
    if state:
        return OAuth2Session(
            app.config['CLIENT_ID_G'],
            state=state,
            redirect_uri=app.config['REDIRECT_URI_G'])
    oauth = OAuth2Session(
        app.config['CLIENT_ID_G'],
        redirect_uri=app.config['REDIRECT_URI_G'],
        scope=app.config['SCOPE_G'])
    return oauth



@app.route('/login')
def login():
    if current_user.is_authenticated:
        print("user is authenticated")
        return redirect(url_for('mainpage'))
    print("========= Hello From Login ==========")
    google = get_google_auth()
    auth_url, state = google.authorization_url(
        app.config['REQUEST_AUTHORIZATION_G'],
        access_type='offline',
        prompt='select_account')
    #redirect()
    session['oauth_state'] = state
    print('oauth statte===========================================')
    print(state)
    print(session['oauth_state'])
    return render_template('login.html',google_auth = auth_url)




@app.route('/google_login')
def google_login():
    # Redirect user to home page if already logged in.
    if current_user.is_authenticated:
        print('is authnticated')

    if current_user is not None and current_user.is_authenticated:
        return redirect(url_for('index'))
    if 'error' in request.args:
        if request.args.get('error') == 'access_denied':
            return 'You denied access.'
        return 'Error encountered.'


    else:
        # Execution reaches here when user has
        # successfully authenticated our app.
        try:
            google = get_google_auth(state=session['oauth_state'])
        except KeyError:
            return redirect(url_for('login'))

        try:
            token = google.fetch_token(
                app.config['TOKEN_URI_G'],
                client_secret=app.config['CLIENT_SECRET_G'],
                # Here is where he gets the response
                authorization_response=request.url)

        except HTTPError:
            return 'HTTPError occurred.'
        google = get_google_auth(token=token)
        resp = google.get(app.config['USER_INFO_G'])
        if resp.status_code == 200:
            user_data = resp.json()
            email = user_data['email']
            user = User.query.filter_by(email=email).first()
            if user is None:
                user = User()
                user.email = email
                user.username = user_data['name']
                user.created_ts=datetime.datetime.utcnow()
                db.session.add(user)
                db.session.commit()
            login_user(user)
            print(current_user)
            return redirect(url_for('submit_menu'))
        return 'Could not fetch your information.'



def clean_text(str_):
    if str=='':
        return None
    else:
        return str_.replace("'","").replace("(","").replace(")","").replace(",","")

def get_menu(event_code):

    conn = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], echo=False)
    df = pd.read_sql("select * from menu where event_code=%s and dish <>'';" %event_code,conn)
    data = dict()
    for submenu in df['submenu'].unique():
        for index,dish in df[df.submenu==submenu].reset_index().iterrows():
            if index==0:
                data[submenu] = {index:{
                                   'item':dish.dish,
                                    'item_desc':dish.dish_desc
                                }}

            else:
                data[submenu].update({index:{
                                   'item':dish.dish,
                                    'item_desc':dish.dish_desc
                                }})
    # Creating a sorted dictionary
    data_sorted = OrderedDict()
    for item in app.config['ORDERED_ITEMS']:
        data_sorted[item] = data[item]


    return data_sorted

@app.route('/menu/',methods=['GET','POST'])
def menu():
    if  request.args.get('voter_name'):
        voter = request.args.get('voter_name')
        print("the voter is : "+voter)
        code = request.args.get('event_code_id')
        print("the code is : "+str(code))
        session['voter_vote'] = voter
        session['event_code'] = code
    else:
        voter = session['voter_vote']
        code = session['event_code']

    menu_data = get_menu(code)

    return render_template('menu.html',data=menu_data,translator=app.config['TRANSLATOR'])

@app.route('/post_menu_voted',methods=['POST','GET'])
def post_menu_voted():
    if request.method=='POST':
        print("hello from post_menu_voted")
        session['starters_vote'] = json.loads(request.form['starters'])
        session['main_vote'] = json.loads(request.form['main'])
        session['desserts_vote'] = json.loads(request.form['desserts'])
        session['drinks_vote'] = json.loads(request.form['drinks'])
        return jsonify(dict(redirect=url_for('menu_voted_conf')))


@app.route('/menu_voted_conf')
def menu_voted_conf():
    return render_template('menu_voted_conf.html')

@app.route('/menu_voted_submitted')
def menu_voted_submitted():
    starters = session['starters_vote']
    main = session['main_vote']
    desserts = session['desserts_vote']
    drinks = session['drinks_vote']
    voter = session['voter_vote']
    event_code = session['event_code']
    for item in starters:
        new_entry = MenuVote(event_code=event_code,
                          voter=voter,
                          submenu='starters',
                          item=item.strip(),
                          created_ts=datetime.datetime.utcnow())

        db.session.add(new_entry)


    for item in main:
        new_entry = MenuVote(event_code=event_code,
                          voter=voter,
                          submenu='main',
                          item=item.strip(),
                          created_ts=datetime.datetime.utcnow())

        db.session.add(new_entry)
    for item in desserts:
        new_entry = MenuVote(event_code=event_code,
                          voter=voter,
                          submenu='desserts',
                          item=item.strip(),
                          created_ts=datetime.datetime.utcnow())

        db.session.add(new_entry)
    for item in drinks:
        new_entry = MenuVote(event_code=event_code,
                          voter=voter,
                          submenu='drinks',
                          item=item.strip(),
                          created_ts=datetime.datetime.utcnow())

        db.session.add(new_entry)
        db.session.commit()

    return render_template('menu_voted_thanks.html')
