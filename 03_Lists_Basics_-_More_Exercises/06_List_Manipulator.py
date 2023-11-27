import sys


def exchange(exchange_list, index, arg_3=""):  # [1, 2, 3, 4, 5] , 2 --> [4, 5, 1, 2, 3]
    index = int(index)
    if index < 0 or index not in range(len(exchange_list)):
        return exchange_list, "Invalid index"
    else:
        for _ in range(index + 1):
            exchange_list.append(exchange_list[0])
            exchange_list.pop(0)

        return exchange_list, ""


def maximum(max_list, odd_even, arg_3):  # returns max rightmost index of even/odd element
    max_even_element = -sys.maxsize
    max_odd_element = -sys.maxsize
    max_index = None
    if odd_even == "even":
        for index, element in enumerate(max_list):
            if element % 2 == 0:
                if element >= max_even_element:
                    max_even_element = element
                    max_index = index
    elif odd_even == "odd":
        for index, element in enumerate(max_list):
            if element % 2 == 1:
                if element >= max_odd_element:
                    max_odd_element = element
                    max_index = index
    if max_index is None:
        max_index = "No matches"
    return max_list, max_index


def minimum(min_list, odd_even, arg_3):  # returns min rightmost index of even/odd element
    min_even_element = sys.maxsize
    min_odd_element = sys.maxsize
    min_index = None
    if odd_even == "even":
        for index, element in enumerate(min_list):
            if element % 2 == 0:
                if element <= min_even_element:
                    min_even_element = element
                    min_index = index
    elif odd_even == "odd":
        for index, element in enumerate(min_list):
            if element % 2 == 1:
                if element <= min_odd_element:
                    min_odd_element = element
                    min_index = index
    if min_index is None:
        min_index = "No matches"
    return min_list, min_index


def first(first_list, count, odd_even):  # returns first odd/even elements as pe count
    new_list = []
    count = int(count)
    if count > len(first_list):
        return first_list, "Invalid count"
    if odd_even == "even":
        for item in first_list:
            if item % 2 == 0 and count > 0:
                new_list.append(item)
                count -= 1
    elif odd_even == "odd":
        for item in first_list:
            if item % 2 == 1 and count > 0:
                new_list.append(item)
                count -= 1
    return first_list, new_list


def last(last_list, count, odd_even):  # returns last odd/even elements as pe count
    new_list = []
    count = int(count)
    if count > len(last_list):
        return last_list, "Invalid count"
    last_list.rev()
    if odd_even == "even":
        for item in last_list:
            if item % 2 == 0 and count > 0:
                new_list.append(item)
                count -= 1
    elif odd_even == "odd":
        for item in last_list:
            if item % 2 == 1 and count > 0:
                new_list.append(item)
                count -= 1
    new_list.reverse()
    last_list.rev()

    return last_list, new_list


function_dict = {"exchange": exchange, "max": maximum, "min": minimum, "first": first, "last": last}

initial_list = input()
initial_list = initial_list.split()
initial_list = [int(i) for i in initial_list]
manipulated_list = initial_list.copy()
is_over = False
while not is_over:
    command = input()
    if command == "end":
        is_over = True
        print(manipulated_list)
        break
    else:
        command = command.split()
        command.append("")
        function_name = command[0]
        function_arg_1 = manipulated_list
        function_arg_2 = command[1]
        function_arg_3 = command[2]
        manipulated_list = function_dict[function_name](function_arg_1, function_arg_2, function_arg_3)
        if function_name == "exchange":
            if manipulated_list[1] == "Invalid index":
                print(manipulated_list[1])
            manipulated_list = manipulated_list[0]
            continue
        print(manipulated_list[1])
        manipulated_list = manipulated_list[0]
