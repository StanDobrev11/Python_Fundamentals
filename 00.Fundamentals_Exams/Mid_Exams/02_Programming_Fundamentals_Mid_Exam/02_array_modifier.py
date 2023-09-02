def swap(swap_list, ind_1, ind_2):
    swap_list[ind_1], swap_list[ind_2] = swap_list[ind_2], swap_list[ind_1]
    return swap_list


def multiply(multiply_list, ind_1, ind_2):
    result = multiply_list[ind_1] * multiply_list[ind_2]
    multiply_list[ind_1] = result
    return multiply_list


def decrease(decrease_list):
    return list(map(lambda x: x - 1, decrease_list))


input_string = input()

result_list = list(map(int, input_string.split()))

command = input()
while not command == 'end':
    command = command.split()
    if command[0] == "swap":
        result_list = swap(result_list, int(command[1]), int(command[2]))
    elif command[0] == 'multiply':
        result_list = multiply(result_list, int(command[1]), int(command[2]))
    elif command[0] == 'decrease':
        result_list = decrease(result_list)
    command = input()

result_list = list(map(str, result_list))
print(', '.join(result_list))
