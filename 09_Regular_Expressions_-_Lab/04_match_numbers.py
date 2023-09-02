import re

pattern = r'(^|(?<=\s))\-?\d+(\.\d+)?($|(?=\s))'

data = input()

numbers = re.finditer(pattern, data)

numbers = [n.group() for n in numbers]

print(*numbers)


