import pytest
from datetime import datetime
from src.account import Account

# @pytest.fixture(scope="function", autouse=True)
# def initialize_account_instance():
    # prepare something ahead of all tests
    # print("test")

def test_feature_print_empty_balance(capsys):
    account = Account()
    account.print_statement()
    out, err = capsys.readouterr()

    assert out == "date || credit || debit || balance\n"
    assert err == ""

def test_feature_print_balance_after_two_deposits_and_one_withdraw(capsys):
    date = datetime.now().strftime("%m/%d/%Y")
    account = Account()
    account.deposit(1000)
    account.deposit(2000)
    account.withdraw(500)
    
    account.print_statement()
    out, err = capsys.readouterr()

    transaction1 = f"{date} || 1000.00 || || 1000.00"
    transaction2 = f"{date} || 2000.00 || || 3000.00"
    transaction3 = f"{date} || || 500.00 || 2500.00"

    assert out == f"date || credit || debit || balance\n{transaction3}\n{transaction2}\n{transaction1}\n"
    assert err == ""
