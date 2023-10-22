numbers = [int(x) for x in input().split()]

command = input()

while command != 'Finish':
    command, *rest = command.split()
    num = int(rest[0])
    if command == "Add":
        numbers.append(num)

    elif command == "Remove":
        if num in numbers:
            numbers.remove(num)

    elif command == "Replace":
        old_value, new_value = [int(x) for x in rest]
        if old_value in numbers:
            idx = numbers.index(num)
            numbers[idx] = new_value

    elif command == "Collapse":
        numbers = [x for x in numbers if x >= num]

    command = input()

print(' '.join(str(x) for x in numbers))

"""
1 4 5 19 1 20 -1 10 5 9 70 -56 9 9
Add 1
Remove 4
Finish

1 20 -1 10
Collapse 8
Finish

5 9 70 -56 9 9
Replace 9 10
Remove 9
Finish

                5 10 70 -56 9
"""