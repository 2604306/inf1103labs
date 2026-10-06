import json
import os


# Default inventory with at least 3 products
inventory = [
    {
        "id": "P001",
        "name": "Laptop",
        "price": 1200.00,
        "stock": 15
    },
    {
        "id": "P002",
        "name": "Mouse",
        "price": 25.50,
        "stock": 40
    },
    {
        "id": "P003",
        "name": "Keyboard",
        "price": 45.00,
        "stock": 25
    }
]


def load_inventory():
    global inventory

    if os.path.exists("inventory.json"):
        print("inventory.json found.")

        try:
            with open("inventory.json", "r") as file:
                inventory = json.load(file)

            print("Inventory loaded successfully.")

        except json.JSONDecodeError:
            print("Error reading inventory.json.")
            print("Starting with default inventory.")

    else:
        print("inventory.json not found.")
        print("Starting with default inventory.")


def save_inventory():
    with open("inventory.json", "w") as file:
        json.dump(inventory, file, indent=4)

    print("Inventory saved successfully to inventory.json.")


def display_all():
    print("\nCurrent Inventory")
    print("------------------------------------------------")

    if len(inventory) == 0:
        print("Inventory is empty.")
    else:
        for product in inventory:
            print(
                f"ID: {product['id']} | "
                f"Name: {product['name']} | "
                f"Price: ${product['price']:.2f} | "
                f"Stock: {product['stock']}"
            )

    print("------------------------------------------------")


def add_product():
    print("\nAdd New Product")

    product_id = input("Product ID: ").strip().upper()

    for product in inventory:
        if product["id"] == product_id:
            print("Product ID already exists.")
            return

    product_name = input("Product Name: ").strip()

    while True:
        try:
            price = float(input("Price: "))

            if price < 0:
                print("Price cannot be negative.")
            else:
                break

        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            stock = int(input("Stock Quantity: "))

            if stock < 0:
                print("Stock cannot be negative.")
            else:
                break

        except ValueError:
            print("Please enter a whole number.")

    new_product = {
        "id": product_id,
        "name": product_name,
        "price": price,
        "stock": stock
    }

    inventory.append(new_product)

    print("Product added successfully!")


def update_stock():
    print("\nUpdate Stock")

    product_id = input("Enter Product ID: ").strip().upper()

    for product in inventory:
        if product["id"] == product_id:
            print("Product Found:")
            print(f"Name: {product['name']}")
            print(f"Current Stock: {product['stock']}")

            while True:
                try:
                    new_stock = int(input("New Stock Quantity: "))

                    if new_stock < 0:
                        print("Stock cannot be negative.")
                    else:
                        break

                except ValueError:
                    print("Please enter a whole number.")

            product["stock"] = new_stock

            print("Stock updated successfully!")
            return

    print("Product not found.")


def search_product():
    print("\nSearch Product")

    product_id = input("Enter Product ID: ").strip().upper()

    for product in inventory:
        if product["id"] == product_id:
            print("Product Found")
            print("------------------------------------------------")
            print(f"ID: {product['id']}")
            print(f"Name: {product['name']}")
            print(f"Price: ${product['price']:.2f}")
            print(f"Stock: {product['stock']}")
            print("------------------------------------------------")
            return

    print("Product not found.")


def display_menu():
    print("\n----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")


def main():
    print("========================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("========================================")

    load_inventory()

    while True:
        display_menu()

        option = input("Enter option: ").strip()

        if option == "1":
            display_all()

        elif option == "2":
            add_product()

        elif option == "3":
            update_stock()

        elif option == "4":
            search_product()

        elif option == "5":
            print("Saving inventory...")
            save_inventory()

        elif option == "6":
            print("Saving inventory before exit...")
            save_inventory()

            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            break

        else:
            print("Invalid option. Please select 1 to 6.")


if __name__ == "__main__":
    main()
