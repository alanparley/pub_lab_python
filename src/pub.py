from src.customer import Customer
from src.drink import Drink


class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def count_drinks(self):
        return len(self.drinks)

    def add_drinks(self, new_drink):
        self.drinks.append(new_drink)

    def remove_drink(self, drink):
        self.drinks.remove(drink)

    def add_money(self, amount_to_add):
        self.till += amount_to_add

    def sells_drink_to_customer(self, customer, input_drink):
        customer.buy_drinks(input_drink)
        customer.spend_cash(input_drink)
        self.remove_drink(input_drink)
        self.add_money(input_drink.price)

        # def sell_drink(self):
        #     self.drink.remove(drink)
