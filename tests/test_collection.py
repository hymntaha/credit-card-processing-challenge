import unittest
from collections import deque

from utils.collection import CreditRecordsCollection
from utils.data import Account, Transaction



class CollectionTest(unittest.TestCase):
    def setUp(self):
        self.verified_account = deque([
            Account(
                name='Sam',
                account_number='123456789',
                limit=1000,
                amount=0,
                verified=True)
        ])

        self.unverified_account = deque([
            Account(
                name='Sam',
                account_number='123456789',
                limit=1000,
                amount=0,
                verified=False)
        ])

    def test_initialize_collection(self):
        collection = CreditRecordsCollection(accounts=self.verified_account)
        self.assertEqual(collection.data['Sam']['amount'], 0)
        self.assertEqual(collection.data['Sam']['verified'], True)

    def test_charge_account(self):
        transactions = deque([
            Transaction(
                type='Charge',
                name='Sam',
                amount=500
            )
        ])

        collection = CreditRecordsCollection(accounts=self.verified_account)
        collection.process(transactions=transactions)

        self.assertEqual(collection.data['Sam']['amount'], 500)

    def test_credit_account(self):
        transactions = deque([
            Transaction(
                type='Credit',
                name='Sam',
                amount=500
            )
        ])

        collection = CreditRecordsCollection(accounts=self.verified_account)
        collection.process(transactions=transactions)

        self.assertEqual(collection.data['Sam']['amount'], -500)

    def test_charge_over_limit(self):
        transactions = deque([
            Transaction(
                type='Charge',
                name='Sam',
                amount=2000
            )
        ])

        collection = CreditRecordsCollection(accounts=self.verified_account)
        collection.process(transactions=transactions)

        self.assertEqual(collection.data['Sam']['amount'], 0)

    def test_account_verification_error(self):
        transactions = deque([
            Transaction(
                type='Charge',
                name='Sam',
                amount=500
            )
        ])

        collection = CreditRecordsCollection(accounts=self.unverified_account)
        collection.process(transactions=transactions)

        self.assertEqual(collection.data['Sam']['amount'], 'error')
