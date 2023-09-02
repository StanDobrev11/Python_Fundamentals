class Dragon:
    def __init__(self, dragon_type, name, damage, health, armor):
        self.dragon_type = dragon_type
        self.name = name
        self.damage = int(damage) if damage != 'null' else 45
        self.health = int(health) if health != 'null' else 250
        self.armor = int(armor) if armor != 'null' else 10


number_of_dragons = int(input())

dragons_by_type = {}
for _ in range(number_of_dragons):
    dragon_type, name, damage, health, armor = input().split()
    current_dragon = Dragon(dragon_type, name, damage, health, armor)
    is_duplicated = False
    if dragon_type not in dragons_by_type:
        dragons_by_type[dragon_type] = []
    else:
        for dragon in dragons_by_type[dragon_type]:
            if name == dragon.name:
                dragon.damage = int(damage) if damage != 'null' else 45
                dragon.health = int(health) if health != 'null' else 250
                dragon.armor = int(armor) if armor != 'null' else 10
                is_duplicated = True
                break
    if is_duplicated:
        continue
    dragons_by_type[dragon_type].append(current_dragon)

type_stats = {}
for color, value in dragons_by_type.items():
    damage = 0
    health = 0
    armor = 0
    for dragon in value:
        damage += dragon.damage
        health += dragon.health
        armor += dragon.armor
    av_damage = damage / len(value)
    av_health = health / len(value)
    av_armor = armor / len(value)
    type_stats[color] = (av_damage, av_health, av_armor)

for color, value in dragons_by_type.items():
    av_damage, av_health, av_armor = type_stats[color]
    print(f'{color}::({av_damage:.2f}/{av_health:.2f}/{av_armor:.2f})')
    for dragon in sorted(value, key=lambda x: x.name):
        print(f'-{dragon.name} -> damage: {dragon.damage}, health: {dragon.health}, armor: {dragon.armor}')
