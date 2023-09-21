"""
Let`s take a break and visit the game bar at SoftUni. It is about time for the people behind the bar to go home and you are the person who has to draw the line and calculate the money from the products that were sold throughout the day. Until you receive a line with text "end of shift" you will be given lines of input. But before processing that line you should do some validations first.
Each valid order should have a customer, product, count and a price:
•	Valid customer's name should be surrounded by '%' and must start with a capital letter, followed by lower-case letters
•	Valid product contains any word character (not only letters)and must be surrounded by '<' and '>'
•	Valid count is an integer, surrounded by '|'
•	Valid price is any real number followed by '$'
The parts of a valid order should appear in the order given: customer, product, count and a price.
Between each part there can be other symbols, except ('|', '$', '%' and '.')
For each valid line print on the console: "{customerName}: {product} - {totalPrice}"
When you receive "end of shift" print the total amount of money for the day rounded to 2 decimal places in the following format:"Total income: {income}".
Input / Constraints
•	Strings that you have to process until you receive text "end of shift".
Output
•	Print all of the valid lines in the format "{customerName}: {product} - {totalPrice}"
•	After receiving "end of shift" print the total amount of money for the day rounded to 2 decimal places in the following format: "Total income: {income}"
•	Allowed working time / memory: 100ms / 16MB.

Input	                    Output	                    Comment
%George%<Croissant>|2|10.3$
%Peter%<Gum>|1|1.3$
%Maria%<Cola>|1|2.4$
                            end of shift	George: Croissant - 20.60
                            Peter: Gum - 1.30
                            Maria: Cola - 2.40
                            Total income: 24.30
                                                        Each line is valid, so we print each order,
                                                        calculating the total price of the product bought.
                                                        At the end we print the total income for the day

%InvalidName%<Croissant>|2|10.3$
%Peter%<Gum>1.3$
%Maria%<Cola>|1|2.4
%Valid%<Valid>valid|10|valid20$
end of shift
                            Valid: Valid - 200.00
                            Total income: 200.00
                                                        On the first line, the customer name isn`t valid, so we skip that line.
                                                        The second line is missing product count.
                                                        The third line don`t have a valid price.
                                                        And only the forth line is valid
"""

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
