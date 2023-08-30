class City:
    def __init__(self, name, population, gold):
        self.name = name
        self.gold = gold
        self.population = population

    def add_stuff(self, gold, population):
        self.gold += gold
        self.population += population

    def plunder(self, gold, people):
        print(f"{self.name} plundered! {gold} gold stolen, {people} citizens killed.")
        if self.gold - gold == 0 or self.population - people == 0:
            print(f"{self.name} has been wiped off the map!")
            return True
        self.gold -= gold
        self.population -= people

    def prosper(self, gold):
        self.gold += gold
        return True


command = input()

cities = {}
while not command == 'Sail':
    name, population, gold = command.split('||')
    gold = int(gold)
    population = int(population)
    if name not in cities:
        cities[name] = City(name, population, gold)
    else:
        cities[name].add_stuff(gold, population)

    command = input()

command = input()

while command != 'End':
    command = command.split('=>')
    if command[0] == 'Plunder':
        town, people, gold = command[1], int(command[2]), int(command[3])
        if cities[town].plunder(gold, people):
            del cities[town]
    elif command[0] == 'Prosper':
        town, gold = command[1], int(command[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
            command = input()
            continue
        if cities[town].prosper(gold):
            print(f"{gold} gold added to the city treasury. {town} now has {cities[town].gold} gold.")

    command = input()

if cities:
    print(f'Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:')
    for town, values in cities.items():
        print(f'{town} -> Population: {values.population} citizens, Gold: {values.gold} kg')
else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")
