class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def discount(self, percent):
        final_price = self.price - (self.price * percent / 100)
        print("Price after discount =", final_price)

l = Laptop("Dell", 50000)

l.discount(10)