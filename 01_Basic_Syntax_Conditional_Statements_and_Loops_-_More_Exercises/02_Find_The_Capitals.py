string = input()

string = list(string)
index = []
# for each_item in string:
#     if each_item.isupper():
#         index.append(string.index(each_item))
for each_item in range(len(string)):
    if string[each_item].isupper():
        index.append(each_item)

print(index)
