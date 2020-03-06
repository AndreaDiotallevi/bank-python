import pytest
from freezegun import freeze_time
from src.transaction import Transaction

@freeze_time("2020-01-01")

def test_format():
    transaction = Transaction(1000, 0, 1000)

    assert transaction.format() == "01/01/2020 || 1000.00 || || 1000.00"
