import re


class Customer:
    total_income = 0

    def __init__(self, name, product, quantity, price):
        self.name = name
        self.product = product
        self.quantity = int(quantity)
        self.price = float(price)
        self.cost = self.quantity * self.price

    def add_income(self):
        Customer.total_income += self.quantity * self.price


pattern = r'%(?P<name>[A-Z][a-z]+)%<(?P<product>\w+)>(\w+)?\|(?P<quantity>\d+)\|([a-zA-Z0-9]+)?(?P<price>\d+\.?\d+?(?=\$))'

command = input()
list_of_customers = []
while command != 'end of shift':
    data = re.finditer(pattern, command)
    for customer_dict in data:
        customer = Customer(
            customer_dict['name'],
            customer_dict['product'],
            customer_dict['quantity'],
            customer_dict['price']
        )
        list_of_customers.append(customer)
        customer.add_income()
    command = input()

for customer in list_of_customers:
    print(f"{customer.name}: {customer.product} - {customer.cost:.2f}")
print(f'Total income: {Customer.total_income:.2f}')

# qtity = '(?<=\|)(?P<quantity>\d+)(?=\|)'
# price = '(?P<price>\d+(\.\d+)?(?=\$))'