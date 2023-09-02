from math import factorial


def fact_div(num_1, num_2):
    return f"{factorial(num_1) / factorial(num_2):.2f}"


number_1 = int(input())
number_2 = int(input())

print(fact_div(number_1, number_2))
