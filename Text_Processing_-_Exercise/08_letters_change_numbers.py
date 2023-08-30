raw_input = input().split()

total_sum = 0
for item in raw_input:
    initial_letter, end_letter = item[0], item[-1]
    number = int(item[1:-1])

    initial_idx = ord(initial_letter.lower()) - 96
    end_idx = ord(end_letter.lower()) - 96

    if initial_letter.islower():
        number *= initial_idx
    else:
        number /= initial_idx

    if end_letter.islower():
        number += end_idx
    else:
        number -= end_idx

    total_sum += number

print(f"{total_sum:.2f}")
