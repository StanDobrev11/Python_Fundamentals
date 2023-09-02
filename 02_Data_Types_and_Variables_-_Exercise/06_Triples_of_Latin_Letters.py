number = int(input())

for i_1 in range(ord("a"), ord("a") + number):
    for i_2 in range(ord("a"), ord("a") + number):
        for i_3 in range(ord("a"), ord("a") + number):
            print(f"{chr(i_1)}{chr(i_2)}{chr(i_3)}")
