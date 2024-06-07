from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable = False)
    quantity = db.Column(db.Integer, nullable = False)
    stockdate = db.Column(db.Date, nullable = False)
    expdate = db.Column(db.Date, nullable = False)

    def __repr__(self):
        return '<User %r>' % self.username
    
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