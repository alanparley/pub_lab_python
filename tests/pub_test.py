import unittest
from src.pub import Pub
from src.drink import Drink


class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("Ox", 100)
        self.drink_beer = Drink("Beer", 4)

    def test_pub_has_name(self):
        self.assertEqual("Ox", self.pub.name)

    def test_pub_has_cash(self):
        self.assertEqual(100, self.pub.cash)


# def count_drinks(self, drink):
#         return len(self.drink)

    def test_count_drinks(self):
        self.assertEqual(0, self.pub.count_drinks())

    # def add_drinks(self, drink):
    #     self.assertEqual(1, self.pub.drink)

    def test_add_drinks(self):
        self.pub.add_drinks(self.drink_beer) 
        self.assertEqual(1, self.pub.count_drinks())
