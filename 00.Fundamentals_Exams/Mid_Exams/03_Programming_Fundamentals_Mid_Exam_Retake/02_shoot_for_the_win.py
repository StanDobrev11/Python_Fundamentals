def shoot_target(lst, ind, count):
    if ind in range(len(lst)) and lst[ind] != -1:
        target_value = lst[ind]
        for index in range(len(lst)):
            if lst[index] > target_value:
                lst[index] -= target_value
            elif 0 <= lst[index] <= target_value:
                lst[index] += target_value
        lst[ind] = -1
        count += 1

    # print(lst)
    return lst, count


sequence = input()

sequence = list(map(int, sequence.split()))
targets_shot = 0
command = input()
while command != 'End':
    index = int(command)
    sequence, targets_shot = shoot_target(sequence, index, targets_shot)
    command = input()

print(f"Shot targets: {targets_shot} ->", end=" ")
print(*sequence)
