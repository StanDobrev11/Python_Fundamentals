import re

pattern = r'(?<=\b_)[A-Za-z0-9]+\b'
# pattern = r'\b_(?P<valid>[A-Za-z]+)\b'

data = input()

variables = re.finditer(pattern, data)

variables = [var.group() for var in variables]

print(*variables, sep=",")
