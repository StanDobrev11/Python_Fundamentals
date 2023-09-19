from math import sqrt


def distance_to_center():
    # Determines the point closest to the center (0, 0).
    # Returns final converted longest line.
    line_to_check = compare_lines()
    compare_distance_to_center = []
    for line in line_to_check:
        x = line[0]
        y = line[1]
        compare_distance_to_center.append(sqrt((x ** 2) + (y ** 2)))
    convert_0 = tuple(map(int, line_to_check[0]))
    convert_1 = tuple(map(int, line_to_check[1]))
    if compare_distance_to_center[0] > compare_distance_to_center[1]:
        return f"{convert_1}{convert_0}"
    elif compare_distance_to_center[0] <= compare_distance_to_center[1]:
        return f"{convert_0}{convert_1}"


def length_of_line(coordinates):
    # calculates length and returns length of lines
    diff_x = coordinates[0][0] - coordinates[1][0]
    diff_y = coordinates[0][1] - coordinates[1][1]
    diff = sqrt((diff_x ** 2) + (diff_y ** 2))
    # print(diff)
    return diff


def compare_lines():
    # compares length of lines and returns longest line
    if length_of_line(list_of_lines[0]) >= length_of_line(list_of_lines[1]):
        return list_of_lines[0]
    else:
        return list_of_lines[1]


number_of_lines = 2
list_of_lines = []
for line in range(number_of_lines):
    x1 = float(input())
    y1 = float(input())
    x2 = float(input())
    y2 = float(input())

    point_1 = [x1, y1]
    point_2 = [x2, y2]
    line_as_list = [point_1, point_2]
    list_of_lines.append(line_as_list)

print(distance_to_center())
