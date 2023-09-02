def validate_guess(num_list, num_1, num_2):
    if num_1 != num_2 and num_1 in range(len(num_list)) and num_2 in range(len(num_list)):
        return True

    return False


def remove_elements(num_list, num_1, num_2):
    print(f"Congrats! You have found matching elements - {num_list[num_1]}!")
    if num_1 > num_2:
        num_list.pop(num_1)
        num_list.pop(num_2)
    else:
        num_list.pop(num_2)
        num_list.pop(num_1)

    return num_list


def add_elements(num_list, count):
    half_element = (len(num_list) - 1) // 2
    num_list.insert(half_element + 1, f"-{count}a")
    num_list.insert(half_element + 1, f"-{count}a")
    print("Invalid input! Adding additional elements to the board")
    return num_list


def check_is_matching(num_list, num_1, num_2):
    if num_list[num_1] == num_list[num_2]:
        return True
    else:
        return False


def check_win(num_list):
    if len(num_list) == 0:
        return True
    else:
        return False


user_input = input()
memory_list = user_input.split()

attempts = 0
has_won = False
command = input()
while not command == 'end':
    attempts += 1
    guess = list(map(int, command.split()))
    is_guess_valid = validate_guess(memory_list, guess[0], guess[1])
    if len(memory_list) > 0:
        if is_guess_valid:
            if check_is_matching(memory_list, guess[0], guess[1]):
                memory_list = remove_elements(memory_list, guess[0], guess[1])
                has_won = check_win(memory_list)
                if has_won:
                    print(f"You have won in {attempts} turns!")
            else:
                print("Try again!")
        else:
            memory_list = add_elements(memory_list, attempts)
    command = input()

if command == 'end' and not has_won:
    print("Sorry you lose :(")
    print(*memory_list)
