#Working File Pass 1
# Import Account class from Accounts.py
from Account import Account

# Define the create_savings_account function
def create_savings_account(balance, apr, months): # Add months parameter

    # Create Account instance
    savings_account = Account(balance, apr)

    # Calculate interest earned and update balance

    # Return updated balance and interest earned

# Define the create_cd_account function
def create_cd_account(balance, apr, months):
    # Create Account instance
    cd_account = Account(balance, apr)
    # Calculate interest earned and update balance
    # ...
    # Return updated balance and interest earned

# Define the main function
def main():
    # Prompt user for savings account details
    # ...
    # Call create_savings_account and print results
    # ...
    # Prompt user for CD account details
    # ...
    # Call create_cd_account and print results

# Call the main function if script is run directly
    if __name__ == "__main__":
        main()

# Create a class called Account
class Account:
    # Create a constructor method that takes in balance and interest
    def __init__(self, balance, interest):
        self.balance = balance
        self.interest = interest

    # Create a set balance method that takes in balance and sets the balance
    def set_balance(self, balance):
        self.balance = balance

    # Create a set interest method that takes in interest and sets the interest
    def set_interest(self, interest):
        self.interest = interest

    # Create a get balance method that returns the balance
    def get_balance(self):
        return self.balance

    # Create a get interest method that returns the interest
    def get_interest(self):
        return self.interest
    
# Create a Menu
def menu():
    print()
    print("Welcome to the First United Bank of Python")
    print()
    print("1. Create a Savings Account")
    print("2. Create a CD Account")
    print("3. Exit")
    print()
    
    user_choice = input("Enter your choice: ")  # Add variable declaration for user_choice
    
    return user_choice

menu()

if user_choice == 1
    print()
    print("Create a Savings Account")
    print()
    balance = input("How much would you like to start your account with?    : "
                    apr = input("What is the interest rate for your account?    : ")
                    months = input("How many months will you be saving?    : ")

if user_choice == 2
    print()
    print("Create a CD Account")
    print()
    balance = input("How much would you like to start your account with?    : "
                    apr = input("What is the interest rate for your account?    : ")
                    months = input("How many months will you be saving?
                                   
# Create a function to calculate interest
def calculate_interest(balance, interest, months):
    interest_earned = balance * interest * months / 12
    return interest_earned

# Create a function to update balance
def update_balance(balance, interest_earned):
    balance = balance + interest_earned
    return balance

# Create a function to update interest
def update_interest(interest, interest_earned):
    interest = interest_earned
    return interest

# Create a function to update time
def update_time(months):
    months = months
    return months

# Create a function to update balance
def update_balance(balance, interest_earned):
    balance = balance + interest_earned
    return balance


        


    



