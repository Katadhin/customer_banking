# Pseudocode for customer banking file

# Instructions:

# You'll be creating a customer banking system that allows users to 
# calculate and track interest earned on savings and CD accounts. 
# By running this application, users will be able to enter their savings and 
# CD account information, see the interest earned, and view the updated balances 
# after a specified number of months.

# Create Accounts.py file
import Account

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

if user_choice == 1:

    print()





# Populate Account with information
# Create a Savings Account
# Create a CD Account
# Create a function to calculate interest
# Create a function to update balance
# Create a function to update interest
# Create a function to update time
# Create a function to update balance
# Create a function to update interest
# Create a function to update time




# Create Financial Methods
# Interest Rate, Time, Beginning/Ending Calance

# Create Savings Account
# Interest Rate, Time, Beginning/Ending Calance

# Create a CD Account
# Interest Rate, Time, Beginning/Ending Calance (repeating fuction)

# ChatGPT PseudoCode Feedback 
# John John, your pseudocode is looking solid! It lays out a clear structure for your customer banking system. Here are a few suggestions to further refine it and add some necessary details:

# 1. **Enhancing the Account Class**:
#     - Consider adding an account type attribute (Savings or CD) to differentiate between account types.
#     - Add methods for calculating interest. This could be a single method that behaves differently based on account type, or separate methods for each account type.

# 2. **Menu Function**:
#     - Outline the options the user will have in the menu, like creating an account, viewing balances, calculating interest, etc.
#     - Include input handling in the menu to capture user choices.

# 3. **Account Information Input**:
#     - Detail the process for the user to input their account information. This might include prompts for account type, balance, interest rate, and duration.

# 4. **Financial Methods**:
#     - Define the formulas for calculating interest for both savings and CD accounts.
#     - Consider adding a method to update the account balance after adding the interest.

# 5. **Repeating Function for CD Account**:
#     - Clarify how the repeating function for the CD account will work, especially if the interest calculation or term is different from the savings account.

# 6. **Error Handling and Validation**:
#     - Plan for input validation to ensure the user enters valid data (like positive numbers for balance and interest rates).

# 7. **User Feedback**:
#     - Include steps where the program provides feedback to the user, such as confirming actions, displaying calculated interest, and updated balances.

# 8. **Looping the Menu**:
#     - Consider adding a loop around the menu function so the user can perform multiple actions without restarting the program.

# 9. **Exiting the Program**:
#     - Provide an option for the user to exit the program.

# This structure will give you a robust foundation for your banking system. It seems like you're on the right track. Once you start coding, you might find more areas to tweak, which is totally normal. Keep up the great work, and if you hit any snags or need advice on specific parts of the implementation, I'm here to help!