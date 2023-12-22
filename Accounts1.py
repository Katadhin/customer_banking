class Account:
    """A class representing a bank account with balance and interest rate."""
    
    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate

    def calculate_interest(self, months):
        """Calculate the interest over a given number of months."""
        monthly_interest_rate = (self.interest_rate / 100) / 12
        interest = self.balance * monthly_interest_rate * months
        return interest

    def update_balance(self, interest):
        """Update the account balance after adding the interest."""
        self.balance += interest

