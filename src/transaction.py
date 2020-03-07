from datetime import datetime

class Transaction():
    def __init__(self, credit, debit, balance):
        self.credit = credit
        self.debit = debit
        self.balance = balance

    def format(self):
        date = self.__format_date()
        credit = self.__format_decimals(self.credit)
        debit = self.__format_decimals(self.debit)
        balance = self.__format_decimals(self.balance)
        formatted_transaction = f"{date} || {credit} || {debit} || {balance}"
        return formatted_transaction.replace(" 0.00 ", " ")

    def __format_date(self):
        return datetime.now().strftime("%m/%d/%Y")

    def __format_decimals(self, amount):
        return "{0:.2f}".format(amount)
