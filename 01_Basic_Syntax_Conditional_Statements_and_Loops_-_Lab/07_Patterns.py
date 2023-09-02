number = int(input())

# top
for row in range(1, number + 1):
    print("*" * row)

# bottom
for row in range(number - 1, 0, -1):
    print("*" * row)
