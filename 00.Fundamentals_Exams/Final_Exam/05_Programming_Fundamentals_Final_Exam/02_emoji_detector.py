import re
from functools import reduce

text = input()

valid_pattern = r"(::|\*\*)([A-Z][a-z]{2,})(\1)"
valid_emojy = [x.group() for x in re.finditer(valid_pattern, text)]

cool_threshold_list = [int(num) for num in text if num.isdigit()]
cool_threshold = reduce(lambda x, y: x * y, cool_threshold_list)

print(f"Cool threshold: {cool_threshold}")
print(f"{len(valid_emojy)} emojis found in the text. The cool ones are:")

for emojy in valid_emojy:
    coolness = sum(ord(x) for x in emojy if x.isalpha())
    if coolness >= cool_threshold:
        print(emojy)
