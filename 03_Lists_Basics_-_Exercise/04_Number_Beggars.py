string = input()
number_of_beggars = int(input())

string = string.split(", ")
number_list = []
for each_item in range(len(string)):
    number = int(string[each_item])
    number_list.append(number)

is_valid = False
while not is_valid:
    if len(number_list) % number_of_beggars != 0:
        number_list.append(0)
    else:
        is_valid = True

new_list = []
for each in range(number_of_beggars):
    new_list.append(0)

is_over = False
while not is_over:
    for i in range(number_of_beggars) or not is_over:
        number = number_list[0]
        new_list[i] += number
        number_list.remove(number)
        if len(number_list) == 0:
            is_over = True

print(new_list)
