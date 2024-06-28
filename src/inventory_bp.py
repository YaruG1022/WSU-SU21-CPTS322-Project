from flask import Blueprint, request, render_template, jsonify, Blueprint, make_response
from models2 import add_item, update_item, delete_items, get_db_connection, update_item_statuses
import sqlite3


inventory_bp = Blueprint('inventory_bp', __name__, template_folder='templates')

# Function to establish a connection to the database
def get_db_connection():
    # Connect to the single database file 'inventory.db'
    conn = sqlite3.connect('data/inventory.db')
    conn.row_factory = sqlite3.Row
    return conn
    
# Existing route for inventory page
@inventory_bp.route('/inventory')
def inventory_pg():
    return render_template('inventory.html')

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
    update_item_statuses()
    conn = get_db_connection()
    cursor = conn.execute('SELECT * FROM inventory')
    rows = cursor.fetchall()
    conn.close()

    # Convert rows to a list of dictionaries
    data = [dict(row) for row in rows]
    columns = ['id', 'name', 'quantity', 'category', 'date_added', 'usable_until', 'status']

    return jsonify({'columns': columns, 'data': data})

# Route to add item
@inventory_bp.route('/addItem', methods=['POST'])
def add_item_route():
    data = request.get_json()
    print(f"Received data: {data}")
    try:
        add_item(data['name'], data['quantity'], data['category'], data['date_added'], data['usable_until'], data['status'])
        return jsonify({'status': 'success'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@inventory_bp.route('/updateItem', methods=['POST'])
def update_item_route():
    data = request.get_json()
    print(f"Updating item: {data}")
    try:
        update_item(data['id'], data['name'], data['quantity'], data['category'], data['date_added'], data['usable_until'], data['status'])
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
        delete_items(ids)
        return jsonify({'status': 'success'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})
