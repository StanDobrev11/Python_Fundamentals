count = int(input())
f_1 = 1
f_2 = 1
f_3 = 2
result = ""
if count >= 3:
    result = "1 1 2 "
    for _ in range(count - 3):
        f_next = f_3 + f_2 + f_1
        f_1 = f_2
        f_2 = f_3
        f_3 = f_next
        result += str(f_next) + " "
elif count == 2:
    result = "1 1"
elif count == 1:
    result = "1"
else:
    result = "0"

print(result)