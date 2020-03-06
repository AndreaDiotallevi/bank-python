import pytest
from unittest.mock import MagicMock  
from src.statement import Statement
from src.transaction import Transaction

@pytest.fixture
def mock_transaction():
    return MagicMock(spec=Transaction) 

def test_add_transaction():
    mock_transaction_class = MagicMock()
    mock_transaction_class.return_value = mock_transaction
    statement = Statement(mock_transaction_class)

    assert statement.add_transaction(0, 1000, 1000) == [mock_transaction]

def test_format_transactions(mock_transaction):
    mock_transaction.format.return_value = "01/01/2020 || 1000.00 || || 1000.00"
    mock_transaction_class = MagicMock()
    mock_transaction_class.return_value = mock_transaction
    statement = Statement(mock_transaction_class)
    statement.add_transaction(0, 1000, 1000)

    assert statement.format_transactions() == "date || credit || debit || balance\n01/01/2020 || 1000.00 || || 1000.00"
