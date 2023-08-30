import re

data = input()
pattern = r'(\+359\s2\s\d{3}\s\d{4}\b)|(\+359\-2-\d{3}-\d{4}\b)'

numbers = re.finditer(pattern, data)

numbers = [number.group(0) for number in numbers]

print(*numbers, sep=', ')
