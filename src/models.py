from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
import datetime
from flask import current_app
from flask_bcrypt import Bcrypt
import pyotp
import os

db = SQLAlchemy()
bcrypt = Bcrypt()


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # automatically increments
    email = db.Column(db.String(255), unique=True, nullable=False) # duplicate emails not allowed
    password = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    pfp_url = db.Column(db.String(255))
    joindate = db.Column(db.DateTime, nullable=False)
    is_2fa_enabled = db.Column(db.Boolean, nullable = False, default = False)
    token_2fa = db.Column(db.String, unique=True)

    def __init__(self, email, name, password):
        default_pfp_dir = os.path.join(current_app.config['IMG_URL'], "profiles/default_profile.png")

        self.email = email
        self.name = name
        self.password = bcrypt.generate_password_hash(password)
        self.joindate = datetime.datetime.now()
        self.token_2fa = pyotp.random_base32()
        self.pfp_url = default_pfp_dir
        

    def __repr__(self):
        return '<Email: %r>' % self.email
    
    def get_2fa_url(self):
        return pyotp.totp.TOTP(self.token_2fa).provisioning_uri(name = self.email, issuer_name=current_app.name)
    
    def verify_otp(self, user_otp):
        totp = pyotp.parse_uri(self.get_2fa_url())
        return totp.verify(user_otp)

## Item model
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True) # item ids, automatically increments
    name = db.Column(db.String(255), nullable = False)
    type = db.Column(db.String(255), nullable = False) # food, hygiene
    quantity = db.Column(db.Integer, nullable = False)
    stockdate = db.Column(db.Date, nullable = False) # item last stock/restock date
    expdate = db.Column(db.Date, nullable = False) # item expiration date
    image = db.Column(db.String(255), nullable = True) # path to picture of item (optional)

    ## Item model functions
    def __repr__(self):
        return '<ID: %r>' % self.id
    
    def serialize(self):
        return { 
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'quantity': self.quantity,
            'stockdate': self.stockdate,
            'expdate': self.expdate,
            'image': self.image
        }
    
    def addItem(item_name, item_quantity, item_stockdate, item_expdate, item_type, item_img = None):
        new_item = Item(name = item_name, quantity = item_quantity, stockdate = item_stockdate, expdate = item_expdate, type = item_type, image = item_img)
        db.session.add(new_item)

        db.session.commit()

    def getAllItems():
        return Item.query.all()

    def getItemByID(item_id):
        return Item.query.filter_by(id = item_id).first()
        #return Item.query.all()
    
    def deleteItemByID(item_id):
        if(Item.getItemByID(id) is None):
            return False
        else:
            Item.query.filter(id = item_id).delete()
            db.session.commit()
            return True

    def setItemQuantity(item_id, quantity):
        if(Item.getItemByID(id) is None):
            print("Item " + str(id) + " not found!")
            return False
        else:
            update_item = Item.query.filter_by(id = item_id).first()
            update_item.quantity = quantity
            db.session.commit()
            return True

    def editItem(item_id, new_name = None, 
                 new_quantity = None,
                 new_stockdate = None, new_expdate = None):
        if(Item.getItemByID(id) is None):
            print("Item " + str(id) + " not found!")
            return False
        else:
            update_item = Item.query.filter_by(id = item_id).first()
            # update all parameters
            if(new_name is not None): update_item.name = new_name
            if(new_quantity is not None): update_item.quantity = new_quantity
            if(new_stockdate is not None): update_item.stockdate = new_stockdate
            if(new_expdate is not None): update_item.expdate = new_expdate
            db.session.commit()
            return True   

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True) # order id, automatically increments
    orderdate = db.Column(db.Date, nullable = False)
    deliverydate = db.Column(db.Date, nullable = True) # can be empty until delivery
    status = db.Column(db.String(255), nullable = False)
    items = db.Column(db.String(255), nullable = False) # stored as comma separated item IDs
    recipient_name = db.Column(db.String(255), nullable = False)
    recipient_address = db.Column(db.String(255), nullable = False)

