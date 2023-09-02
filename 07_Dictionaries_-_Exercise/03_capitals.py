keys = input().split(', ')
values = input().split(', ')


dict1 = {keys[idx]:values[idx] for idx in range(len(keys))}


for key, value in dict1.items():
    print(f'{key} -> {value}')
