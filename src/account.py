from src.statement import Statement

class Account():
    def __init__(self, statement = Statement()):
        self.balance = 0
        self.statement = statement

    def print_statement(self):
        print(self.statement.format_transactions())

    def deposit(self, amount):
        self.balance += amount
        self.statement.add_transaction(amount, 0, self.balance)
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        self.statement.add_transaction(0, amount, self.balance)
        return self.balance
