class Inventory:

    def __init__(self, capacity):
        self.__capacity = capacity
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        if self.__capacity < len(self.items):
            self.items.pop()
            return "not enough room in the inventory"

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        capacity_left = self.__capacity - len(self.items)
        return f"Items: {', '.join(self.items)}.\nCapacity left: {capacity_left}"


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
