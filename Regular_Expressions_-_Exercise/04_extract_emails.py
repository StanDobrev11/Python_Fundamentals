import re

data = input().lower()

pattern = r'(^|(?<=\s))[a-z0-9]+[\._-]?[a-z0-9]+@[a-z]+\-?[a-z]+\.[a-z]+(\.[a-z]+)?'

emails = re.finditer(pattern, data)

for mail in emails:
    print(mail.group())
