lines_count = int(input())

total_sum = 0
for each_line in range(lines_count):
    chrtr = input()
    chrtr_value = ord(chrtr)
    total_sum += chrtr_value

print(f"The sum equals: {total_sum}")
