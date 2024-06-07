from flask import Blueprint, render_template, request, bcrypt, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from models import db, User

login_bp = Blueprint('login_bp', __name__)


# signup functions
# signup form
@login_bp.route('/signup_form', methods=['POST'])
def signup_form():
    return render_template("signup.html")

# signup action
@login_bp.route('signup', methods=['POST'])
def signup():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    # check for duplicate email
    user = User.query.filter_by(email=email).first()
    if(user is not None):
        flash('Email address already in use')
        return redirect(url_for('signup_form'))
    
    new_user = User(email=email, name=name, password=bcrypt.generate_password_hash(password))
    db.session.add(new_user)
    db.session.commit()
    flash('Successfully signed up')
    return redirect(url_for('login_form'))

# login functions
# login form
@login_bp.route('/login_form')
def login_form():
    return render_template("login.html")


# login action
@login_bp.route('login', methods=['POST'])
def login():
    # get form data
    email = request.form.get('email')
    password = request.form.get('password')
    remember = request.form.get('remember')
    # search for a user with the entered email
    user = User.query.filter_by(email=email).first()
    # validate credentials
    if (user) and (bcrypt.check_password_hash(user.password, password)):
        user.authenticated = True
        db.session.add(user)
        db.session.commit()
        login_user(user, remember=remember)
        return redirect(url_for("login_test"))
    flash('Login failed, incorrect username or password.')
    return redirect(url_for("login_form"))

# pages that need a login to view

@login_required
@login_bp.route('log_out', methods=['POST'])
def log_out():
    logout_user()
    return redirect(url_for('index'))

@login_required
@login_bp.route('login_test', methods=['POST'])
def login_test():
    return render_template('login_test.html', username=current_user.name)