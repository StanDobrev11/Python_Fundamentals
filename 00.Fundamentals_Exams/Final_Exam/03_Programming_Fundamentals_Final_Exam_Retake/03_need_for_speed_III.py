class Car:
    def __init__(self, make, miles, fuel_quantity):
        self.make = make
        self.miles = int(miles)
        self.fuel_quantity = int(fuel_quantity)
        self.fuel_capacity = 75
        self.min_milage = 10000
        self.max_milage = 100000

    def drive(self, distance, fuel):
        if self.fuel_quantity < int(fuel):
            print("Not enough fuel to make that ride")
            return

        self.miles += int(distance)
        self.fuel_quantity -= int(fuel)
        print(f"{self.make} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

        if self.miles >= self.max_milage:
            del garage[self.make]
            print(f"Time to sell the {self.make}!")

    def revert(self, kilometers):
        if self.miles - int(kilometers) < self.min_milage:
            self.miles = self.min_milage
        else:
            self.miles -= int(kilometers)
            print(f"{self.make} mileage decreased by {kilometers} kilometers")

    def refuel(self, qtity):
        if self.fuel_quantity + int(qtity) > self.fuel_capacity:
            qtity = self.fuel_capacity - self.fuel_quantity
            self.fuel_quantity = self.fuel_capacity
        else:
            self.fuel_quantity += int(qtity)

        print(f"{self.make} refueled with {qtity} liters")


number_of_cars = int(input())

garage = {}

for _ in range(number_of_cars):
    make_model, milage, fuel = input().split('|')
    garage[make_model] = Car(make_model, milage, fuel)

command_line = input()

while command_line != 'Stop':
    command, *rest = command_line.split(' : ')

    if command == 'Drive':
        make, distance, fuel = rest
        garage[make].drive(distance, fuel)

    elif command == 'Refuel':
        make, fuel = rest
        garage[make].refuel(fuel)

    elif command == "Revert":
        make, km = rest
        garage[make].revert(km)

    command_line = input()

for name, values in garage.items():
    print(f"{name} -> Mileage: {values.miles} kms, Fuel in the tank: {values.fuel_quantity} lt.")
