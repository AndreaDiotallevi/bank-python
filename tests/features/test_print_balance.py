import pytest
from freezegun import freeze_time
from src.account import Account

@freeze_time("2020-01-01")

def test_feature_print_empty_balance(capsys):
    account = Account()
    account.print_statement()
    out, err = capsys.readouterr()

    assert  out == "date || credit || debit || balance\n"

# def test_feature_print_balance_after_one_deposit(capsys):
#     account = Account()
#     account.deposit(1000)
#     account.print_statement()
#     out, err = capsys.readouterr()

#     assert  out == "date || credit || debit || balance\n01/01/2020 || 1000.00 || || 1000.00\n"
