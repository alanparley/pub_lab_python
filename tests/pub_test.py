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

    

    
