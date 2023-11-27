class City:
    def __init__(self, name, population, money):
        self.name = name
        self.population = int(population)
        self.money = int(money)
        self.plundered = False

    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self, value):
        if value <= 0:
            self.plundered = True
        self.__population = value

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, value):
        if value <= 0:
            self.plundered = True
        self.__money = value

    def plunder(self, people, treasure):  # "Plunder=>{town}=>{people}=>{gold}"
        print(f"{self.name} plundered! {treasure} gold stolen, {people} citizens killed.")
        self.population -= int(people)
        self.money -= int(treasure)

        if self.plundered:
            print(f"{self.name} has been wiped off the map!")
            del targets[self.name]

    def prosper(self, treasure):
        if int(treasure) < 0:
            print("Gold added cannot be a negative number!")
            return

        self.money += int(treasure)
        print(f"{treasure} gold added to the city treasury. {self.name} now has {self.money} gold.")

    def __str__(self):
        return f"{self.name} -> Population: {self.population} citizens, Gold: {self.money} kg"


command_map = {
    "Plunder": City.plunder,
    "Prosper": City.prosper,
}

targets = {}
target_input = input()

while not target_input == 'Sail':
    city_name, souls, gold = target_input.split('||')
    if city_name not in targets:
        targets[city_name] = City(city_name, souls, gold)
    else:
        targets[city_name].money += int(gold)
        targets[city_name].population += int(souls)

    target_input = input()

command_list = input()

while not command_list == 'End':
    command, target, *rest = command_list.split('=>')

    command_map[command](targets[target], *rest)

    command_list = input()

if not targets:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(targets)} wealthy settlements to go to:")
    print('\n'.join(str(city) for city in targets.values()))
