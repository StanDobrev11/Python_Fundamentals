level_of_fire = input()
water_qtity = int(input())

level_of_fire = level_of_fire.split("#")

cell_effort = 0
total_effort = 0
total_fire_put_out = 0
is_water_available = True
cell_count = len(level_of_fire)
print("Cells:")
while is_water_available and cell_count > 0:
    for index in range(cell_count):
        cell = level_of_fire[index]
        cell = cell.split("=")
        if cell[0] == "High " and int(cell[1]) in range(81, 125 + 1):
            if water_qtity >= int(cell[1]):
                water_qtity -= int(cell[1])
                cell_effort = int(cell[1]) * 0.25
                print(" -", int(cell[1]))
                total_effort += cell_effort
                total_fire_put_out += int(cell[1])
        elif cell[0] == "Medium " and int(cell[1]) in range(51, 80 + 1):
            if water_qtity >= int(cell[1]):
                water_qtity -= int(cell[1])
                cell_effort = int(cell[1]) * 0.25
                print(" -", int(cell[1]))
                total_effort += cell_effort
                total_fire_put_out += int(cell[1])
        elif cell[0] == "Low " and int(cell[1]) in range(1, 50 + 1):
            if water_qtity >= int(cell[1]):
                water_qtity -= int(cell[1])
                cell_effort = int(cell[1]) * 0.25
                print(" -", int(cell[1]))
                total_effort += cell_effort
                total_fire_put_out += int(cell[1])
        cell_count -= 1
        if total_fire_put_out >= water_qtity:
            is_water_available = False

print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire_put_out}")
