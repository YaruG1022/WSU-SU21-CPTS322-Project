from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
import datetime
from flask import current_app

db = SQLAlchemy()
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # automatically increments
    email = db.Column(db.String(255), unique=True) # duplicate emails not allowed
    password = db.Column(db.String(255))
    name = db.Column(db.String(255))
    pfp_url = db.Column(db.String(255))

    def __repr__(self):
        return '<Email: %r>' % self.email

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

