command = input()

dict1 = {}

while not command.isdigit():
    key, value = command.split('-')
    dict1[key] = value
    command = input()

for _ in range(int(command)):
    name = input()
    if name in dict1:
        print(f'{name} -> {dict1[name]}')
    else:
        print(f'Contact {name} does not exist.')
