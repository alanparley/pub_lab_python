class Pub:
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash
        self.drink = []

    def count_drinks(self):
        return len(self.drink)

    def add_drinks(self, drink):
        self.drink.append(drink)

    def sell_drink(self, drink):
        self.drink.remove(drink)
