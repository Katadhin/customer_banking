# Pseudocode for customer banking file

# Instructions:

# You'll be creating a customer banking system that allows users to 
# calculate and track interest earned on savings and CD accounts. 
# By running this application, users will be able to enter their savings and 
# CD account information, see the interest earned, and view the updated balances 
# after a specified number of months.

# Create Accounts.py file
# Create a class called Account
# Create a constructor method that takes in balance and interest
# Create a set balance method that takes in balance and sets the balance
# Create a set interest method that takes in interest and sets the interest
# Create a get balance method that returns the balance
# Create a get interest method that returns the interest

# Create a Menu
# Create a function that displays the menu


# Populate Account with information

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