from unittest import TestCase
from bankAccount import *

testAccount = BankAccount(id='BA123', surname='Smith', first_name='Bob', pin='1234', balance=50000)

class TestBankAccount(TestCase):
    def test_get_id(self):
        self.assertEqual(testAccount.id, 'BA123')

    def test_get_surname(self):
        self.assertEqual(testAccount.surname, 'Smith')

    def test_get_first_name(self):
        self.assertEqual(testAccount.first_name, 'Bob')

    def test_get_balance(self):
        self.assertEqual(testAccount.balance, 50000)

    def test_deposit(self):
        self.assertEqual(testAccount.deposit(100), 50100)

    def test_withdraw(self):
        self.assertEqual(testAccount.withdraw(100), 49900)
