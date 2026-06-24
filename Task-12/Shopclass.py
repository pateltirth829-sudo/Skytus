class Shop:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def list_products(self):
        print("Products:")
        for p in self.products:
            print(p)

s = Shop()

s.add_product("Laptop")
s.add_product("Mobile")
s.add_product("Mouse")

s.list_products()