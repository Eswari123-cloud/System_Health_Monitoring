# utils/db.py
import sqlite3
import pandas as pd

def connect_to_db(db_filename):
    """Establish connection to the SQLite database."""
    try:
        conn = sqlite3.connect(db_filename)
        return conn
    except sqlite3.Error as e:
        print(f"Failed to connect to database: {str(e)}")
        return None

def fetch_servers_from_db(conn):
    """Fetch the list of servers from the database."""
    try:
        query = "SELECT hostname FROM servers"
        df = pd.read_sql_query(query, conn)
        servers = df['hostname'].tolist()
        return servers
    except Exception as e:
        print(f"Failed to fetch servers from database: {str(e)}")
        return []

