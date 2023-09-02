def check_x(x1, x2):
    if abs(x1) <= abs(x2):
        return int(x1)
    else:
        return int(x2)


def check_y(y1, y2):
    if abs(y1) <= abs(y2):
        return int(y1)
    else:
        return int(y2)


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

x_min = check_x(x1, x2)
y_min = check_y(y1, y2)

if abs(x1) == abs(x2) and abs(y1) == abs(y2):
    print(f"({int(x1)}, {int(y1)})")
else:
    print(f"({x_min}, {y_min})")
