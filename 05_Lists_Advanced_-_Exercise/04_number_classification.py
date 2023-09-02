number_line = input()

positive = list(filter(lambda x: int(x) >= 0, number_line.split(", ")))
negative = list(filter(lambda x: int(x) < 0, number_line.split(", ")))
even = list(filter(lambda x: int(x) % 2 == 0, number_line.split(", ")))
odd = list(filter(lambda x: int(x) % 2 == 1, number_line.split(", ")))

print(f'Positive: {", ".join(positive)}')
print(f'Negative: {", ".join(negative)}')
print(f'Even: {", ".join(even)}')
print(f'Odd: {", ".join(odd)}')
