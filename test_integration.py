import pytest
from bank_app import transfer, calculate_interest

def test_transfer_success():
    from_balance, to_balance = transfer(5000, 2000, 1000)
    assert from_balance == 4000
    assert to_balance == 3000

def test_transfer_and_interest():
    from_balance, to_balance = transfer(6000, 3000, 2000)
    interest_balance = calculate_interest(to_balance, 10, 1)
    assert round(interest_balance, 2) == 5500.00

def test_transfer_failure():
    with pytest.raises(ValueError):
        transfer(1000, 2000, 5000)
