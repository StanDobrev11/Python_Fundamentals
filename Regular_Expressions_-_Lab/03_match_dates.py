import re

pattern = r'(?P<day>\d{2})(?P<separator>[\./-])(?P<month>[A-Z][a-z]{2})\2(?P<year>\d{4})'

data = input()

dates = re.finditer(pattern, data)

for date in dates:
    date_dict = date.groupdict()

    print(f"Day: {date_dict['day']}, Month: {date_dict['month']}, Year: {date_dict['year']}")
