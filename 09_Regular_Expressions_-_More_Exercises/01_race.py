"""
Write a program that processes information about a race. On the first line you will be given list of
participant separated by ", ". On the next few lines until you receive a line "end of race" you will
be given some info which will be some alphanumeric characters. In between them you could have some
extra characters which you should ignore. For example: "G!32e%o7r#32g$235@!2e". The letters are the
name of the person and the sum of the digits is the distance he ran. So here we have George who ran 29 km.
Store the information about the person only if the list of racers contains the name of the person.
If you receive the same person more than once just add the distance to his old distance.
At the end print the top 3 racers ordered by distance in descending in the format:
"1st place: {first racer}
2nd place: {second racer}
3rd place: {third racer}"

Input	                Output	                Comment
George, Peter, Bill, Tom
G4e@55or%6g6!68e!!@
R1@!3a$y4456@
B5@i@#123ll
G@e54o$r6ge#
7P%et^#e5346r
T$o553m&6
                        end of race	1st place: George
                        2nd place: Peter
                        3rd place: Tom
                                                On the 3rd input line we have Ray. He is not in the list,
                                                so we do not count his result. The other ones are valid.
                                                George has total of 55 km, Peter has 25 and Tom has 19.
                                                We do not print Bill because he is on 4th place.
"""

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
