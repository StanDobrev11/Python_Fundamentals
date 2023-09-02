days = int(input())
plunder_per_day = int(input())
expected_plunder = float(input())

plunder_gathered = 0
for day in range(1, days + 1):
    plunder_gathered += plunder_per_day
    if day % 3 == 0:
        plunder_gathered += plunder_per_day * 0.5
    if day % 5 == 0:
        plunder_gathered *= 0.7

if plunder_gathered >= expected_plunder:
    print(f"Ahoy! {plunder_gathered:.2f} plunder gained.")
else:
    percentage = 100 * plunder_gathered / expected_plunder
    print(f"Collected only {percentage:.2f}% of the plunder.")
