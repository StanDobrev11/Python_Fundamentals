class Vehicle:

    def __init__(self, type_1, model, price, owner=None):
        self.type = type_1
        self.model = model
        self.price = price
        self.owner = owner

    def buy(self, money, owner):
        if money >= self.price and self.owner is None:
            change = money - self.price
            self.owner = owner
            return f"Successfully bought a {self.type}. Change: {change:.2f}"
        elif self.owner is not None:
            return "Car already sold"
        else:
            return "Sorry, not enough money"

    def sell(self):
        if self.owner is not None:
            self.owner = None
        else:
            return "Vehicle has no owner"

    def __repr__(self):
        if self.owner is not None:
            return f"{self.model} {self.type} is owned by: {self.owner}"
        else:
            return f"{self.model} {self.type} is on sale: {self.price}"


vehicle_1 = Vehicle("car", "BMW", 30000)
print(vehicle_1.buy(15000, "Peter"))
print(vehicle_1.buy(35000, "George"))
print(vehicle_1)
vehicle_1.sell()
print(vehicle_1)

vehicle_2 = Vehicle("van", "WW", 45000)
print(vehicle_2.buy(45000, "Sway"))
print(vehicle_1.buy(35000, "George"))
print(vehicle_1, vehicle_2)
vehicle_2.sell()
print(vehicle_1, vehicle_2)
vehicle_1.sell()
print(vehicle_1, vehicle_2)