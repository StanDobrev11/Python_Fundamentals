group_size = int(input())
days_adventure = int(input())

total_coins = 0
for day in range(1, days_adventure + 1):
    if day % 10 == 0:
        group_size -= 2
    if day % 15 == 0:
        group_size += 5
    total_coins += 50 - 2 * group_size # every day +50 , -2 * group
    if day % 3 == 0:
        total_coins -= 3 * group_size
    if day % 5 == 0:
        total_coins += 20 * group_size
        if day % 3 == 0:
            total_coins -= 2 * group_size

coins_per_companion = total_coins / group_size
print(f"{group_size} companions received {int(coins_per_companion)} coins each.")
