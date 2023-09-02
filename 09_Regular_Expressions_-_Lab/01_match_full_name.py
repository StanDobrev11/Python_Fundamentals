import re

pattern = r'\b[A-Z][a-z]+\s[A-Z][a-z]+\b'
data = input()

names = re.findall(pattern, data)

print(*names)
