import re

location = input()

pattern = r'(?<=(=|/))[A-Z][A-Za-z][A-Za-z]+(?=\1)'
data = [x.group() for x in re.finditer(pattern, location)]
points = sum(len(x) for x in data)

print(f"Destinations: {', '.join(data)}")
print(f"Travel Points: {points}")
