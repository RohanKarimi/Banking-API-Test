import unittest
import HtmlTestRunner
import pytest
import pytest_html
from BankingAPI import BankingAPI

class TestBankingAPI(unittest.TestCase):
    def setUp(self):
        self.api = BankingAPI()

    def test_create_account(self):
        success, message = self.api.create_user('user1', 'John Doe')
        self.assertTrue(success)
        self.assertEqual(message, 'User created successfully.')

        success, message = self.api.create_account('user1', 'account1')
        self.assertTrue(success)
        self.assertEqual(message, 'Account created successfully.')

    def test_create_duplicate_account(self):
        success, message = self.api.create_user('user1', 'John Doe')
        self.assertTrue(success)
        self.assertEqual(message, 'User created successfully.')

        success, message = self.api.create_account('user1', 'account1')
        self.assertTrue(success)
        self.assertEqual(message, 'Account created successfully.')

        success, message = self.api.create_account('user1', 'account1')
        self.assertFalse(success)
        self.assertEqual(message, 'Account already exists for the user.')

    def test_delete_account(self):
        success, message = self.api.create_user('user1', 'John Doe')
        self.assertTrue(success)
        self.assertEqual(message, 'User created successfully.')

        success, message = self.api.create_account('user1', 'account1')
        self.assertTrue(success)
        self.assertEqual(message, 'Account created successfully.')

        success, message = self.api.delete_account('user1', 'account1')
        self.assertTrue(success)
        self.assertEqual(message, 'Account deleted successfully.')

    def test_delete_nonexistent_account(self):
        success, message = self.api.create_user('user1', 'John Doe')
        self.assertTrue(success)
        self.assertEqual(message, 'User created successfully.')

        success, message = self.api.delete_account('user1', 'account1')
        self.assertFalse(success)
        self.assertEqual(message, 'Account does not exist for the user.')

    def test_create_and_delete_multiple_accounts(self):
        success, message = self.api.create_user('user1', 'John Doe')
        self.assertTrue(success)
        self.assertEqual(message, 'User created successfully.')

        success, message = self.api.create_account('user1', 'account1')
        self.assertTrue(success)
        self.assertEqual(message, 'Account created successfully.')

        success, message = self.api.create_account('user1', 'account2')
        self.assertTrue(success)
        self.assertEqual(message, 'Account created successfully.')

        success, message = self.api.create_account('user1', 'account3')
        self.assertTrue(success)
        self.assertEqual(message, 'Account created successfully.')

        success, message = self.api.delete_account('user1', 'account2')
        self.assertTrue(success)
        self.assertEqual(message, 'Account deleted successfully.')

    def test_deposit(self):
        success, message = self.api.create_user('user1', 'John Doe')
        self.assertTrue(success)
        self.assertEqual(message, 'User created successfully.')

        success, message = self.api.create_account('user1', 'account1')
        self.assertTrue(success)
        self.assertEqual(message, 'Account created successfully.')

        success, message = self.api.deposit('user1', 'account1', 500)
        self.assertTrue(success)
        self.assertEqual(message, 'Amount deposited successfully.')

    def test_withdraw(self):
        success, message = self.api.create_user('user1', 'John Doe')
        self.assertTrue(success)
        self.assertEqual(message, 'User created successfully.')

        success, message = self.api.create_account('user1', 'account1')
        self.assertTrue(success)
        self.assertEqual(message, 'Account created successfully.')

        success, message = self.api.deposit('user1', 'account1', 1000)
        self.assertTrue(success)
        self.assertEqual(message, 'Amount deposited successfully.')

        success, message = self.api.withdraw('user1', 'account1', 500)
        self.assertTrue(success)
        self.assertEqual(message, 'Amount withdrawn successfully.')


    def test_withdraw_exceeds_balance_limit(self):
        success, message = self.api.create_user('user1', 'John Doe')
        self.assertTrue(success)
        self.assertEqual(message, 'User created successfully.')

        success, message = self.api.create_account('user1', 'account1')
        self.assertTrue(success)
        self.assertEqual(message, 'Account created successfully.')

        success, message = self.api.deposit('user1', 'account1', 1000)
        self.assertTrue(success)
        self.assertEqual(message, 'Amount deposited successfully.')

        success, message = self.api.withdraw('user1', 'account1', 1100)
        self.assertFalse(success)
        self.assertEqual(message, 'Withdrawal amount exceeds the limit.')

    def test_withdraw_from_nonexistent_account(self):
        success, message = self.api.create_user('user1', 'John Doe')
        self.assertTrue(success)
        self.assertEqual(message, 'User created successfully.')

        success, message = self.api.withdraw('user1', 'account1', 500)
        self.assertFalse(success)
        self.assertEqual(message, 'Account does not exist for the user.')


    def test_withdraw_limit_ninety_percentage(self):
        success, message = self.api.create_user('user1', 'John Doe')
        self.assertTrue(success)
        self.assertEqual(message, 'User created successfully.')

        success, message = self.api.create_account('user1', 'account1')
        self.assertTrue(success)
        self.assertEqual(message, 'Account created successfully.')

        # Deposit $500 into the account
        success, message = self.api.deposit('user1', 'account1', 500)
        self.assertTrue(success)
        self.assertEqual(message, 'Amount deposited successfully.')

        # Verify initial balance is $500
        balance = self.api.get_balance('user1', 'account1')
        self.assertEqual(balance, 500)

        # Attempt to withdraw $450 (less than 90% of the balance)
        success, message = self.api.withdraw('user1', 'account1', 450)
        self.assertTrue(success)
        self.assertEqual(message, 'Amount withdrawn successfully.')

        # Verify new balance is $50
        balance = self.api.get_balance('user1', 'account1')
        self.assertEqual(balance, 50)

        # Attempt to withdraw $55 (more than 90% of the balance)
        success, message = self.api.withdraw('user1', 'account1', 55)
        self.assertFalse(success)
        self.assertEqual(message, 'Withdrawal amount exceeds the maximum limit.')

        # Verify balance remains $50
        balance = self.api.get_balance('user1', 'account1')
        self.assertEqual(balance, 50)

    def test_deposit_limit(self):
        success, message = self.api.create_user('user1', 'John Doe')
        self.assertTrue(success)
        self.assertEqual(message, 'User created successfully.')

        success, message = self.api.create_account('user1', 'account1')
        self.assertTrue(success)
        self.assertEqual(message, 'Account created successfully.')

        # Verify initial balance is $0
        balance = self.api.get_balance('user1', 'account1')
        self.assertEqual(balance, 0)

        # Deposit $5,000 into the account
        success, message = self.api.deposit('user1', 'account1', 5000)
        self.assertTrue(success)
        self.assertEqual(message, 'Amount deposited successfully.')

        # Verify new balance is $5,000
        balance = self.api.get_balance('user1', 'account1')
        self.assertEqual(balance, 5000)

        # Attempt to deposit $12,000 (exceeds the limit)
        success, message = self.api.deposit('user1', 'account1', 12000)
        self.assertFalse(success)
        self.assertEqual(message, 'Deposit amount exceeds the maximum limit.')

        # Verify balance remains $5,000
        balance = self.api.get_balance('user1', 'account1')
        self.assertEqual(balance, 5000)


    def tearDown(self):
        self.api = None
        print("Test completed....")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../API/BankingAPI'))
