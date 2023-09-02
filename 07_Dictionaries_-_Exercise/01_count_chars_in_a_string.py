line = input().split()


dict1 = {}
for item in line:
    for symbol in item:

        if symbol not in dict1:
            dict1[symbol] = 1
        else:
            dict1[symbol] += 1

for key, value in dict1.items():
    print(f'{key} -> {value}')
