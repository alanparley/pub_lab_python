class Pub:
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash
        self.drinks = []

    def count_drinks(self):
        return len(self.drinks)

    def add_drinks(self, new_drink):
        self.drinks.append(new_drink)

    # def sell_drink(self):
    #     self.drink.remove(drink)