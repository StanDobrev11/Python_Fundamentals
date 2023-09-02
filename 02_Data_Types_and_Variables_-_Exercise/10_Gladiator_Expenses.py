lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmet_is_broken = 0
sword_is_broken = 0
shield_is_broken = 0
armor_is_broken = 0

for fights in range(1, lost_fights + 1):
    if fights % 2 == 0:
        helmet_is_broken += 1
    if fights % 3 == 0:
        sword_is_broken += 1
        if fights % 2 == 0:
            shield_is_broken += 1
            if shield_is_broken % 2 == 0:
                armor_is_broken = shield_is_broken / 2

expenses = helmet_is_broken * helmet_price \
           + sword_is_broken * sword_price \
           + shield_is_broken * shield_price \
           + armor_is_broken * armor_price

print(f"Gladiator expenses: {expenses:.2f} aureus")
