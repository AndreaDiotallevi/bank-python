import pytest
from datetime import datetime
from src.account import Account

def test_feature_print_empty_balance(capsys):
    account = Account()
    account.print_statement()
    out, err = capsys.readouterr()

    assert  out == "date || credit || debit || balance\n"

def test_feature_print_balance_after_one_deposit(capsys):
    date = datetime.now().strftime("%m/%d/%Y")
    account = Account()
    account.deposit(1000)
    account.print_statement()
    out, err = capsys.readouterr()

    assert  out == f"date || credit || debit || balance\n{date} || 1000.00 || || 1000.00\n"
