group_size = int(input())
days_adventure = int(input())

total_coins = 0
for day in range(1, days_adventure + 1):
    if day % 10 == 0:
        group_size -= 2
    if day % 15 == 0:
        group_size += 5
    earn = 50
    spent = 2 * group_size  # food consumption
    total_coins += earn - spent
    if day % 3 == 0:
        spent = 3 * group_size  # water consumption motivation party
        total_coins -= spent
    if day % 5 == 0:
        earn = 20 * group_size
        total_coins += earn
        if day % 3 == 0:
            spent = 2 * group_size
            total_coins -= spent

coins_per_companion = total_coins / group_size
print(f"{group_size} companions received {coins_per_companion:.0f} coins each.")
