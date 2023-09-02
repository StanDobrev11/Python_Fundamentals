budget = float(input())
price_per_kg_flour = float(input())

price_per_pack_of_eggs = price_per_kg_flour * 0.75
price_per_ltr_milk = price_per_kg_flour + 0.25 * price_per_kg_flour

loave_cost = price_per_kg_flour + price_per_pack_of_eggs + price_per_ltr_milk / 4

colored_eggs = 0
number_of_loaves = 0
while budget > loave_cost:
    budget -= loave_cost
    number_of_loaves += 1
    colored_eggs += 3
    if number_of_loaves % 3 == 0:
        colored_eggs -= number_of_loaves - 2

money_left = budget

print(f"You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs "
      f"and {money_left:.2f}BGN left.")
