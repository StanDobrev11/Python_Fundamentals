in_stock = input().split()
products = input().split()

bakery = {}

for i in range(0, len(in_stock), 2):
    key = in_stock[i]
    value = in_stock[i + 1]
    bakery[key] = int(value)

for product in products:
    if product in bakery:
        print(f'We have {bakery[product]} of {product} left')
    else:
        print(f"Sorry, we don't have {product}")
