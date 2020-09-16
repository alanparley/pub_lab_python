import unittest
from src.customer import Customer


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Barry", 50)

    def test_customer_has_name(self):
        self.assertEqual("Barry", self.customer.name)

    def test_customer_has_cash(self):
        self.assertEqual(50, self.customer.cash)
