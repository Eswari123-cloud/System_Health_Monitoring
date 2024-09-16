import pandas as pd
from database.db_utils import create_table_if_not_exists
import sqlite3

def insert_servers_from_csv(csv_filename, db_filename):
    try:
        # Connect to SQLite database
        conn = sqlite3.connect(db_filename)
        cursor = conn.cursor()

        # Read server details from CSV file
        df = pd.read_csv(csv_filename)

        # Insert each row into the database
        for _, row in df.iterrows():
            cursor.execute('''
                INSERT INTO servers (hostname, ip) VALUES (?, ?)
            ''', (row['hostname'], row['ip']))

        # Commit changes and close connection
        conn.commit()
        conn.close()
        print("All servers added successfully.")
    except Exception as e:
        print(f"Failed to insert servers: {str(e)}")

# Create table if not exists
db_filename = 'servers.db'
csv_filename = 'servers.csv'

create_table_if_not_exists(db_filename)
insert_servers_from_csv(csv_filename, db_filename)
