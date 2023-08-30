import re


class Food:
    total_calories = 0

    def __init__(self, name, exp_date, calories):
        self.name = name
        self.exp_date = exp_date
        self.calories = int(calories)

    def calculate_calories(self):
        Food.total_calories += self.calories


pattern = r'(?P<sep>#|\|)(?P<item>[A-Za-z\s]+)(?P=sep)(?P<exp>\d{2}/\d{2}/\d{2})(?P=sep)(?P<cal>\d+)(?P=sep)'

food_input = input()

data = re.finditer(pattern, food_input)
list_of_foods = []

for item in data:
    item = item.groupdict()
    food = Food(item['item'], item['exp'], item['cal'])
    food.calculate_calories()
    list_of_foods.append(food)

print(f'You have food to last you for: {Food.total_calories // 2000} days!')
for food in list_of_foods:
    print(f"Item: {food.name}, Best before: {food.exp_date}, Nutrition: {food.calories}")
