class Zoo:
    __animal = 0 # attribute is private for the class, Class Attribute

    def __init__(self, name):
        self.name = name
        self.mammal = []
        self.bird = []
        self.fish = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammal.append(name)
        elif species == "fish":
            self.fish.append(name)
        elif species == "bird":
            self.bird.append(name)
        zoo.__animal += 1

    def get_info(self, species):
        if species == "mammal":
            print(f"{species.capitalize()}s in {self.name}: {', '.join(self.mammal)}")
            print(f"Total animals: {zoo.__animal}")
        elif species == "bird":
            print(f"{species.capitalize()}s in {self.name}: {', '.join(self.bird)}\n"
                  f"Total animals: {zoo.__animal}")
        elif species == "fish":
            print(f"{species.capitalize()}es in {self.name}: {', '.join(self.fish)}\n"
                  f"Total animals: {zoo.__animal}")


zoo_name = input()
zoo = Zoo(zoo_name)
animals_in_zoo = int(input())
for _ in range(animals_in_zoo):
    animal_details = input()
    animal_details = animal_details.split()
    animal_species = animal_details[0]
    animal_name = animal_details[1]
    zoo.add_animal(animal_species, animal_name)

species = input()
zoo.get_info(species)
