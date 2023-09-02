string = input()

string = string.split()
opposite_list = []
for index in range(len(string)):
    number = int(string[index])
    opposite_number = number * -1
    opposite_list.append(opposite_number)

print(opposite_list)
