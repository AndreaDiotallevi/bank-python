import pytest
from src.transaction import Transaction

def test_format():
    transaction = Transaction(1000, 0, 1000)

    assert transaction.format() == "01/01/2020 || 1000.00 || || 1000.00"
    