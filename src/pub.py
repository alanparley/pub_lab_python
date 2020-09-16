class Pub:
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash
        self.drink = []

    def add_drinks(self, drink):
        self.drink.append(drink)

    def count_drinks(self, drink):
        return len(self.drink)

    def sell_drink(self, drink):
        self.drink.remove(drink)
