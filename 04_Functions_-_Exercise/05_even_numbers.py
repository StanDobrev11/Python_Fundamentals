def even_numbers(number_list):
    return list(map(int, list(filter(lambda x: int(x) % 2 == 0, number_list))))


numbers = input()
numbers = numbers.split()

print(even_numbers(numbers))
