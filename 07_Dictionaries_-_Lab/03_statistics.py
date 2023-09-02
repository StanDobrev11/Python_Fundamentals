command = input()

products = {}
while command != 'statistics':
    product, value = command.split(':')
    if product in products:
        products[product] += int(value)
    else:
        products[product] = int(value)
    command = input()
print("Products in stock:")
for product, value in products.items():
    print(f'- {product}: {value}')
print(f'Total Products: {len(products)}')

# total_value = 0
# for item in products:
#     total_value += products[item]
# print(f'Total Quantity: {total_value}')
print(f'Total Quantity: {sum(products.values())}')