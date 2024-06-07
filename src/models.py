from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
import datetime

db = SQLAlchemy()
## Item model
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True) # item ids, automatically increments
    name = db.Column(db.String(255), nullable = False)
    quantity = db.Column(db.Integer, nullable = False)
    stockdate = db.Column(db.Date, nullable = False) # item last stock/restock date
    expdate = db.Column(db.Date, nullable = False) # item expiration date

    def __repr__(self):
        return '<User %r>' % self.username
    
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # automatically increments
    email = db.Column(db.String(255), unique=True) # duplicate emails not allowed
    password = db.Column(db.String(255))
    name = db.Column(db.String(255))




## Item model functions
def addItem(item_name, item_quantity, item_stockdate, item_expdate):
    new_item = Item(name = item_name, quantity = item_quantity, stockdate = item_stockdate, expdate = item_expdate)
    db.session.add(new_item)

    db.session.commit()

def getAllItems():
    return Item.query.all()

def getItemByID(item_id):
    return Item.query.filter_by(id = item_id).first()
    #return Item.query.all()
  
def deleteItemByID(item_id):
    if(getItemByID(id) is None):
        return False
    else:
        Item.query.filter(id = item_id).delete()
        db.session.commit()
        return True
    
def setItemQuantity(item_id, quantity):
    if(getItemByID(id) is None):
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
    if(getItemByID(id) is None):
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
    
