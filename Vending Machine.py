import time

print("""
██╗   ██╗███████╗███╗   ██╗██████╗ ██╗███╗   ██╗ ██████╗     ███╗   ███╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗███████╗
██║   ██║██╔════╝████╗  ██║██╔══██╗██║████╗  ██║██╔════╝     ████╗ ████║██╔══██╗██╔════╝██║  ██║██║████╗  ██║██╔════╝
██║   ██║█████╗  ██╔██╗ ██║██║  ██║██║██╔██╗ ██║██║  ███╗    ██╔████╔██║███████║██║     ███████║██║██╔██╗ ██║█████╗  
╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██║  ██║██║██║╚██╗██║██║   ██║    ██║╚██╔╝██║██╔══██║██║     ██╔══██║██║██║╚██╗██║██╔══╝  
 ╚████╔╝ ███████╗██║ ╚████║██████╔╝██║██║ ╚████║╚██████╔╝    ██║ ╚═╝ ██║██║  ██║╚██████╗██║  ██║██║██║ ╚████║███████╗
  ╚═══╝  ╚══════╝╚═╝  ╚═══╝╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝
  """)                                                                                                                   


class VendingMachine:
    def __init__(self):
        self.users = {}
        self.beverages = {'A1': {'name': 'Soda', 'price': 1.50, 'quantity': 5},
                          'A2': {'name': 'Water', 'price': 1.00, 'quantity': 5},
                          'A3': {'name': 'Coffee', 'price': 2.00, 'quantity': 5},
                          'A4': {'name': 'Tea', 'price': 1.75, 'quantity': 5},
                          'A5': {'name': 'Energy Drink', 'price': 2.50, 'quantity': 5}}
        self.snacks = {'B1': {'name': 'Chips', 'price': 1.00, 'quantity': 5},
                       'B2': {'name': 'Candy', 'price': 0.75, 'quantity': 5},
                       'B3': {'name': 'Chocolate', 'price': 1.25, 'quantity': 5},
                       'B4': {'name': 'Popcorn', 'price': 1.50, 'quantity': 5},
                       'B5': {'name': 'Pretzels', 'price': 1.25, 'quantity': 5}}
        self.toys = {'C1': {'name': 'Stuffed Animal', 'price': 3.50, 'quantity': 5},
                     'C2': {'name': 'Action Figure', 'price': 2.50, 'quantity': 5},
                     'C3': {'name': 'Board Game', 'price': 5.00, 'quantity': 5},
                     'C4': {'name': 'Puzzle', 'price': 3.00, 'quantity': 5},
                     'C5': {'name': 'Yo-yo', 'price': 1.50, 'quantity': 5}}

        self.categories = {'beverages': self.beverages, 'snacks': self.snacks, 'toys': self.toys}

    def reset(self):
        for category in self.categories.values():
            for item in category.values():
                item['quantity'] = 5

    def display_items(self, category):
        category_styles = {'beverages': '\033[94m', 'snacks': '\033[92m', 'toys': '\033[93m', 'default': '\033[0m'}

        print("\n" + category_styles.get(category, category_styles['default']) +
              f"╔══════════════════════════════════════╗\n"
              f"║     Vending Machine - {category.capitalize()}     ║\n"
              f"╚══════════════════════════════════════╝{category_styles['default']}\n"
              f"Available items:\n"
              f"Code   | Item                 | Price | Quantity\n"
              f"-------+----------------------+-------+---------")
        for code, item in self.categories[category].items():
            print(f"{code.ljust(6)} | {item['name'].ljust(20)} | ${item['price']:.2f} | {item['quantity']}")
        time.sleep(1)

    def add_money_to_wallet(self, username):
        amount = float(input("Enter the amount to add to your wallet: $"))
        if username not in self.users:
            self.users[username] = {'wallet': 0.00, 'transactions': []}
        self.users[username]['wallet'] += amount
        print(f"${amount:.2f} added to your wallet.")
        print(f"Current wallet balance: ${self.users[username]['wallet']:.2f}")

    def process_transaction(self, code, username, category):
        item = self.categories[category].get(code)

        if not item:
            print("Invalid item code. Please try again.")
            return

        if item['quantity'] > 0:
            price = item['price']
            print(f"Selected item: {item['name']}")
            print(f"Price: ${price:.2f}")
            time.sleep(1)

            user_money = self.users[username]['wallet']

            while user_money < price:
                print("Insufficient funds.")
                add_more = input("Do you want to add more money? (y/n): ").lower()
                if add_more == 'y':
                    self.add_money_to_wallet(username)
                    user_money = self.users[username]['wallet']
                    print(f"User's available funds: ${user_money:.2f}")
                else:
                    print("Transaction canceled. Returning to the main menu.")
                    return

            change = user_money - price
            print(f"Transaction successful! Here is your {item['name']}.")
            print(f"Change: ${change:.2f}")
            item['quantity'] -= 1
            self.users[username]['wallet'] -= price
            self.users[username]['transactions'].append(f"Purchase: {item['name']} - ${price:.2f}")
            print(f"Current wallet balance: ${self.users[username]['wallet']:.2f}")

        else:
            print("Item is out of stock. Please choose another item.")

    def display_transaction_history(self, username):
        print(f"Transaction history for {username}:")
        for transaction in self.users.get(username, {}).get('transactions', []):
            print(transaction)

def main():
    vending_machine = VendingMachine()

    # Add money to the wallet as the first step
    username = input("Enter your username: ")
    vending_machine.add_money_to_wallet(username)

    main_menu = {
        '1': 'Display All Items',
        '2': 'Make a Transaction',
        '3': 'Transaction History',
        '4': 'Exit'
    }

    while True:
        print("\nMain Menu:")
        for key, value in main_menu.items():
            print(f"{key}. {value}")

        user_choice = input("Enter your choice: ")

        if user_choice == '1':
            for category in vending_machine.categories.keys():
                vending_machine.display_items(category)
        elif user_choice == '2':
            category = input("Enter the category (Beverages / Snacks / Toys): ").lower()
            vending_machine.display_items(category)
            user_choice_item = input("Enter the code of the item you want to purchase: ").upper()
            vending_machine.process_transaction(user_choice_item, username, category)
        elif user_choice == '3':
            vending_machine.display_transaction_history(username)
        elif user_choice == '4':
            print("Thank you for using the vending machine. Have a great day!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
