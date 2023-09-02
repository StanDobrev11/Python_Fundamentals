food = float(input()) * 1000
hay = float(input()) * 1000
cover = float(input()) * 1000
weight = float(input()) * 1000

food_per_day = 300

remaining_food = food
for day in range(1, 31):
    remaining_food -= food_per_day
    if day % 2 == 0:
        hay -= remaining_food * 5 / 100

    if day % 3 == 0:
        cover -= weight / 3

if remaining_food > 0 and hay > 0 and cover > 0:
    print(
        f"Everything is fine! Puppy is happy! Food: {remaining_food / 1000 :.2f}, Hay: {hay / 1000:.2f}, Cover: {cover / 1000:.2f}.")
else:
    print("Merry must go to the pet store!")
