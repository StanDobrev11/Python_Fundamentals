import re

num_of_lines = int(input())

pattern = r"^(%|\$)(?P<tag>[A-Z][a-z]{2,})(\1): (?P<digits>(\[\d+\]\|){3})$"

for _ in range(num_of_lines):
    coded_msg = input()

    try:
        decrypted = [x.groupdict() for x in re.finditer(pattern, coded_msg)][0]
    except IndexError:
        print("Valid message not found!")
        continue

    digits_only = decrypted['digits'].split('|')

    result = ''
    for i in range(3):
        nums = digits_only[i]
        digit_pattern = r"(\d+)"

        digits = int([x.group() for x in re.finditer(digit_pattern, nums)][0])
        result += chr(digits)

    print(f"{decrypted['tag']}: {result}")
