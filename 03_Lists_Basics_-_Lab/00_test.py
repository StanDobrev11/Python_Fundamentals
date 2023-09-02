def positive():
    for i in range(len(number_list) - 1, -1, -1):
        item = number_list[i]
        if item < 0:
            number_list.remove(item)


number_list = [0, 5, 2, -1, 4, -8, 7]

positive()
print(number_list)
