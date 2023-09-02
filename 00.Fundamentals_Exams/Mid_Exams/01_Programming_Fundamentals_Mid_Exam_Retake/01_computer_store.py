discount = 0.9
tax = 1.2

current_amount = 0
user_input = input()

while user_input != "special" and user_input != "regular":
    price = float(user_input)
    if price < 0:
        print("Invalid price!")
    else:
        current_amount += price
    user_input = input()

total_price = current_amount * tax
taxes = total_price - current_amount

if total_price == 0:
    print("Invalid order!")
else:
    if user_input == "special":
        total_price *= discount

    print(f"Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {current_amount:.2f}$\n"
          f"Taxes: {taxes:.2f}$\n"
          f"-----------\n"
          f"Total price: {total_price:.2f}$")
