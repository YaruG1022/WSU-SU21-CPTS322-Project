from flask import Blueprint, render_template, request, jsonify, make_response
import sqlite3
import pandas as pd
import io
import logging

# Create a Blueprint for the report
report_bp = Blueprint('report_bp', __name__, template_folder='templates')

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Function to establish a connection to the database
def get_db_connection():
    try:
        # Connect to the single database file 'inventory.db'
        conn = sqlite3.connect('data/inventory.db')
        conn.row_factory = sqlite3.Row
        return conn
    except Exception as e:
        # Log any errors that occur during the connection
        logger.error(f"Error connecting to the database: {e}")
        return None

# Route to render the report page
@report_bp.route('/report')
def report_pg():
    return render_template('report.html')

# Route to fetch report data based on report type
@report_bp.route('/getReportData')
def get_report_data():
    # Get the report type from the request parameters
    report_type = request.args.get('reportType')
    
    # Map the report type to the corresponding table name
    table_map = {
        'inventory': 'inventory',
        'donation': 'donation',
        'recipient order': 'recipient_order'
    }

    # Get the table name based on the report type
    table_name = table_map.get(report_type)

    if not table_name:
        # If the table name is not valid, return an empty response
        return jsonify([])

    conn = get_db_connection()
    
    if conn is None:
        # If the database connection fails, return an error response
        return jsonify({'error': 'Database connection failed'}), 500

    try:
        # Fetch column names
        cursor = conn.cursor()
        cursor.execute(f'PRAGMA table_info({table_name})')
        columns = [col[1] for col in cursor.fetchall()]

        # Query to select all data from the specified table
        query = f'SELECT * FROM {table_name}'
        data = cursor.execute(query).fetchall()
        conn.close()

        # Convert the data to a list of dictionaries
        result = {
            'columns': columns,
            'data': [dict(row) for row in data]
        }
        return jsonify(result)
    except Exception as e:
        # Log any errors that occur during data fetching
        logger.error(f"Error fetching data: {e}")
        return jsonify({'error': 'Failed to fetch data'}), 500
    
# Route to generate and download the report
@report_bp.route('/generateReport', methods=['POST'])
def generate_report():
    # Get the JSON data from the request
    data = request.get_json()
    report_type = data['reportType']
    export_format = data['exportFormat']
    
    # Map the report type to the corresponding table name
    table_map = {
        'inventory': 'inventory',
        'donation': 'donation',
        'recipient order': 'recipient_order'
    }

    # Get the table name based on the report type
    table_name = table_map.get(report_type)

    if not table_name:
        # If the report type is invalid, return an error response
        return jsonify({'error': 'Invalid report type'}), 400

    conn = get_db_connection()
    
    if conn is None:
        # If the database connection fails, return an error response
        return jsonify({'error': 'Database connection failed'}), 500

    try:
        # Query to select all data from the specified table
        query = f'SELECT * FROM {table_name}'
        data = conn.execute(query).fetchall()
        conn.close()

        # Convert the data to a list of dictionaries
        report_data = [dict(row) for row in data]
        df = pd.DataFrame(report_data)
        
        if export_format == 'csv':
            # Export the data to CSV format
            output = io.StringIO()
            df.to_csv(output, index=False)
            response = make_response(output.getvalue())
            response.headers['Content-Disposition'] = 'attachment; filename=report.csv'
            response.headers['Content-Type'] = 'text/csv'
        elif export_format == 'xls':
            # Export the data to XLS format
            output = io.BytesIO()
            with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                df.to_excel(writer, index=False, sheet_name='Report')
            response = make_response(output.getvalue())
            response.headers['Content-Disposition'] = 'attachment; filename=report.xlsx'
            response.headers['Content-Type'] = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        else:
            # If the export format is invalid, return an error response
            return jsonify({'error': 'Invalid format'}), 400
        
        return response
    except Exception as e:
        # Log any errors that occur during report generation
        logger.error(f"Error generating report: {e}")
        return jsonify({'error': 'Failed to generate report'}), 500
