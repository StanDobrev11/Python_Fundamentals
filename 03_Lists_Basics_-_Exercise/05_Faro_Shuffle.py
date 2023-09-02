string = input()
counts_of_shuffle = int(input())

string_list = string.split()
count_of_items = len(string_list)

first_symbol = string_list[0]
last_symbol = string_list[-1]

string_list.pop(0)
string_list.pop()
halfed = int(len(string_list) / 2)
shuffled_list = string_list

for shuffles in range(counts_of_shuffle):
    first_half = []
    second_half = shuffled_list
    for item in range(halfed):
        first_half.append(shuffled_list[0])
        second_half.pop(0)
    shuffled_list = []
    for item in range(count_of_items - 2):
        if item % 2 == 0:
            shuffled_list.append(second_half[0])
            second_half.pop(0)
        else:
            shuffled_list.append((first_half[0]))
            first_half.pop(0)

shuffled_list.insert(0, first_symbol)
shuffled_list.insert(count_of_items, last_symbol)
print(shuffled_list)
