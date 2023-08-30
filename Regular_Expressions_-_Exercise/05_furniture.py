import re


class Furniture:
    total_cost = 0

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)

    def add_price(self):
        Furniture.total_cost += self.quantity * self.price


pattern = r'(?<=>>)(?P<furniture>[a-zA-Z]+)(?:<<)(?P<price>[0-9]+(\.[0-9]+)?)!(?P<quantity>\d+)'

command = input()
items = []

while command != 'Purchase':
    data = re.finditer(pattern, command)
    for item_dict in data:
        item = Furniture(item_dict['furniture'], item_dict['price'], item_dict['quantity'])
        items.append(item)
        item.add_price()
    command = input()

print('Bought furniture:')
for item in items:
    print(item.name)

print(f"Total money spend: {Furniture.total_cost:.2f}")