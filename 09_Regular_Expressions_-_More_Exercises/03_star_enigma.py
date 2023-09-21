"""
The war is in its peak, but you, young Padawan, can turn the tides with your programming skills. You are tasked to create a program to decrypt the messages of The Order and prevent the death of hundreds of lives.
You will receive several messages, which are encrypted using the legendary star enigma. You should decrypt the messages, following these rules:
To properly decrypt a message, you should count all the letters[s, t, a, r] – case-insensitive and remove the count from the current ASCII value of each symbol of the encrypted message.
After decryption:
Each message should have a planet name, population, attack type ('A', as attack or 'D', as destruction) and soldier count.
The planet name starts after'@' and contains only letters from the Latin alphabet.
The planet population starts after ':' and is an Integer;
The attack type may be "A"(attack) or "D"(destruction) and must be surrounded by "!" (exclamation mark).
The soldier count starts after "->" and should be an Integer.

The order in the message should be: planet name -> planet population -> attack type -> soldier count. Each part can be separated from the others by any character except: '@', '-', '!', ':' and '>'.
Input / Constraints
•	The first line holds n – the number of messages– integer in range [1…100];
•	On the next n lines, you will be receiving encrypted messages.
Output
After decrypting all messages, you should print the decrypted information in the following format:
First print the attacked planets, then the destroyed planets.
"Attacked planets: {attackedPlanetsCount}"
"-> {planetName}"
"Destroyed planets: {destroyedPlanetsCount}"
"-> {planetName}"
The planets should be ordered by name alphabetically.

Input	                        Output	                        Comments
2
STCDoghudd4=63333$D$0A53333
EHfsytsnhf?8555&I&2C9555SR
                                Attacked planets: 1
                                ->Alderaa
                                Destroyed planets: 1
                                ->Cantonica
                                                                We receive two messages, to decrypt them we calculate the key:
                                                                First message has decryption key 3. So we substract from each characters code 3.
                                                                PQ@Alderaa1:30000!A!->20000
                                                                The second message has key 5.
                                                                @Cantonica:3000!D!->4000NM
                                                                Both messages are valid and they contain planet, population, attack type and soldiers count.
                                                                After decrypting all messages we print each planet according the format given.
3
tt(''DGsvywgerx>6444444444%H%1B9444
GQhrr|A977777(H(TTTT
EHfsytsnhf?8555&I&2C9555SR
                                Attacked planets: 0
                                Destroyed planets: 2
                                ->Cantonica
                                -> Coruscant
                                                                We receive three messages.
                                                                Message one is decrypted with key 4:
                                                                pp$##@Coruscant:2000000000!D!->5000
                                                                Message two is decrypted with key 7:
                                                                @Jakku:200000!A!MMMM
                                                                This is invalid message, missing soldier count, so we continue.
                                                                The third message has key 5.
                                                                @Cantonica:3000!D!->4000NM
"""

import re


class Planet:
    attacked = []
    destroyed = []

    def __init__(self, name, attacked_status):
        self.name = name
        self.attacked_status = attacked_status

    def attacked_destroyed(self):
        if self.attacked_status == "A":
            Planet.attacked.append(self.name)
        else:
            Planet.destroyed.append(self.name)


n = int(input())

for _ in range(n):
    coded_msg = input()
    key_pattern = r'[starSTAR]'
    key = len(re.findall(key_pattern, coded_msg))
    decoded_msg = ''
    for ch in coded_msg:
        decoded_ch = chr(ord(ch) - key)
        decoded_msg += decoded_ch

    fight_pattern = r'((?<=@)(?P<planet>[a-zA-Z]+)).*?((?<=:)(?P<population>\d+)).*?!(?P<attack>[AD])!.*?->(?P<soldiers>\d+)'
    planet_info = re.finditer(fight_pattern, decoded_msg)
    for info_dict in planet_info:
        planet = Planet(info_dict['planet'], info_dict['attack'])
        planet.attacked_destroyed()

print(f'Attacked planets: {len(Planet.attacked)}')
for planet in sorted(Planet.attacked):
    print(f'-> {planet}')
print(f'Destroyed planets: {len(Planet.destroyed)}')
for planet in sorted(Planet.destroyed):
    print(f'-> {planet}')
