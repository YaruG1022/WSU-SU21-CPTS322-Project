
from flask import Flask, render_template, url_for, request, Blueprint
from flask_login import login_user, login_required, logout_user, current_user
from models import db, User

interface_bp = Blueprint("interface_bp", __name__)

@interface_bp.route('/')
@interface_bp.route('/home')
def home_page():
    return render_template("homepage.html", title="Home")

@interface_bp.route('/add_donation')
@login_required
def donation_pg():
    return render_template("donation.html", title="Add Donation")

@interface_bp.route('/inventory')
@login_required
def inventory_pg():
    return render_template("inventory.html", title="Inventory")

@interface_bp.route('/report')
@login_required
def report_pg():
    return render_template("report.html", title="Report")

@interface_bp.route('/transaction')
@login_required
def transaction_pg():
    return render_template("transaction.html", title="Order Now")

@interface_bp.route('/account')
@login_required
def account_pg():
    return render_template("user_account.html", title="Account")

@interface_bp.route('/login_required')
def login_dialogue():
    return render_template("login_required.html", title="Login Required")