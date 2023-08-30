class Hero:
    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = int(hp)
        self.mp = int(mp)

    def cast_spell(self, needed_mp):
        if self.mp >= needed_mp:
            self.mp -= needed_mp
            return True

        return False

    def take_damage(self, damage):
        if self.hp > damage:
            self.hp -= damage
            return True
        return False

    def recharge(self, amount):
        if self.mp + amount > 200:
            amount = 200 - self.mp
            self.mp = 200
        else:
            self.mp += amount
        return amount

    def heal(self, amount):
        if self.hp + amount > 100:
            amount = 100 - self.hp
            self.hp = 100
        else:
            self.hp += amount
        return amount


n = int(input())

heroes = {}
for _ in range(n):
    name, hp, mp = input().split()
    heroes[name] = Hero(name, hp, mp)

command = input()
while not command == 'End':
    command = command.split(' - ')
    action, hero_name = command[0], command[1]
    if action == 'CastSpell':
        needed_mp, spell_name = int(command[2]), command[3]
        if heroes[hero_name].cast_spell(needed_mp):
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name].mp} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    elif action == 'TakeDamage':
        damage, attacker = int(command[2]), command[3]
        if heroes[hero_name].take_damage(damage):
            print(f'{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name].hp} HP left!')
        else:
            del heroes[hero_name]
            print(f'{hero_name} has been killed by {attacker}!')
    elif action == 'Recharge':
        amount = int(command[2])
        amount_recovered = heroes[hero_name].recharge(amount)
        print(f'{hero_name} recharged for {amount_recovered} MP!')
    elif action == 'Heal':
        amount = int(command[2])
        amount_recovered = heroes[hero_name].heal(amount)
        print(f"{hero_name} healed for {amount_recovered} HP!")

    command = input()

for hero in heroes:
    print(hero)
    print(f'  HP: {heroes[hero].hp}')
    print(f'  MP: {heroes[hero].mp}')
