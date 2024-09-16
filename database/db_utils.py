import sqlite3

def create_table_if_not_exists(db_filename):
    try:
        # Connect to SQLite database
        conn = sqlite3.connect(db_filename)
        cursor = conn.cursor()

        # Create table if it does not exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS servers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                hostname TEXT NOT NULL,
                ip TEXT NOT NULL
            )
        ''')

        # Commit changes and close connection
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Failed to create table: {str(e)}")
