from flask import Blueprint, request, render_template, jsonify, Blueprint, make_response
import sqlite3
from models import db, Item, User

inventory_bp = Blueprint('inventory_bp', __name__, template_folder='templates')

# Route to get inventory data
# @inventory_bp.route('/getInventoryData', methods=['GET'])
# def get_inventory_data():
#     conn = get_db_connection()
#     cursor = conn.execute('SELECT * FROM inventory')
#     rows = cursor.fetchall()
#     conn.close()
    
#     # Convert rows to a list of dictionaries
#     data = [dict(row) for row in rows]
#     columns = ['id', 'name', 'quantity', 'category', 'date_added', 'usable_until', 'status']
    
#     return jsonify({'columns': columns, 'data': data})

@inventory_bp.route('/getInventoryData', methods=['GET'])
def get_inventory_data():
    rows = Item.query.all()

    return jsonify([item.serialize() for item in rows])

# Route to add item
@inventory_bp.route('/addItem', methods=['POST'])
def add_item_route():
    data = request.get_json()
    print(f"Received data: {data}")
    try:
        Item.addItem(data['name'], data['quantity'], data['date_added'], data['usable_until'], data['category'])
        return jsonify({'status': 'success'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@inventory_bp.route('/updateItem', methods=['POST'])
def update_item_route():
    data = request.get_json()
    print(f"Updating item: {data}")
    try:
        Item.update_item(data['id'], data['name'], data['quantity'], data['category'], data['date_added'], data['usable_until'])
        return jsonify({'status': 'success'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

# Route to delete item
@inventory_bp.route('/deleteItem', methods=['POST'])
def delete_item_route():
    data = request.get_json()
    ids = data.get('ids', [])
    print(f"Deleting items with ids: {ids}")
    try:
        for id in ids:
            Item.deleteItemByID(id)
        return jsonify({'status': 'success'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})
