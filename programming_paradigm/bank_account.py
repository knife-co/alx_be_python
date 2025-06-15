class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = account_balance

    def deposit(self, amount):
        deposit = amount + self.account_balance
        return f"Deposited: ${deposit}"
    
    def withdraw(self, amount):
        if self.account_balance >= amount:
            withdraw = self.account_balance - amount
            return f"Withdrew: ${withdraw}"
        else:
            return "Insufficient funds"
    
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")

    

    