# Python Test Question

You are required to implement a banking program using Python.

The program should allow users to create accounts, deposit and withdraw funds, view their balance, and log all transactions.

You can use the following code skeleton as a starting point:

```python
import os
import random
import string
from datetime import datetime


# Implement the log_transaction decorator function


class Account:
    # Implement the Account class


class SavingsAccount(Account):
    # Implement the SavingsAccount class


class CheckingAccount(Account):
    # Implement the CheckingAccount class


class Bank:
    # Implement the Bank class


# Test the implementation
bank = Bank()

while True:
    # Display menu options and get user input


    if choice == 1:
        # Prompt the user to create a new account


    elif choice == 2:
        # Prompt the user to make a deposit


    elif choice == 3:
        # Prompt the user to make a withdrawal


    elif choice == 4:
        # Prompt the user to view the account balance


    elif choice == 5:
        # Exit the program


    print("--------------------")
```

## Your task is to complete the implementation by following these instructions:

1. Implement the `log_transaction` decorator function.

   - The decorator function should log each transaction to a file named `<account_number>.txt` inside a folder named `"transactions"`.
   - The log should include the transaction type, account number, amount, and timestamp in the following format:

   ```text
   [timestamp]: Transaction Type: <transaction_type>, Account Number: <account_number>, Amount: <amount>.
   ```

   - Make sure to create the `"transactions"` folder if it doesn't exist.
   - Append the transaction log to the corresponding account's log file if it exists; otherwise, create a new file.

2. Implement the `Account` class with the required attributes and methods. It should have functionality for depositing and withdrawing funds, as well as retrieving the account balance.

3. Implement the `SavingsAccount` and `CheckingAccount` classes as subclasses of `Account`.

   - `SavingsAccount` should include functionality for earning interest on deposits.
   - `CheckingAccount` should enforce a transaction limit.

4. Implement the `Bank` class with methods for adding accounts, retrieving accounts by account number and password, and getting the total balance across all accounts.

5. Test the implementation by running the program. The program should display a menu with the following options:

   - **Create Account:** Prompts the user to enter a password and confirm password. Then, asks for the account type (savings or checking) and additional details based on the account type. After successful account creation, display the account number to the user.

   - **Deposit:** Prompts the user to enter the account number, password, and deposit amount. If the account is valid, deposit the specified amount into the account and log the transaction.

   - **Withdraw:** Prompts the user to enter the account number, password, and withdrawal amount. If the account is valid and has sufficient funds, withdraw the specified amount from the account and log the transaction.

   - **View Balance:** Prompts the user to enter the account number and password. If the account is valid, display the current account balance.

   - **Exit:** Terminate the program.

6. Ensure to handle errors and display appropriate error messages for invalid inputs, insufficient funds, incorrect passwords, etc.

# Terminal Output

```text
1. Create Account
2. Deposit
3. Withdraw
4. View Balance
5. Exit
Enter choice: 1
Enter password: 123$
Confirm password: 123$
Enter account type (savings/checking): Savings
Account created Successfully, Note Down your Account Number: 9554046419006156
--------------------

1. Create Account
2. Deposit
3. Withdraw
4. View Balance
5. Exit
Enter choice: 1
Enter password: abc$
Confirm password: abc$   
Enter account type (savings/checking): checking
Account created Successfully, Note Down your Account Number: 8211994660922730
--------------------

1. Create Account
2. Deposit
3. Withdraw
4. View Balance
5. Exit
Enter choice: 1
Enter password: 456#
Confirm password: #456
Passwords didn't match. Please try again.

1. Create Account
2. Deposit
3. Withdraw
4. View Balance
5. Exit
Enter choice: 1
Enter password: #456
Confirm password: #456
Enter account type (savings/checking): current
Error: Invalid account type
--------------------

1. Create Account
2. Deposit
3. Withdraw
4. View Balance
5. Exit
Enter choice: 2
Account number: 1234567890123456
Password: 0000
Amount: 1000
Error: Account not found
--------------------

1. Create Account
2. Deposit
3. Withdraw
4. View Balance
5. Exit
Enter choice: 2
Account number: 9554046419006156
Password: 123$
Amount: 1000
Rs.1000.0 Deposited successfully
--------------------

1. Create Account
2. Deposit
3. Withdraw
4. View Balance
5. Exit
Enter choice: 4
Account number: 9554046419006156
Password: 123$
Balance: 1025.0
--------------------

1. Create Account
2. Deposit
3. Withdraw
4. View Balance
5. Exit
Enter choice: 2
Account number: 9554046419006156
Password: 123$
Amount: -500
Error: Invalid amount
--------------------

1. Create Account
2. Deposit
3. Withdraw
4. View Balance
5. Exit
Enter choice: 3
Account number: 9554046419006156
Password: 123$
Amount: 500
Rs.500.0 Withdrawn successfully
--------------------

1. Create Account
2. Deposit
3. Withdraw
4. View Balance
5. Exit
Enter choice: 3  
Account number: 9554046419006156
Password: 123$
Amount: 600
Error: Insufficient Funds
--------------------

1. Create Account
2. Deposit
3. Withdraw
4. View Balance
5. Exit
Enter choice: 3
Account number: 9554046419006156
Password: 123$
Amount: -100
Error: Invalid amount
--------------------

1. Create Account
2. Deposit
3. Withdraw
4. View Balance
5. Exit
Enter choice: 4
Account number: 9554046419006156
Password: #456
Error: Incorrect password
--------------------

1. Create Account
2. Deposit
3. Withdraw
4. View Balance
5. Exit
Enter choice: 4               
Account number: 1234567890123456
Password: 0000
Error: Account not found
--------------------

1. Create Account
2. Deposit
3. Withdraw
4. View Balance
5. Exit
Enter choice: 2
Account number: 9554046419006156
Password: 123$
Amount: 100000
Rs.100000.0 Deposited successfully
--------------------

1. Create Account
2. Deposit
3. Withdraw
4. View Balance
5. Exit
Enter choice: 3
Account number: 9554046419006156
Password: 123$
Amount: 60000
Rs.60000.0 Withdrawn successfully
--------------------

1. Create Account
2. Deposit
3. Withdraw
4. View Balance
5. Exit
Enter choice: 2
Account number: 8211994660922730
Password: abc$
Amount: 100000
Rs.100000.0 Deposited successfully
--------------------

1. Create Account
2. Deposit
3. Withdraw
4. View Balance
5. Exit
Enter choice: 3
Account number: 8211994660922730
Password: abc$
Amount: 60000
Error: Transaction Limit Exceeded
--------------------

1. Create Account
2. Deposit
3. Withdraw
4. View Balance
5. Exit
Enter choice: 8
Invalid choice
--------------------

1. Create Account
2. Deposit
3. Withdraw
4. View Balance
5. Exit
Enter choice: abc
Invalid choice

1. Create Account
2. Deposit
3. Withdraw
4. View Balance
5. Exit
Enter choice: 5
PS C:\Users\LENOVO\OneDrive\Desktop\Python-Development> 
```