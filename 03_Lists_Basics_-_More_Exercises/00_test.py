number = 2

sum_of_nums = 0
while number > 0:
    num = int(number) % 10
    sum_of_nums += num
    number /= 10

print(sum_of_nums)