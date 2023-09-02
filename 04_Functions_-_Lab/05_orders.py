# def calc_price(cost, qtity):
#     return f"{cost * qtity:.2f}"


item_price_dict = {"coffee": 1.5, "coke": 1.4, "water": 1, "snacks": 2}

item = input()
quantity = int(input())

# print(calc_price(item_price_dict[item], quantity))
print(f"{(lambda a, b: a * b)(item_price_dict[item], quantity):.2f}")
