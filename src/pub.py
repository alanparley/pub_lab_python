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

    def sells_drink_to_customer(customer, input_drink)
        




    # def sell_drink(self):
    #     self.drink.remove(drink)