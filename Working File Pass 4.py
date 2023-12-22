from Accounts1 import Account

def create_account(balance, apr, months): # Add months parameter
    """Create an account and calculate interest and new balance."""
    account = Account(balance, apr) # Create an instance of the `Account` class and pass in the balance and interest parameters.
    interest_earned = account.calculate_interest(months) # Calculate interest earned
    account.update_balance(interest_earned) # Update the account balance by adding the interest earned
    return account.balance, interest_earned # Return the updated balance and interest earned.

def get_account_info():
    """Get account information from the user."""
    balance = float(input("Enter starting balance: $")) # Get the starting balance from the user
    apr = float(input("Enter annual interest rate (in %): ")) # Get the APR from the user
    months = int(input("Enter number of months: ")) # Get the number of months from the user
    return balance, apr, months # Return the balance, APR, and months

def menu():
    """Display the menu and return the user's choice."""
    print("\nWelcome to the First United Bank of Python") # Display the menu
    print("\n1. Create a Savings Account") # Display the menu
    print("2. Create a CD Account") # Display the menu
    print("3. Exit") # Display the menu
    return int(input("\nEnter your choice: ")) # Return the user's choice

def login(users):
    """Simple login function."""
    username = input("Enter your username (default = user1):  ")
    password = input("Enter your password: (default = password1): ")
    if username in users and users[username] == password:
        print("Login successful!")
        return True
    else:
        print("Login failed. Invalid username or password.")
        return False

def main():
    users = {"user1": "password1", "user2": "password2"}  # Basic user data

    if login(users):
        while True:
            choice = menu()

            if choice in [1, 2]:
                balance, apr, months = get_account_info()
                new_balance, interest_earned = create_account(balance, apr, months)
                print(f"\nInterest Earned: ${interest_earned:.2f}")
                print(f"Future Balance: ${new_balance:.2f}")
        
                another_operation = input("\nWould you like to open another account? (yes/no): ").lower()
                if another_operation != 'yes':
                    print("\nThank you for using the First United Bank of Python.")
                    break

            elif choice == 3:
                print("\nThank you for using the First United Bank of Python.")
                break

            else:
                print("\nInvalid choice. Please try again.")
    else:
        print("\nAccess denied.")

if __name__ == "__main__":
    main()
