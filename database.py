import sqlite3
DATABASE_NAME = "contracts.db"

def create_tables():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contracts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_name TEXT NOT NULL,
            location TEXT NOT NULL,
            value REAL NOT NULL,
            entry_date DATE NOT NULL,
            email TEXT
        )       
    """)
    conn.commit()
    conn.close()
    
def insert_contract(client_name, location, value, entry_date, email):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO contracts (client_name, location, value, entry_date, email)
        VALUES (?, ?, ?, ?, ?)
        """, (client_name, location, value, entry_date, email))
    conn.commit()
    conn.close()

def get_all_contracts():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM contracts
    """)
    results = cursor.fetchall()
    conn.close()
    return results
