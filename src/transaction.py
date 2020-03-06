import datetime

class Transaction():
    def __init__(self, debit, credit, balance):
        self.credit = credit
        self.debit = debit
        self.balance = balance

    def format(self):
        return "01/01/2020 || 1000.00 || || 1000.00"

# %d/%m/%Y