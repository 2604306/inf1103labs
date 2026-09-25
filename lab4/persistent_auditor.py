#persistent_auditor.py

import json
from pathlib import Path

# Store inventory.txt beside this Python file.
FILENAME = Path(__file__).with_name("inventory.txt")

inventory = 0
failed = 0
history = []


def load_inventory():
    try:
        with open(FILENAME, "r") as file:
            data = json.load(file)

        return data["total"], data["history"]

    except FileNotFoundError:
        return 0, []


def save_inventory(total, transactions):
    data = {
        "total": total,
        "history": transactions
    }

    with open(FILENAME, "w") as file:
        json.dump(data, file, indent=4)


def process_delivery(current_total, new_value):
    return current_total + new_value


def calculate_tax(amount):
    return amount * 0.1


def get_valid_input():
    global inventory, failed, history

    while True:
        stock = input("Enter stock to add (or reset / quit): ").strip()

        if stock.lower() == "quit":
            save_inventory(inventory, history)
            print("Inventory saved to inventory.txt")
            break
        
        if stock.lower() == "reset":
            inventory = 0
            history.clear()
            save_inventory(inventory, history)
            print("Stock and transaction history cleared.")
            continue

        try:
            value = int(stock)
        except ValueError:
            print("Error, please input an integer value")
            failed += 1
            continue

        if value < 0:
            print("Negative numbers are not allowed")
            failed += 1
            continue

        inventory = process_delivery(inventory, value)
        history.append(value)

        print("Current inventory:", inventory)


def generate_report(total_units, failed_attempts):
    print("======Summary=====")
    print("Total units:", total_units)
    print("Failed entries this session:", failed_attempts)
    print("Transaction history:", history)
    print("Total Taxes:", calculate_tax(total_units))


def main():
    global inventory, history

    print("Smart inventory auditor")

    inventory, history = load_inventory()
    print("Loaded inventory:", inventory)
    print("Previous transactions:", history)

    get_valid_input()
    generate_report(inventory, failed)


if __name__ == "__main__":
    main()