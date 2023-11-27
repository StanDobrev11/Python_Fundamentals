num_of_lines = int(input())

plants_list = {}
rating_list = {}
for _ in range(num_of_lines):
    plant, rarity = input().split('<->')
    plants_list[plant] = rarity
    if plant not in rating_list:
        rating_list[plant] = []

command = input()

while command != 'Exhibition':
    command = command.split(': ')
    parameters = [x for x in command[1].split(' - ')]
    plant = parameters[0]
    if plant not in plants_list:
        print('error')
        command = input()
        continue
    if command[0] == 'Rate':
        rating = int(parameters[1])
        rating_list[plant].append(rating)
    elif command[0] == 'Update':
        rarity = parameters[1]
        plants_list[plant] = rarity
    elif command[0] == 'Reset':
        rating_list[plant] = []

    command = input()

print('Plants for the exhibition:')
for plant in plants_list:
    average_rating = 0 if not len(rating_list[plant]) else sum(rating_list[plant]) / len(rating_list[plant])
    print(f'- {plant}; Rarity: {plants_list[plant]}; Rating: {average_rating:.2f}')
