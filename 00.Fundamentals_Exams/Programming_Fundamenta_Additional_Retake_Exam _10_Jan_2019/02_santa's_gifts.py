number_of_commands = int(input())
house_numbers = [int(x) for x in input().split()]

idx = 0
for _ in range(number_of_commands):
    command = input().split()
    if command[0] == "Forward":
        number_of_steps = int(command[1])
        if idx + number_of_steps in range(len(house_numbers)):
            idx += number_of_steps
            house_numbers.pop(idx)

    elif command[0] == "Back":
        number_of_steps = int(command[1])
        if idx - number_of_steps in range(len(house_numbers)):
            idx -= number_of_steps
            house_numbers.pop(idx)
    elif command[0] == "Gift":
        if int(command[1]) in range(len(house_numbers)):
            idx, house_number = int(command[1]), int(command[2])
            house_numbers.insert(idx, house_number)
    elif command[0] == "Swap":
        first_house, second_house = int(command[1]), int(command[2])
        if first_house in house_numbers and second_house in house_numbers:
            first_house_idx = house_numbers.index(first_house)
            second_house_idx = house_numbers.index(second_house)
            house_numbers[first_house_idx], house_numbers[second_house_idx] = (
                house_numbers[second_house_idx], house_numbers[first_house_idx])

print(f"Position: {idx}")
print(*house_numbers, sep=", ")
