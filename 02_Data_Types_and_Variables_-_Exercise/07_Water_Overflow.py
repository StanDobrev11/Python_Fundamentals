capacity = 255  # water tank capacity in ltrs
number_of_water_ingress = int(input())

water_in_tank = 0
for each_ingress in range(number_of_water_ingress):
    quantity_of_water = int(input())
    water_in_tank += quantity_of_water
    if water_in_tank > capacity:
        print("Insufficient capacity!")
        water_in_tank -= quantity_of_water

print(water_in_tank)
