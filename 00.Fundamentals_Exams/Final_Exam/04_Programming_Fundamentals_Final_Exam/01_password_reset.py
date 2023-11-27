def take_odd():
    """ Takes only the characters at ODD indices and concatenates them to obtain the new
    raw password and then prints it """

    result = ''
    for i in range(1, len(password), 2):
        result += password[i]

    return result


def cut(idx, length):
    """ Gets the substring with the given length starting from the given index from the password and
    removes its first occurrence, then prints the password on the console """

    substring = password[idx: idx + length]

    find_first_occurrence_idx = password.index(substring)

    return password[:find_first_occurrence_idx] + password[find_first_occurrence_idx + length:]


def sub(old, new):
    return password.replace(old, new)


password = input()

command_line = input()

while command_line != 'Done':
    command, *rest = command_line.split()

    if command == 'TakeOdd':
        password = take_odd()
        print(password)

    elif command == 'Cut':
        idx, length = rest
        password = cut(int(idx), int(length))
        print(password)

    elif command == 'Substitute':
        old, new = rest
        if old not in password:
            print("Nothing to replace!")
        else:
            password = sub(old, new)
            print(password)

    command_line = input()

print(f"Your password is: {password}")
