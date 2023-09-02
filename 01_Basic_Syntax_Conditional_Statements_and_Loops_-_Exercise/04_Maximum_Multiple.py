divisor = int(input())
boundary = int(input())

max_divisible = 1
for x in range(boundary, 0, -1):
    if x % divisor == 0:
        print(x)
        break
