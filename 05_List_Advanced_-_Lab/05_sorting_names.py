names_lst = input()
names_lst = names_lst.split(', ')
names_lst.sort()

names_lst.sort(reverse=True, key=len)
print(names_lst)