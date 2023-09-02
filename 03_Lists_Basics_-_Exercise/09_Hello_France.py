from decimal import Decimal

item_price = input()
budget = Decimal(input())
ticket_cost = 150
item_price = item_price.split("|")
profit = 0
sell_prices_list = []
list_items_sold = []
item_dict = {'Clothes': 50, 'Shoes': 35, 'Accessories': 20.5}
for item in item_price:
    item = item.split("->")
    if Decimal(item[1]) <= item_dict[item[0]]:
        price = Decimal(item[1])
        if budget >= price:
            list_items_sold.append(price)
            budget -= price
            sell_price = price
            sell_price *= Decimal('1.4')
            sell_prices_list.append(round(sell_price, 2))
            profit += price * Decimal('0.4')
print(*sell_prices_list)
print(f"Profit: {profit:.2f}")
new_budget = budget + sum(sell_prices_list)
if new_budget >= ticket_cost:
    print("Hello, France!")
else:
    print("Not enough money.")
