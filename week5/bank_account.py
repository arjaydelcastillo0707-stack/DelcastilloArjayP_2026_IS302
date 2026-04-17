# Define the BankAccount class
class BankAccount:
    def __init__(self, account_name, balance):
        self.account_name = account_name
        self.balance = balance

    # Method to add money to the balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} successful.")

    # Method to remove money, with a safety check
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of {amount} successful.")
        else:
            print("Error: Insufficient balance.")

    # Method to check the current balance
    def display_balance(self):
        print(f"Account: {self.account_name} | Current Balance: {self.balance}")

# 1. Create a new account with an initial balance
account = BankAccount("Juan", 5000)

# 2. Perform transactions
account.deposit(1000)    # Balance becomes 6000
account.withdraw(2000)   # Balance becomes 4000
account.display_balance()