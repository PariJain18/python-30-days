import pytest


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount


# Pytest Tests


def test_deposit():
    account = BankAccount("Pari", 1000)
    account.deposit(500)
    assert account.balance == 1500


def test_withdraw():
    account = BankAccount("Pari", 1000)
    account.withdraw(300)
    assert account.balance == 700


def test_failed_overdraft():
    account = BankAccount("Pari", 1000)

    with pytest.raises(ValueError):
        account.withdraw(1500)

    assert account.balance == 1000
