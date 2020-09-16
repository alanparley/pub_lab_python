class Customer:
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash
        self.drinks = []

# make a method for the customer to buy a drink from the pub

    def count_drinks(self):
        return len(self.drinks)

    def buy_drinks(self, new_drink):
        self.drinks.append(new_drink)

    def spend_cash(self, new_drink):
        self.cash -= new_drink.price
