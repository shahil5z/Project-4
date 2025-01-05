from inventory import add_product, update_stock, check_availability, view_all_products, search_products, view_audit_log

# Main Menu
def main_menu():
    while True:
        print("\n=== Retail Inventory Management ===")
        print("1. Add New Product")
        print("2. Update Stock")
        print("3. Check Product Availability")
        print("4. View All Products")
        print("5. Search Products")
        print("6. View Audit Log")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter product name: ")
            category = input("Enter category: ")
            price = float(input("Enter price: "))
            stock_quantity = int(input("Enter stock quantity: "))
            expiry_date = input("Enter expiry date (YYYY-MM-DD): ")
            add_product(name, category, price, stock_quantity, expiry_date)
        elif choice == "2":
            product_id = int(input("Enter Product ID: "))
            quantity = int(input("Enter quantity to add: "))
            update_stock(product_id, quantity)
        elif choice == "3":
            product_id = int(input("Enter Product ID: "))
            check_availability(product_id)
        elif choice == "4":
            view_all_products()
        elif choice == "5":
            search_term = input("Enter product name or category to search: ")
            search_products(search_term)
        elif choice == "6":
            view_audit_log()
        elif choice == "7":
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main menu
if __name__ == "__main__":
    main_menu()
