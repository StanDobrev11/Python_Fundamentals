to_do = input()
rate = [0] * 10
todos_nums = []
list_todos = []
while to_do != "End":
    list_todos.append(to_do)
    to_do = input()
list_todos.sort()
for el in list_todos:
    if "10" in el:
        rem = el
        list_todos.remove(el)
        list_todos.append(rem)
new_list = []
for item in list_todos:
    item = item.split("-")
    new_list.append(item[1])

print(new_list)
# while True:
#     to_do = input()
#     if to_do == "End":
#         break
#     to_do = to_do.split("-")
#     priority = int(to_do[0]) - 1
#     rate.pop(priority)
#     rate.insert(priority, to_do[1])
#
# rate = [element for element in rate if element != 0]
# print(rate)