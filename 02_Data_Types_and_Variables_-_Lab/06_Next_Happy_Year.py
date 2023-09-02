number = int(input())
number += 1

is_valid = False
while not is_valid:
    num_string = str(number)
    range_num = len(num_string)
    for num in range(range_num):
        if num_string.count(num_string[num]) > 1:
            number += 1
            break
        else:
            if num == range_num - 1:
                is_valid = True
                print(number)
