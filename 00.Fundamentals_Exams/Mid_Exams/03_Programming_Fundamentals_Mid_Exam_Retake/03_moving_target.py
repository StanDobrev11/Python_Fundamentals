def shoot(targets, ind, power):
    """
    Shoot the target at the index if it exists by reducing its value by the given power
    (integer value). Remove the target if it is shot.
    A target is considered shot when its value reaches 0.
    """
    if ind in range(len(targets)):
        targets[ind] -= power
        if targets[ind] <= 0:
            targets.pop(ind)

    return targets


def add(targets, ind, val):
    """
    Insert a target with the received value at the received index if it exists.
If not, print: "Invalid placement!"
    """
    if ind in range(len(targets)):
        targets.insert(ind, val)
    else:
        print('Invalid placement!')

    return targets


def strike(target, ind, radius):
    """
    Remove the target at the given index and the ones before and after it depending on the radius.
If any of the indices in the range is invalid, print: "Strike missed!" and skip this command.
    """
    left_part = ind - radius
    right_part = ind + radius
    if left_part in range(len(target)) and right_part in range(len(target)):
        return target[:left_part] + target[right_part + 1:]
    else:
        print("Strike missed!")
        return target

target_sequence = input()
target_sequence = list(map(int, target_sequence.split()))
command = input()
while command != "End":
    command = command.split()
    command, index, value = command[0], int(command[1]), int(command[2])
    if command == "Shoot":
        target_sequence = shoot(target_sequence, index, value)
    elif command == "Add":
        target_sequence = add(target_sequence, index, value)
    elif command == "Strike":
        target_sequence = strike(target_sequence, index, value)
    command = input()

target_sequence = list(map(str, target_sequence))
print("|".join(target_sequence))
