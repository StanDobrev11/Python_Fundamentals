factor = int(input())
count = int(input())

list_numbers = []
number = 1
while len(list_numbers) < count:
    if number % factor == 0:
        list_numbers.append(number)
    number += 1

print(list_numbers)
