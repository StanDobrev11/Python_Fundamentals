string = input()

list_animals = string
list_animals = list(list_animals.split(", "))
list_animals.reverse()

if list_animals[0] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    N = list_animals.index("wolf")
    print(f"Oi! Sheep number {N}! You are about to be eaten by a wolf!")
