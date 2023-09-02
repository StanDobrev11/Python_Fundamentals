battle_field = []
rows_of_field = int(input())
for _ in range(rows_of_field):
    row = input().split()
    row = list(map(int, row))
    battle_field.append(row)
attack = input().split()

ships_destroyed = 0
for each_attack in attack:
    row, col = list(map(int, each_attack.split("-")))
    if battle_field[row][col] > 0:
        battle_field[row][col] -= 1
        if battle_field[row][col] == 0:
            ships_destroyed += 1

print(ships_destroyed)
