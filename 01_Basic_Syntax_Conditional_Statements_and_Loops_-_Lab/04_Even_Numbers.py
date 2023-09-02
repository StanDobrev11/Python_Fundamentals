initial_count = int(input())

number = 0
is_even = False
for num in range(initial_count):
    number = int(input())
    if number % 2 == 1:
        print(f"{number} is odd!")
        # is_even = False
        break
else:
    # is_even = True
    print("All numbers are even.")


# if is_even:
#     print("All numbers are even.")
# else:
#     print(f"{number} is odd!")
