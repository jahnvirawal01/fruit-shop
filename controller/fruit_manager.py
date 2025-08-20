from utils import log_transaction

STOCK_FILE = "data/stock.txt"
fruits_data = {}  # shared in-memory data


def load_stock():
    """Load fruit stock from file into dictionary."""
    try:
        with open(STOCK_FILE, "r") as f:
            for line in f:
                fruit, qty, price = line.strip().split(" : ")
                fruits_data[fruit] = {"qty": int(qty), "price": float(price)}
    except FileNotFoundError:
        pass  # no stock file yet


def save_stock():
    """Save fruit stock dictionary into file."""
    with open(STOCK_FILE, "w") as f:
        for fruit, details in fruits_data.items():
            f.write(f"{fruit} : {details['qty']} : {details['price']}\n")


def fruits():
    """Fruit Manager Menu."""
    load_stock()  # always load latest stock at start

    while True:
        print("\n----- Fruit Market Manager -----")
        print("1. Add Fruit Stock")
        print("2. View Fruit Stock")
        print("3. Update Fruit Stock")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                print("\nADD FRUIT STOCK")
                fruit = input("Enter the fruit name: ").strip().lower()

                qty = int(input("Enter the quantity (in kgs): "))
                price = float(input("Enter price (per piece): "))

                if fruit in fruits_data:
                    fruits_data[fruit]["qty"] += qty
                    fruits_data[fruit]["price"] = price
                else:
                    fruits_data[fruit] = {"qty": qty, "price": price}

                save_stock()
                log_transaction(f"Manager added {fruit} (Qty: {qty}, Price: {price})")
                print("[Transaction logged ✅]")

            elif choice == 2:
                print("\nVIEW FRUIT STOCK")
                load_stock()
                print("Fruit      | Qty (kg) | Price (₹)")
                print("-------------------------------")
                for fruit, details in fruits_data.items():
                    print(f"{fruit:<10} | {details['qty']:<7} | {details['price']}")
                print("[Data loaded from stock file]")

            elif choice == 3:
                print("\nUPDATE FRUIT STOCK")
                fruit = input("Enter the fruit name: ").strip().lower()

                if fruit in fruits_data:
                    qty = int(input("Enter the new quantity (in kgs): "))
                    price = float(input("Enter the new price (per piece): "))
                    fruits_data[fruit] = {"qty": qty, "price": price}

                    save_stock()
                    log_transaction(f"Manager updated {fruit} (Qty: {qty}, Price: {price})")
                    print("[Transaction logged ✅]")
                else:
                    print("⚠️ Fruit not found in stock!")

            elif choice == 4:
                print("Thank you for using the Fruit Store App! 🙏")
                break

            else:
                print("⚠️ Invalid choice. Please select (1–4).")

        except ValueError:
            print("⚠️ Invalid input. Please enter a number (1–4).")
