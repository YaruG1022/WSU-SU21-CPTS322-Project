from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app, make_response
from flask_bcrypt import Bcrypt
from flask_login import login_user, login_required, logout_user, current_user
from models import db, User
import werkzeug.exceptions
from werkzeug.utils import secure_filename
import os
import server_utils


login_bp = Blueprint('login_bp', __name__)
bcrypt = Bcrypt()

# signup functions
# signup form
@login_bp.route('/signup_form')
def signup_form():
    return render_template("signup_form_test.html")

# signup action
@login_bp.route('/signup', methods=['POST'])
def signup():
    email = request.form.get('email')
    name = request.form.get('username')
    password = request.form.get('password')
    
    # redirect path
    redir = request.form.get('redir')

    # not all forms filled out
    if not (email and name and password):
        flash('Please fill out all forms before signing up.')
        return redirect(redir + "?signup")
    
    # check for duplicate email
    user = User.query.filter_by(email=email).first()
    if(user is not None):
        flash('Email address already in use')
        return redirect(redir + "?signup")
    

    new_user = User(email=email, name=name, password=password)
    db.session.add(new_user)
    db.session.commit()
    login_user(new_user)

    flash('Successfully signed up')
    return redirect(redir)

# LOGIN FORM
@login_bp.route('/login_form')
def login_form():
    return render_template("login_form_test.html")


# LOGIN ACTION
@login_bp.route('/login', methods=['POST'])
def login():
    # get form data
    email = request.form.get('email')
    password = request.form.get('password')
    remember = request.form.get('remember')

    # redirect path
    redir = request.form.get('redir')

    # search for a user with the entered email
    user = User.query.filter_by(email=email).first()
    # validate credentials
    if (user) and (bcrypt.check_password_hash(user.password, password)):
        user.authenticated = True
        db.session.add(user)
        db.session.commit()
        login_user(user, remember=remember)
        # correct login
        return redirect(redir)
    
    # incorrect login
    flash('Login failed, incorrect username or password.')
    return redirect(redir + "?login")

## OTP
# @login_bp.route('/verify_otp', methods=['POST'])
# def verify_otp():
#    pass

# @login_bp.route('/verify_otp', methods=['POST'])
# def verify_otp():
#    pass



# pages that need a login to view

@login_bp.route('/log_out')
@login_required
def log_out():
    logout_user()
    return redirect(url_for('interface_bp.home_page'))


@login_bp.route('/login_test')
@login_required
def login_test():
    return render_template('login_check.html', username=current_user.name)

## UPLOAD PFP


@login_bp.route('/upload_profile_image', methods=['POST'])
@login_required
def upload_pfp():
    user_page = url_for('interface_bp.account_pg')
    # check if a file was uploaded
    if 'file' not in request.files:
        flash('Profile image file not uploaded.')
        return redirect(user_page)
    file = request.files['file']

    upload_success = server_utils.upload_image(file, "profiles", current_user.id)

    if(upload_success[0] == False):
        flash(upload_success[1])
        return redirect(user_page)
    else:
        current_user.pfp_url = upload_success[1]
        db.session.commit()

    return redirect(user_page)

## UPDATE USER DATA

@login_bp.route('/update_user_data', methods=['POST'])
@login_required
def update_user_data():
    email = request.form.get("email")
    username = request.form.get("username")

    # check username length
    if(len(username) > 48):
        flash("Username too long, must be 48 characters or shorter.")
        response = make_response("Updating user data failed.")
        response.mimetype = "text/plain"
        return response

    current_user.email = email
    current_user.name = username
    db.session.commit()

    flash("User data updated!")
    response = make_response("User credentials updated.")
    response.mimetype = "text/plain"
    return response

@login_bp.route('/update_user_password', methods=['POST'])
@login_required
def update_user_password():
    password = request.form.get("password")

    current_user.password = bcrypt.generate_password_hash(password)
    flash("Password updated!")
    return redirect(url_for('interface_bp.account_pg'))

