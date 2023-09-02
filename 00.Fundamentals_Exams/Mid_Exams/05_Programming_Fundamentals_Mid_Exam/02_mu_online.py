def fight(hp, power, name):
    hp -= int(power)
    if hp > 0:
        print(f"You slayed {name}.")
        return hp
    else:
        print(f"You died! Killed by {name}.")
        return True


rooms = input().split("|")
is_dead = False
health = 100
bit_coins = 0
for each_room in rooms:
    action, value = each_room.split()
    if action == "potion":
        if health <= 100:
            health += int(value)
            if health > 100:
                used_value = int(value) - (health - 100)
                print(f"You healed for {used_value} hp.")
                health = 100
            else:
                print(f"You healed for {value} hp.")
        print(f"Current health: {health} hp.")
    elif action == "chest":
        bit_coins += int(value)
        print(f"You found {value} bitcoins.")
    else:
        monster_name = action
        health = fight(health, value, monster_name)
        if health is True:
            print(f"Best room: {rooms.index(each_room) + 1}")
            is_dead = True
            break

if not is_dead:
    print("You've made it!")
    print(f"Bitcoins: {bit_coins}")
    print(f"Health: {health}")
