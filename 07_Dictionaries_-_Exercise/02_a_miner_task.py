command = input()

dict1 = {}
while command != 'stop':
    key = command
    value = int(input())
    if key not in dict1:
        dict1[key] = value
    else:
        dict1[key] += value

    command = input()
for key, value in dict1.items():
    print(f'{key} -> {value}')
