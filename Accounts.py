class Account:
    """Creating an Account class with methods"""
    def __init__(self, balance, interest):
        self.balance = balance
        self.interest = interest

    def set_balance(self, balance):
        self.balance = balance

    def set_interest(self, interest):
        self.interest = interest

    def get_balance(self):
        return self.balance

    def get_interest(self):
        return self.interest

    def calculate_interest(self, months):
        monthly_interest = (self.interest / 12) / 100
        return self.balance * monthly_interest * months
