from Accounts1 import Account

def create_account(balance, apr, months):
    """Create an account and calculate interest and new balance."""
    account = Account(balance, apr)
    interest_earned = account.calculate_interest(months)
    account.update_balance(interest_earned)
    return account.balance, interest_earned

def get_account_info():
    """Get account information from the user."""
    balance = float(input("Enter starting balance: $"))
    apr = float(input("Enter annual interest rate (in %): "))
    months = int(input("Enter number of months: "))
    return balance, apr, months

def menu():
    """Display the menu and return the user's choice."""
    print("\nWelcome to the First United Bank of Python")
    print("1. Create a Savings Account")
    print("2. Create a CD Account")
    print("3. Exit")
    return int(input("Enter your choice: "))

def main():
    while True:
        choice = menu()

        if choice in [1, 2]:
            balance, apr, months = get_account_info()
            new_balance, interest_earned = create_account(balance, apr, months)
            print(f"\nInterest Earned: ${interest_earned:.2f}")
            print(f"New Balance: ${new_balance:.2f}")

            another_operation = input("\nWould you like to open another account? (yes/no): ").lower()
            if another_operation != 'yes':
                print("\nThank you for using the First United Bank of Python.")
                break

        elif choice == 3:
            print("\nThank you for using the First United Bank of Python.")
            break

        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
