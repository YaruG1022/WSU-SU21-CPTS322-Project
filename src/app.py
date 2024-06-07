from flask import Flask, render_template, request, url_for, make_response, redirect
from markupsafe import escape
from datetime import datetime
from models import *
from flask_login import LoginManager
import os

app = Flask(__name__) # create flask app
# Temporary item database to test in development (./data/test.db)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, "data/test.db")
db.init_app(app)

## Login manager
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
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
    stockdate = datetime.datetime.strptime(request.form['stock-date'], '%Y-%m-%d')
    expdate = datetime.datetime.strptime(request.form['expiry-date'], '%Y-%m-%d')

    addItem(itm_name, itm_quantity, stockdate, expdate)
    resp = make_response(redirect(url_for("success_page")))
    return resp

@app.route("/item_list")
def listitem_test():
    itemlist = getAllItems()
    return render_template("itemlist_test.html", itemlist = itemlist)
    pass

@app.route("/success")
def success_page():
    return render_template("success.html")

