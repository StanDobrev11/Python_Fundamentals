n_1 = int(input())
n_2 = int(input())
n_3 = int(input())

num_list = [n_1, n_2, n_3]

count = 0
is_negative = False
is_positive = False
is_zero = False

for item in num_list:
    if item < 0:
        count += 1
    elif item == 0:
        is_zero = True

if count % 2 == 0:
    is_positive = True
else:
    is_negative = True

if is_zero:
    print("zero")
elif is_negative:
    print("negative")
elif is_positive:
    print("positive")
