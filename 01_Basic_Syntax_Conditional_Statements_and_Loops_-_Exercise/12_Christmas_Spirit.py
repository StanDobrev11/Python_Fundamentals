qtity_to_buy = int(input())
days_left = int(input())

list_additional_items = ["Tree Skirt",
                         "Tree Garland",
                         "Tree Lights"]
prices_per_items = {"Ornament Set": 2,
                    "Tree Skirt": 5,
                    "Tree Garland": 3,
                    "Tree Lights": 15}
spirit_points_per_item = {"Ornament Set": 5,
                          "Tree Skirt": 3,
                          "Tree Garland": 10,
                          "Tree Lights": 17}

spirit_points = 0
money_spent = 0
for day in range(1, days_left + 1):
    items_bought = []
    if day % 2 == 0:
        items_bought.append("Ornament Set")
    if day % 3 == 0:
        items_bought.append("Tree Skirt")
        items_bought.append("Tree Garland")
        # spirit_points += 30
    if day % 5 == 0:
        items_bought.append("Tree Lights")
    if day % 10 == 0:
        spirit_points -= 20
        for each_item in list_additional_items:
            money_spent += prices_per_items[each_item]
    if day % 3 == 0 and day % 5 == 0:
        spirit_points += 30
    if day % 11 == 0:
        qtity_to_buy += 2
    if day == days_left and days_left % 10 == 0:
        spirit_points -= 30
    for items in items_bought:
        money_spent += qtity_to_buy * prices_per_items[items]
        spirit_points += spirit_points_per_item[items]

print(f"Total cost: {money_spent}")
print(f"Total spirit: {spirit_points}")
