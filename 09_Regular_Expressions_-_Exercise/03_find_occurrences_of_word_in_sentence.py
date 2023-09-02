import re

data = input().lower()
key = input().lower()

pattern = f"{key}\\b"

repeated = re.findall(pattern, data)

print(len(repeated))
