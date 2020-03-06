import pytest
from src.account import Account

def test_print_empty_balance(capsys):
    account = Account()
    account.print_statement()
    out, err = capsys.readouterr()

    assert  out == "date || credit || debit || balance\n"

def test_deposit_returns_current_balance():
    account = Account()

    assert account.deposit(1000) == 1000
