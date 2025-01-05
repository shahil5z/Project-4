import sqlite3
import datetime

# Path to your database
DB_PATH = r'C:\Users\SHAHIL\Downloads\Project\Retail Inventory System\inventory.db'

# Function to add a new product
def add_product(name, category, price, stock_quantity, expiry_date):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO products (name, category, price, stock_quantity, expiry_date) VALUES (?, ?, ?, ?, ?)',
                   (name, category, price, stock_quantity, expiry_date))
    conn.commit()
    conn.close()
    log_action(f"Added new product: {name}")

# Function to update stock quantity
def update_stock(product_id, quantity):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('UPDATE products SET stock_quantity = stock_quantity + ? WHERE product_id = ?',
                   (quantity, product_id))
    conn.commit()
    conn.close()
    log_action(f"Updated stock for product ID {product_id}")

# Function to check product availability
def check_availability(product_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT name, stock_quantity FROM products WHERE product_id = ?', (product_id,))
    product = cursor.fetchone()
    conn.close()
    if product:
        name, stock_quantity = product
        print(f"Product: {name}, Available Stock: {stock_quantity}")
    else:
        print("Product not found.")

# Function to view all products
def view_all_products():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    conn.close()
    print("Product List:")
    for product in products:
        print(product)

# Function to search products by name or category
def search_products(search_term):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE name LIKE ? OR category LIKE ?", ('%' + search_term + '%', '%' + search_term + '%'))
    products = cursor.fetchall()
    conn.close()
    print("Search Results:")
    for product in products:
        print(product)

# Function to log actions in the audit log
def log_action(action):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO audit_log (action, timestamp) VALUES (?, ?)", (action, timestamp))
    conn.commit()
    conn.close()

# Function to view audit log
def view_audit_log():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM audit_log")
    logs = cursor.fetchall()
    conn.close()
    print("Audit Log:")
    for log in logs:
        print(log)
