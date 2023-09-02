race_line = input()

race_line = race_line.split()

half_way = int((len(race_line) - 1) / 2)

sum_of_left = 0
for i in range(half_way):
    left_num = int(race_line[i])
    if left_num > 0:
        sum_of_left += left_num
    else:
        sum_of_left -= sum_of_left * 0.2

sum_of_right = 0
for i in range(len(race_line) - 1, half_way, -1):
    right_num = int(race_line[i])
    if right_num > 0:
        sum_of_right += right_num
    else:
        sum_of_right -= sum_of_right * 0.2

print(f"The winner is {'left' if sum_of_left < sum_of_right else 'right'} "
      f"with total time: {sum_of_left if sum_of_left < sum_of_right else sum_of_right :.1f}")
