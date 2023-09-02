def split_secret_msg(message: list) -> tuple:
    """
    Takes every digit from the string and transfer it to new lists. After this operation, we have two lists of items -
a numbers list and a non-numbers list.
    :param message: original list
    :return: two split lists
    """
    num_list = list(filter(lambda x: x.isdigit(), message))
    num_list = list(map(int, num_list))
    non_num_list = list(filter(lambda x: not x.isdigit(), message))
    return num_list, non_num_list


def take_or_skip(num_list: list) -> tuple:
    """
    Takes every digit in the numbers list and split it up into a take list and a skip list. In the take list, we
keep all digits at an even index. In the skip list, we keep all digits at an odd index.
    :param num_list: list of numbers
    :return: two modified lists
    """
    even_list = [num_list[index] for index in range(len(num_list)) if index % 2 == 0]
    odd_list = [num_list[index] for index in range(len(num_list)) if index % 2 == 1]
    return even_list, odd_list


secret_msg = list(input())
number_list, non_number_list = split_secret_msg(secret_msg)
take_list, skip_list = take_or_skip(number_list)

is_finished = False
result_string = ""
while not is_finished:
    for index, number in enumerate(number_list):
        if number_list[-1] == number:
            is_finished = True

        if index % 2 == 0:
            if number == 0:
                continue
            else:
                for i in range(number):
                    if len(non_number_list) == 0:
                        break
                    result_string += non_number_list.pop(0)
        elif index % 2 == 1:
            if number == 0:
                continue
            else:
                for i in range(number):
                    if len(non_number_list) == 0:
                        break
                    non_number_list.pop(0)

print(result_string)
