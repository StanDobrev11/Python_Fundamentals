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


storage = Storage(4)
storage.add_product("apple")
storage.add_product("banana")
storage.add_product("potato")
storage.add_product("tomato")
storage.add_product("bread")
print(storage.get_products())
