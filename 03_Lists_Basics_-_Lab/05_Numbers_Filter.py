number_of_iterations = int(input())

even_list = []
odd_list = []
positive_list = []
negative_list = []
for each in range(number_of_iterations):
    number = int(input())
    if number >= 0:
        positive_list.append(number)
        if number % 2 == 0:
            even_list.append(number)
        else:
            odd_list.append(number)
    else:
        negative_list.append(number)
        if number % 2 == 0:
            even_list.append(number)
        else:
            odd_list.append(number)

dict_lists = {"even": even_list,
              "odd": odd_list,
              "negative": negative_list,
              "positive": positive_list}
type_of_list = input()

print(dict_lists[type_of_list])
