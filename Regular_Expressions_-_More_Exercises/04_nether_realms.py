import re

daemons = [daemon.strip() for daemon in input().split(', ')]

health_regex = r'[^0-9\+\-\*\/\.]'
damage_regex = r'[\+\-]?[\d+(\.\d+)?]+'
damage_multiplier_regex = r'[\/\*]'

for daemon in sorted(daemons):
    health = 0
    damage = 0

    health_str = re.findall(health_regex, daemon)
    for letter in health_str:
        health += ord(letter)

    damage_str = re.findall(damage_regex, daemon)
    for number in damage_str:
        damage += float(number)

    damage_multi_str = re.findall(damage_multiplier_regex, daemon)
    for symbol in damage_multi_str:
        if symbol == "*":
            damage *= 2
        else:
            damage /= 2

    print(f"{daemon} - {health} health, {damage:.2f} damage")
    # print(health_str)
    # print(damage_str)
    # print(damage_multi_str)
