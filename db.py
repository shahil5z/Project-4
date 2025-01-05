import sqlite3

# Function to connect to the database and create tables if they don't exist
def connect_db():
    conn = sqlite3.connect(r'C:\Users\SHAHIL\Downloads\Project\Retail Inventory System\inventory.db')
    cursor = conn.cursor()

    # Create the products table
    cursor.execute('''CREATE TABLE IF NOT EXISTS products (
        product_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT,
        price REAL NOT NULL,
        stock_quantity INTEGER NOT NULL,
        expiry_date TEXT
    )''')

    # Create the sales table
    cursor.execute('''CREATE TABLE IF NOT EXISTS sales (
        sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id INTEGER,
        quantity_sold INTEGER,
        sale_date TEXT,
        total_price REAL,
        FOREIGN KEY (product_id) REFERENCES products(product_id)
    )''')

    # Create the audit log table
    cursor.execute('''CREATE TABLE IF NOT EXISTS audit_log (
        audit_id INTEGER PRIMARY KEY AUTOINCREMENT,
        action TEXT,
        timestamp TEXT
    )''')

    conn.commit()
    conn.close()

# Call the function to create the database and tables
if __name__ == "__main__":
    connect_db()
