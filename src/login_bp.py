from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app, make_response
from flask_bcrypt import Bcrypt
from flask_login import login_user, login_required, logout_user, current_user
from models import db, User
import werkzeug.exceptions
from werkzeug.utils import secure_filename
import os

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
    
    default_pfp_dir = os.path.join(current_app.config['IMG_URL'], "profiles/default_profile.png")

    new_user = User(email=email, name=name, password=bcrypt.generate_password_hash(password), pfp_url = default_pfp_dir)
    db.session.add(new_user)
    db.session.commit()
    flash('Successfully signed up')
    return redirect(redir + "?login")

# login functions
# login form
@login_bp.route('/login_form')
def login_form():
    return render_template("login_form_test.html")


# login action
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

IMAGE_EXTENSIONS = { 'png', 'jpg', 'jpeg', 'gif', 'webp', 'jfif'}

@login_bp.route('/upload_profile_image', methods=['POST'])
@login_required
def upload_pfp():
    user_page = url_for('interface_bp.account_pg')

    # get image upload directory
    upload_dir = os.path.join(current_app.config['IMG_URL'], "profiles/")
    # check if a file was uploaded
    if 'file' not in request.files:
        flash('Profile image file not uploaded.')
        return redirect(user_page)
    file = request.files['file']
    # check filename isnt empty
    if file.filename == '':
        flash("Empty file name")
        return redirect(user_page)
    # check file is allowed
    if '.' in file.filename: 
        file_extension = file.filename.rsplit('.', 1)[1].lower()
        filename = secure_filename(str(current_user.id) + "." + file_extension)
        if(file_extension in IMAGE_EXTENSIONS):
            try:
                # save file to directory
                path = os.path.join(upload_dir, filename)
                file.save(path)
                current_user.pfp_url = path
                db.session.commit()
            except werkzeug.exceptions.RequestEntityTooLarge:
                # Uploaded file broke file size limit
                flash("Uploaded file too large, max file size is " + current_app.config['MAX_CONTENT_LENGTH'] / (1000000) + " MB")
                return redirect(user_page)
        else:
            # invalid extension
            flash("Invalid file type. Uploaded image must be a PNG, JPEG, GIF, WEBP, or JFIF.")
            return redirect(user_page)
    else:
        # filename has no extension
        flash("Invalid file name.")
        return redirect(user_page)
        
    return redirect(user_page)

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

