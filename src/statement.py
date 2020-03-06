from src.transaction import Transaction

class Statement():
    HEADER = "date || credit || debit || balance"

    def __init__(self, transaction_class = Transaction):
        self.transactions = []
        self.transaction_class = transaction_class

    def add_transaction(self, credit, debit, balance):
        self.transactions.append(self.transaction_class(credit, debit, balance))
        return self.transactions

    def format_transactions(self):
        formatted_balance = [self.HEADER]
        for transaction in self.transactions:
            formatted_balance.append(transaction.format())
        return "\n".join(formatted_balance)
