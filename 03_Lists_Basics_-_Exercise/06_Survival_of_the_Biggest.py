string = input()
count_to_remove = int(input())

string_list = string.split()
number_list = []
for item in range(len(string_list)):
    number = int(string_list[item])
    number_list.append(number)

is_valid = False
while not is_valid:
    for each_number in number_list:
        if each_number == min(number_list):
            number_list.remove(each_number)
            count_to_remove -= 1
            if count_to_remove == 0:
                is_valid = True
                break

print(*number_list, sep=", ")
