import sqlite3
from datetime import datetime

# Define the function to create the database connection
def get_db_connection():
    conn = sqlite3.connect('data/inventory.db')
    conn.row_factory = sqlite3.Row
    return conn

# Function to add an item to the inventory
def add_item(name, quantity, category, date_added, usable_until, status):
    conn = get_db_connection()
    conn.execute(
        'INSERT INTO inventory (name, quantity, category, date_added, usable_until, status) VALUES (?, ?, ?, ?, ?, ?)',
        (name, quantity, category, date_added, usable_until, status)
    )
    conn.commit()
    conn.close()

def update_item(id, name, quantity, category, date_added, usable_until, status):
    conn = get_db_connection()
    try:
        conn.execute(
            'UPDATE inventory SET name = ?, quantity = ?, category = ?, date_added = ?, usable_until = ?, status = ? WHERE id = ?',
            (name, quantity, category, date_added, usable_until, status, id)
        )
        conn.commit()
        print("Item updated successfully")
    except Exception as e:
        print(f"Error updating item: {e}")
    finally:
        conn.close()

def delete_items(ids):
    conn = get_db_connection()
    try:
        query = 'DELETE FROM inventory WHERE id IN ({})'.format(','.join('?' * len(ids)))
        conn.execute(query, ids)
        conn.commit()
        print("Items deleted successfully")
    except Exception as e:
        print(f"Error deleting items: {e}")
    finally:
        conn.close()



def update_item_statuses():
    conn = get_db_connection()
    today = datetime.today().strftime('%Y-%m-%d')
    cursor = conn.execute('SELECT id, quantity, date_added, usable_until FROM inventory')
    items = cursor.fetchall()

    for item in items:
        status = []
        if item['quantity'] == 0:
            status.append("Unavailable")
        else:
            status.append("Available")
        
        if item['usable_until'] and item['usable_until'] < today:
            status.append("Expired")
        elif item['date_added'] and item['usable_until'] and item['date_added'] > item['usable_until']:
            status.append("Expired")
        else:
            status.append("Usable")
        
        final_status = "\n".join(status)
        conn.execute('UPDATE inventory SET status = ? WHERE id = ?', (final_status, item['id']))

    conn.commit()
    conn.close()
