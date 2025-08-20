from utils import log_transaction

STOCK_FILE = "data/stock.txt"
customer_data = {}


def load_stock():
    """Load fruit stock from stock.txt into a dictionary"""
    fruits_data = {}
    try:
        with open(STOCK_FILE, "r") as f:
            for line in f:
                fruit, qty, price = line.strip().split(" : ")
                fruits_data[fruit] = {"qty": int(qty), "price": float(price)}
    except FileNotFoundError:
        pass
    return fruits_data


def customer():
    while True:
        print("\nCustomer Console")
        print("1. View Fruit Stock")
        print("2. Add Fruit to the Basket")
        print("3. Billing")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                print("\nVIEW FRUIT STOCK")
                fruits_data = load_stock()

                if not fruits_data:
                    print("⚠️ No stock available.")
                else:
                    print("Fruit     | Qty (kg) | Price (₹)")
                    print("-------------------------------")
                    for fruit, info in fruits_data.items():
                        print(f"{fruit:<10}| {info['qty']:<8} | {info['price']}")

            elif choice == 2:
                print("\nADD FRUIT TO THE BASKET")
                fruits_data = load_stock()

                fruit = input("Enter the fruit name: ").strip().lower()

                if fruit not in fruits_data:
                    print("❌ Fruit not available in stock.")
                    continue

                qty = int(input("Enter the quantity (in kgs): "))

                if qty > fruits_data[fruit]['qty']:
                    print(f"⚠️ Only {fruits_data[fruit]['qty']} kg available.")
                    continue

                if fruit not in customer_data:
                    customer_data[fruit] = {"qty": 0, "price": 0}

                customer_data[fruit]['qty'] += qty
                customer_data[fruit]['price'] += qty * fruits_data[fruit]['price']

                log_transaction(f"Customer added {fruit} : (Qty: {qty}) in basket")
                print("[Transaction logged ✅]")

            elif choice == 3:
                total = 0
                print("\n🧺 Your Basket:")
                if not customer_data:
                    print("Basket is empty.")
                else:
                    for fruit, info in customer_data.items():
                        print(f"{fruit} - Qty: {info['qty']} kg, Price: ₹{info['price']}")
                        total += info['price']
                    print("Total bill is: ₹", total)

            elif choice == 4:
                print("Thank you for using the Fruit Store App! 🙏")
                break

            else:
                print("⚠️ Invalid choice. Please select (1–4).")

        except ValueError:
            print("⚠️ Invalid input. Please enter a number (1–4).")

