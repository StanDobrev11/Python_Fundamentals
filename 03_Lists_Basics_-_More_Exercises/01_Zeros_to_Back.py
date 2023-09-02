list_numbers = input()

list_numbers = list_numbers.split(", ")
zero_count = list_numbers.count("0")
for i in range(zero_count):
    list_numbers.remove("0")
    list_numbers.append("0")

for i in range(len(list_numbers)):
    list_numbers[i] = int(list_numbers[i])

print(list_numbers)
