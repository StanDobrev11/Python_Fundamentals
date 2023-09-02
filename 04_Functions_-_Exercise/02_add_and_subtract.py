def subtract(x, y, z):
    return sum_numbers(x, y) - z


def sum_numbers(x, y):
    return x + y


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

print(subtract(num_1, num_2, num_3))
