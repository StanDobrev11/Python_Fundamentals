import re

names = input().split(', ')
command = input()

nums_pattern = r'\d'
letters_pattern = r'[A-Za-z]'

participants = {}
for name in names:
    participants[name] = 0

while command != 'end of race':
    name = ''
    num_list = re.findall(nums_pattern, command)
    num_list = [int(x) for x in num_list]
    letter_list = re.findall(letters_pattern, command)

    distance = sum(num_list)
    for letter in letter_list:
        name += letter

    if name in participants:
        participants[name] += distance

    command = input()

winners = []
for name, value in sorted(participants.items(), key=lambda x: x[1], reverse=True):
    winners.append(name)

print(f'1st place: {winners[0]}')
print(f'2nd place: {winners[1]}')
print(f'3rd place: {winners[2]}')
