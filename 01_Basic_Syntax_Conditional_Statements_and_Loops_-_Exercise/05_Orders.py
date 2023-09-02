number_of_orders = int(input())

total_cost = 0
for order in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_spent_daily = int(input())

    cost = price_per_capsule * capsules_spent_daily * days
    if cost > 0 \
            and 0.01 <= price_per_capsule <= 100 \
            and days in range(1, 31 + 1) \
            and capsules_spent_daily in range(1, 2000 + 1):
        print(f"The price for the coffee is: ${cost:.2f}")
        total_cost += cost

print(f"Total: ${total_cost:.2f}")
