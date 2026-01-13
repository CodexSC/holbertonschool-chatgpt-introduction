import json

class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        print("Current Balance: ${:.2f}".format(self.balance))

def load_balance(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return data.get('balance', 0.0)
    except FileNotFoundError:
        return 0.0

def save_balance(filename, balance):
    data = {'balance': balance}
    with open(filename, 'w') as file:
        json.dump(data, file)

def main():
    filename = 'checkbook.json'
    cb = Checkbook()
    cb.balance = load_balance(filename)
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            save_balance(filename, cb.balance)
            break
        elif action.lower() == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif action.lower() == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
