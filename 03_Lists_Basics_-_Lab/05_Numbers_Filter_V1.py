def positive():
    for index in range(len(number_list) - 1, -1, -1):
        item = number_list[index]
        if item < 0:
            number_list.remove(item)
    return number_list


def negative():
    for index in range(len(number_list) - 1, -1, -1):
        item = number_list[index]
        if item >= 0:
            number_list.remove(item)
    return number_list


def even():
    for index in range(len(number_list) - 1, -1, -1):
        item = number_list[index]
        if item % 2 == 1:
            number_list.remove(item)
    return number_list


def odd():
    for index in range(len(number_list) - 1, -1, -1):
        item = number_list[index]
        if item % 2 == 0:
            number_list.remove(item)
    return number_list


number_of_iterations = int(input())

number_list = []
for each in range(number_of_iterations):
    number = int(input())
    number_list.append(number)

command = input()
if command == "positive":
    positive()
elif command == "negative":
    negative()
elif command == "even":
    even()
elif command == "odd":
    odd()

print(number_list)
