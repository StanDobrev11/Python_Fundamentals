def sum_of_odd_digits(number):
    return sum([int(digit) for digit in number if int(digit) % 2 == 1])


def sum_of_even_digits(number):
    return sum([int(digit) for digit in number if int(digit) % 2 == 0])


number = input()
number = list(number)

print(f"Odd sum = {sum_of_odd_digits(number)}, Even sum = {sum_of_even_digits(number)}")
