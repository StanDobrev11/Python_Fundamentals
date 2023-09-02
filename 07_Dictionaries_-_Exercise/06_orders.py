class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


command = input()

prices = {}
quantities = {}
while command != 'buy':
    name, price_str, quantity_str = command.split()
    # product = Product(name, float(price_str), int(quantity_str))
    if name not in quantities:
        quantities[name] = int(quantity_str)
    else:
        quantities[name] += int(quantity_str)
    prices[name] = float(price_str)

    command = input()

total = {}
for key in quantities:
    total[key] = quantities[key] * prices[key]

for key, value in total.items():
    print(f'{key} -> {value:.2f}')
