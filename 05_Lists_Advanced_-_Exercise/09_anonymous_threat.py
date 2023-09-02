def merge(start_index: int, end_index: int) -> list:
    """
    This function concatenate all elements from the startIndex to the endIndex included.
    :param start_index: The start index of the manipulated strings
    :param end_index:  The end index of the manipulated strings
    :return: The concatenated expression inserted into the original string
    """
    element = ""
    if end_index + 1 > len(data_array):
        end_index = len(data_array) - 1
    if start_index < 0:
        start_index = 0
    for index in range(start_index, end_index + 1):
        element += data_array[index]
    for index in range(end_index, start_index - 1, -1):
        data_array.pop(index)
    data_array.insert(start_index, element)
    return data_array


def divide(index: int, partitions: int) -> list:
    """
    This function divides the element at the given index into several small
substrings with equal length. The count of the substrings is equal to the given partitions.
If the string cannot be exactly divided into the given partitions, all partitions except the last
are with equal lengths the last one is the longest.
    :param index: The index of the parameter to be manipulated
    :param partitions: How many splits to be performed
    :return: Original edited list
    """
    element = data_array.pop(index)
    len_of_element = len(element)
    start_range = 0
    end_range = (len_of_element // partitions)
    increment = end_range
    while partitions > 0:
        new_element = ""
        for i in range(start_range, end_range):
            new_element += element[i]

        if partitions == 1:
            start_range = end_range
            new_element += element[start_range:]
        else:
            start_range = end_range
            end_range += increment

        data_array.insert(index, new_element)
        index += 1
        partitions -= 1
    return data_array


data_array = input().split()
while True:
    command = input()
    if command == "3:1":
        break
    command = command.split()
    function, arg_1, arg_2 = command
    if function == "merge":
        merge(int(arg_1), int(arg_2))
    elif function == "divide":
        divide(int(arg_1), int(arg_2))

print(*data_array)
