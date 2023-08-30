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
