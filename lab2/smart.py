#smart inventory auditor

print("Smart inventory auditor")

inventory = 0
failed = 0

while True:
    stock = input("Enter stock to add: ")

    if stock == "quit":
        print("Total inventory:", inventory)
        print("Number of failed/rejected Entries:", failed)
        break

    elif stock.startswith("-") and stock[1:].isdigit():
        print("Negative numbers are not allowed")
        failed += 1

    elif stock.isdigit():
        stock = int(stock)  
        inventory += stock

        if inventory > 500:
            print("Overstock!!")
            break

        else:
            print("Current inventory:", inventory)

    else:
        print("Error, please input an integer value")
        failed += 1

    

    

