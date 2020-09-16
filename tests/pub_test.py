import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer


class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("Ox", 100)
        self.drink_beer = Drink("Beer", 4)

    def test_pub_has_name(self):
        self.assertEqual("Ox", self.pub.name)

    def test_pub_has_cash(self):
        self.assertEqual(100, self.pub.till)

    def test_count_drinks(self):
        self.assertEqual(0, self.pub.count_drinks())

    def test_add_drinks(self):
        self.pub.add_drinks(self.drink_beer)
        self.assertEqual(1, self.pub.count_drinks())

    def test_remove_drink(self):
        self.pub.add_drinks(self.drink_beer)
        self.pub.add_drinks(self.drink_beer)
        self.pub.remove_drink(self.drink_beer)
        self.assertEqual(1, self.pub.count_drinks())

    # customer accepts drink and wallet reduces
    # pub checks stock, gives drink, cash increases

# working for time being to help work the code
    def test_pub_sells_drink_to_customer(self):
        self.pub.add_drinks(self.drink_beer)
        customer = Customer("Barry", 50)  # we have customer so now sell drink
        self.pub.sells_drink_to_customer(customer, self.drink_beer)
        # check customer has drink
        # check customer wallet reduces
        # check pub gave drink
        # check cash in till
        self.assertEqual(1, customer.count_drinks())
        # checking property has changed only
        self.assertEqual(46, customer.cash)
        self.assertEqual(0, self.pub.count_drinks())
        self.assertEqual(104, self.pub.till)

    #
