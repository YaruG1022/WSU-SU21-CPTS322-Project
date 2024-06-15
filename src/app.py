from flask import Flask, render_template, request, url_for, make_response, redirect, jsonify
from markupsafe import escape

import secrets
from pathlib import Path

from datetime import datetime
from models import *
from flask_login import LoginManager
import os
from login_bp import login_bp, bcrypt
from interface import interface_bp

app = Flask(__name__) # create flask app
app.register_blueprint(login_bp) # register login blueprint
app.register_blueprint(interface_bp) # register login blueprint

###-------- Initialization --------###
basedir = os.path.abspath(os.path.dirname(__file__))

# Create crucial empty directories if they do not exist
if(os.path.isdir('data') == False):
    os.makedirs(os.path.join(basedir, "data"))
if(os.path.isdir('static/img/profiles') == False or os.path.isdir('static/img/items') == False):
    os.makedirs(os.path.join(basedir, "static/img/profiles"))
    os.makedirs(os.path.join(basedir, "static/img/items"))

# Temporary item database to test in development (./data/test.db)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, "data/test.db")
# image upload base url
app.config['IMG_URL'] = "static/img/"
# max file size
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000

# generate secret key if it doesn't exist
SECRET_FILE_PATH = Path("secret.txt")
try:
    # read secret key from file
    with SECRET_FILE_PATH.open("r") as secret_file:
        app.config['SECRET_KEY'] = secret_file.read()
except FileNotFoundError:
    # File not found, generate secret key file
    with SECRET_FILE_PATH.open("w") as secret_file:
        app.secret_key = secrets.token_urlsafe(32)
        secret_file.write(app.secret_key)

db.init_app(app)
bcrypt.init_app(app)

###-------- Startup --------###

## Login manager
login_manager = LoginManager()
login_manager.login_view = 'interface_bp.login_dialogue'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# database creation function
def create_db():
    with app.app_context():
        db.create_all()
# create database files if they do not exist
create_db()

###-------- Routes --------###


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/item_form")
def additem_test_form():
    return render_template("additem_form.html")

@app.route("/additem_test", methods=['GET', 'POST'])
def additem_test():
    itm_name = escape(request.form['name'])
    itm_quantity = escape(request.form['quantity'])
    itm_type = escape(request.form['type'])
    stockdate = datetime.datetime.strptime(request.form['stock-date'], '%Y-%m-%d')
    expdate = datetime.datetime.strptime(request.form['expiry-date'], '%Y-%m-%d')

    Item.addItem(itm_name, itm_quantity, stockdate, expdate, itm_type)
    resp = make_response(redirect(url_for("success_page")))
    return resp

@app.route("/item_list")
def listitem_test():
    itemlist = Item.getAllItems()
    return render_template("itemlist_test.html", itemlist = itemlist)
    pass

@app.route("/success")
def success_page():
    return render_template("success.html")


@app.route("/item_search_test")
def item_search_test():
    return render_template("item_search_test.html")

@app.route("/search_item", methods=['GET'])
def search_item():
    query = request.args.get('search')
    print(query)
    if(query is None): item_list = Item.query.all()
    elif(query.isdigit()):
        item_list = Item.query.filter_by(id = int(query))
    else:
        item_list = Item.query.filter(Item.name.ilike("%" + query + "%"))
    result = ""
    
    if(item_list is None):
        return "No items found."
    #for itm in item_list:
    #    result += "(#" + str(itm.id) + "): " + itm.name + " x " + str(itm.quantity) + "<br>" 
    
    return jsonify([item.serialize() for item in item_list])
###-----------------------###