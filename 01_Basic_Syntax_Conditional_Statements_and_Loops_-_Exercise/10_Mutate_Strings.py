string_1 = input()
string_2 = input()

list_string_1 = list(string_1)
list_string_2 = list(string_2)

for i in range(len(string_1)):
    if list_string_1[i] != list_string_2[i]:
        list_string_1[i] = list_string_2[i]
        print("".join(list_string_1))
