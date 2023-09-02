numbers = input()
string = input()

num_list = numbers.split()
string_list = list(string)

msg_list = []
for number in num_list:
    number = int(number)
    sum_of_nums = 0
    while number > 1:
        num_to_sum = int(number) % 10
        sum_of_nums += num_to_sum
        number /= 10
        if sum_of_nums > len(string_list):
            sum_of_nums -= len(string_list)
    msg_list.append(string_list[sum_of_nums])
    string_list.pop(sum_of_nums)

print("".join(msg_list))
