def average(av_list):
    return sum(av_list) / len(av_list)


def top_5(max_list, value):
    max_list.sort()
    max_list.rev()
    max_list = [num for num in max_list if num > value]
    if len(max_list) > 5:
        max_list = max_list[:5]
    elif len(max_list) == 0:
        return False
    return max_list


input_string = input()
result_list = list(map(int, input_string.split()))

average_value = average(result_list)
result_list = top_5(result_list, average_value)
if result_list:
    result_list = list(map(str, result_list))
    print(' '.join(result_list))
else:
    print('No')
