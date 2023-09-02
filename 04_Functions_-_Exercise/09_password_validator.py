from string import ascii_lowercase


def validator(password):
    if length_validator(password) is True:
        if letter_validator(password) is True:
            if digit_count_validator(password) is True:
                print("Password is valid")

    if length_validator(password) is not True:
        print(length_validator(password))
    if letter_validator(password) is not True:
        print(letter_validator(password))
    if digit_count_validator(password) is not True:
        print(digit_count_validator(password))


def length_validator(password):  # "Password must be between 6 and 10 characters"
    if 6 <= len(password) <= 10:
        return True
    else:
        return "Password must be between 6 and 10 characters"


def letter_validator(password):  # "Password must consist only of letters and digits"
    is_valid = False
    for symbol in password:
        if symbol in ascii_lowercase or symbol.isdigit():
            is_valid = True
        else:
            return "Password must consist only of letters and digits"

    if is_valid:
        return True


def digit_count_validator(password):  # "Password must have at least 2 digits"
    count = 0
    for symbol in password:
        if symbol.isdigit():
            count += 1
            if count == 2:
                return True

    return "Password must have at least 2 digits"


test_password = input()
test_password = test_password.lower()
validator(test_password)
