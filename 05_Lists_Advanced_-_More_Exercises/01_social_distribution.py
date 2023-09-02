original_line = input().split(', ')
original_line = list(map(int, original_line))
key_value = int(input())
is_valid = True
modified_line = original_line.copy()
for index, number in enumerate(modified_line):
    if number < key_value:
        diff = key_value - number
        modified_line[index] = key_value
        max_num_index = modified_line.index(max(modified_line))
        if modified_line[max_num_index] > key_value:
            modified_line[max_num_index] -= diff

        if sum(modified_line) != sum(original_line):
            is_valid = False
            break

if is_valid:
    print(modified_line)
else:
    print('No equal distribution possible')
