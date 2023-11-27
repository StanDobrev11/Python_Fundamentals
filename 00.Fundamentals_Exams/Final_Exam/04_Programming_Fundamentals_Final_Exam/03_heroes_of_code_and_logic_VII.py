class Hero:
    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = int(hp)
        self.mp = int(mp)

    def cast_spell(self, mp_required, spell_name):
        """ If the hero has the required MP, he casts the spell, thus reducing his MP """
        mp_required = int(mp_required)
        if self.mp - mp_required >= 0:
            self.mp -= mp_required
            print(f"{self.name} has successfully cast {spell_name} and now has {self.mp} MP!")
        else:
            print(f"{self.name} does not have enough MP to cast {spell_name}!")

    def take_damage(self, damage, attacker):
        """ Reduce the hero HP by the given damage amount.
        If the hero is still alive (his HP is greater than 0) """

        damage = int(damage)
        if self.hp - damage > 0:
            self.hp -= damage
            print(f"{self.name} was hit for {damage} HP by {attacker} and now has {self.hp} HP left!")
        else:
            del heroes[self.name]
            print(f"{self.name} has been killed by {attacker}!")

    def recharge(self, amount):

        amount = int(amount)
        if self.mp + amount >= 200:
            print(f"{self.name} recharged for {200 - self.mp} MP!")
            self.mp = 200
        else:
            print(f"{self.name} recharged for {amount} MP!")
            self.mp += amount

    def heal(self, amount):

        amount = int(amount)
        if self.hp + amount >= 100:
            print(f"{self.name} healed for {100 - self.hp} HP!")
            self.hp = 100
        else:
            print(f"{self.name} healed for {amount} HP!")
            self.hp += amount

    def __repr__(self):
        return f"{self.name}\n  HP: {self.hp}\n  MP: {self.mp}"


command_map = {
    'CastSpell': Hero.cast_spell,
    'TakeDamage': Hero.take_damage,
    'Recharge': Hero.recharge,
    'Heal': Hero.heal,
}

num_of_heroes = int(input())
heroes = {}
for _ in range(num_of_heroes):
    hero_name, hero_hp, hero_mp = input().split()
    heroes[hero_name] = Hero(hero_name, hero_hp, hero_mp)

command_line = input()

while command_line != 'End':
    command, *rest = command_line.split(' - ')

    if command in command_map:
        command_map[command](heroes[rest[0]], *rest[1:])  # Hero.heal(heroes['SirMullich'], 50)

    command_line = input()

print('\n'.join(hero.__repr__() for hero in heroes.values()))
