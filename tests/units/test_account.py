import pytest
from unittest.mock import MagicMock  
from src.account import Account
from src.statement import Statement

@pytest.fixture
def mock_statement():
    return MagicMock(spec=Statement) 

def test_print_empty_balance(capsys, mock_statement):
    mock_statement.format_transactions.return_value = "date || credit || debit || balance"
    account = Account(mock_statement)
    account.print_statement()
    out, err = capsys.readouterr()

    assert out == "date || credit || debit || balance\n"

def test_deposit_returns_current_balance():
    account = Account()

    assert account.deposit(1000) == 1000

def test_withdraw_returns_current_balance():
    account = Account()
    account.deposit(1000)

    assert account.withdraw(500) == 500
