import re

pattern = r'\d+'

line = input()

all_nums = []
while line:
    numbers = re.findall(pattern, line)
    if len(numbers) > 0:
        for num in numbers:
            all_nums.append(num)

    line = input()

print(*all_nums)
