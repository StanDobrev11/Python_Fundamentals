import re

text_string = input()

emoji_pattern = r'(?P<emoji>(?P<sep>::|\*\*)(?P<text>[A-Z][a-z]{2,})(?P=sep))'
digit_pattern = r'\d'

cool_threshold_list = [int(x) for x in re.findall(digit_pattern, text_string)]
cool_threshold = 1
for number in cool_threshold_list:
    cool_threshold *= number

emoji_list = [x.group('emoji') for x in re.finditer(emoji_pattern, text_string)]

emoji_dict = {}
for emoji in emoji_list:
    emoji_sliced = emoji[2:-2]
    emoji_coolness = 0
    for letter in emoji_sliced:
        emoji_coolness += ord(letter)
    emoji_dict[emoji] = emoji_coolness

print(f'Cool threshold: {cool_threshold}')
print(f'{len(emoji_dict)} emojis found in the text. The cool ones are:')
for emoji, coolness in emoji_dict.items():
    if coolness >= cool_threshold:
        print(f'{emoji}')
