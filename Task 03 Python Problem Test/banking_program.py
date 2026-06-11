import os
import random
import string
from datetime import datetime

# Implement the log_transaction decorator function
def log_transaction(function):

    def inner(*args, **kwargs):

        try:
            result = function(*args, **kwargs)
        except Exception as e:
            raise e

        account = args[0]

        amount = args[1] if len(args) > 1 else 0

        os.makedirs("transactions", exist_ok = True)

        file_path = f"Task 03 Python Problem Test/transactions/{account.account_number}.txt"

        timestamp = datetime.now()

        transaction_type = function.__name__

        with open(file_path, "a") as f:
            f.write(
                f"[{timestamp}]: Transaction Type: {transaction_type}, Account Number: {account.account_number}, Amount: {amount}\n"
            )

        return result
    
    return inner

class Account:
    # Implement the Account class
    def __init__(self, account_number, password):
        self.account_number = account_number
        self.password = password
        self.balance = 0
    
    @log_transaction
    def deposit(self, amount):
        if amount <= 0:
            raise Exception("Invalid amount")
        self.balance += amount
    
    @log_transaction
    def withdraw(self, amount):
        if amount <= 0:
            raise Exception("Invalid amount")
        if amount > self.balance:
            raise Exception("Insufficient Funds")
        self.balance -= amount

    def view_balance(self):
        return self.balance

class SavingsAccount(Account):
    # Implement the SavingsAccount class
    interest_rate = 2.5

    @log_transaction
    def deposit(self, amount):
        if amount <= 0:
            raise Exception("Invalid amount")
        interest = amount * self.interest_rate / 100
        self.balance += amount + interest

class CheckingAccount(Account):
    # Implement the CheckingAccount class
    transaction_limit = 50000

    def withdraw(self, amount):
        if amount > self.transaction_limit:
            raise Exception("Transaction Limit Exceeded")
        
        super().withdraw(amount)

class Bank:
    # Implement the Bank class
    def __init__(self):
        self.accounts = {}

    def generate_account_number(self):
        while True:
            account_number = "".join(random.choices(string.digits, k=16))
            if account_number not in self.accounts:
                return account_number

    def create_account(self, password, account_type):
        account_number = self.generate_account_number()
        if account_type.lower() == "savings":
            account = SavingsAccount(account_number, password)
        elif account_type.lower() == "checking":
            account = CheckingAccount(account_number, password)
        else:
            raise Exception("Invalid account type")
        self.accounts[account_number] = account
        return account_number

    def deposit(self, account_number, password, amount):
        account = self.get_account(account_number, password)
        account.deposit(amount)

    def withdraw(self, account_number, password, amount):
        account = self.get_account(account_number, password)
        account.withdraw(amount)

    def view_balance(self, account_number, password):
        account = self.get_account(account_number, password)
        return account.view_balance()
    
    def get_account(self, account_number, password):
        account = self.accounts.get(account_number)
        if not account:
            raise Exception("Account not found")
        if account.password != password:
            raise Exception("Incorrect password")
        return account
    
    def get_total_balance(self):
        total = 0
        for account in self.accounts.values():
            total += account.balance
        return total

# Test the implementation
bank = Bank()

while True:
    # Display menu options and get user input
    print("\n1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. View Balance")
    print("5. Exit")

    try:
        choice = int(input("Enter choice: "))
    except Exception:
        print("Invalid choice")
        continue

    try:
        if choice == 1:
            # Prompt the user to create a new account
            password = input("Enter password: ")
            confirm = input("Confirm password: ")
            if password != confirm:
                print("Passwords didn't match. Please try again.")
                continue
            account_type = input("Enter account type (savings/checking): ")
            account_number = bank.create_account(password, account_type)
            print("Account created Successfully, Note Down your Account Number:", account_number)

        elif choice == 2:
            # Prompt the user to make a deposit
            account = input("Account number: ")
            password = input("Password: ")
            amount = float(input("Amount: "))
            bank.deposit(account, password, amount)
            print(F"Rs.{amount} Deposited successfully")

        elif choice == 3:
            # Prompt the user to make a withdrawal
            account = input("Account number: ")
            password = input("Password: ")
            amount = float(input("Amount: "))
            bank.withdraw(account, password, amount)
            print(F"Rs.{amount} Withdrawn successfully")        

        elif choice == 4:
            # Prompt the user to view the account balance
            account = input("Account number: ")
            password = input("Password: ")
            print("Balance:", bank.view_balance(account, password))

        elif choice == 5:
            # Exit the program
            break

        else:
            print("Invalid choice")   
    except Exception as e:
        print("Error:", e)

    print("--------------------")