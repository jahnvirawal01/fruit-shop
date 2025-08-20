from controller import fruit_manager
from controller import customer

def main_data():
    print("WELCOME TO THE FRUIT MARKET")

    print("1. Manager\n2. Customer")

    choice = int(input("Select a Role: "))

    if choice == 1:
        fruit_manager.fruits()
    elif choice == 2:
        customer.customer()
    else:
        print("Invalid input!")
        main_data()
        
if __name__ == "__main__":
    main_data()