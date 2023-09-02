number = int(input())

total = 0
for x in range(1, number // 2 + 1):
    if number % x == 0:
        total += x
# total += list(x for x in range(1, number // 2 + 1) if number % x == 0)

if total == number:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")

