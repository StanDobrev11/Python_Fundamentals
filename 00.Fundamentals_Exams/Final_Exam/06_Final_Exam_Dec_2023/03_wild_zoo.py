class Animal:
    def __init__(self, name, food_req, area):
        self.name = name
        self.food_req = int(food_req)
        self.area = area


animals = {}
areas = {}

command_line = input()

while command_line != 'EndDay':

    command, *rest = command_line.split(': ')

    if command == 'Add':
        name, food, area = rest[0].split('-')
        if area not in areas:
            areas[area] = []

        if name not in animals:
            animals[name] = Animal(name, int(food), area)
            areas[area].append(name)
        else:
            animals[name].food_req += int(food)

    elif command == "Feed":
        name, food = rest[0].split('-')
        if name in animals:
            animals[name].food_req -= int(food)
            if animals[name].food_req <= 0:
                print(f"{name} was successfully fed")
                animal_area = animals[name].area
                areas[animal_area].remove(name)
                del animals[name]

    command_line = input()

print("Animals:")
for name, values in animals.items():
    print(f" {name} -> {values.food_req}g")

print("Areas with hungry animals:")
for name, animals in areas.items():
    if animals:
        print(f" {name}: {len(animals)}")
