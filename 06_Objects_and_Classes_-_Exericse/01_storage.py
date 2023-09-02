class Storage:
    __storage = []

    def __init__(self, capacity):
        self.capacity = capacity  # capacity is attribute (parameter)

    def add_product(self, product):  # methods (function) with attribute "product"
        Storage.__storage.append(product)
        if len(Storage.__storage) > self.capacity:
            Storage.__storage.pop()

    @staticmethod
    def get_products():
        return Storage.__storage


storage = Storage(2)
storage.add_product("apple")
storage.add_product("banana")
storage.add_product("potato")
storage.add_product("tomato")
storage.add_product("bread")
print(storage.get_products())

storage1 = Storage(7)
storage1.add_product("apple")
storage1.add_product("banana")
storage1.add_product("potato")
storage1.add_product("tomato")
storage1.add_product("bread")
print(storage1.get_products())
