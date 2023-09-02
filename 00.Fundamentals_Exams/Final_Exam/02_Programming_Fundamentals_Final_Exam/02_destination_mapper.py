import re

location = input()

pattern = r'(?<=(=|/))[A-Z][A-Za-z][A-Za-z]+(?=\1)'
data = [x.group() for x in re.finditer(pattern, location)]

ttl_length = 0

for item in data:
    ttl_length += len(item)

print(f"Destinations: {', '.join(data)}")
print(f'Travel Points: {ttl_length}')
