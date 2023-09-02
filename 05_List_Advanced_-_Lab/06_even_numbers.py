num_lst = input()
# num_lst = num_lst.split(', ')

# num_indices = [num_lst.index(element) for element in num_lst if int(element) % 2 == 0]
# num_indices = []
# for  element in num_lst:
#     if int(element) % 2 ==0:
#         num_indices.append(num_lst.index(element))

# print(num_indices)

num_lst = list(map(int, num_lst.split(', ')))
# # num_indices = [num_lst.index(element) for element in num_lst if element % 2 == 0]
found_or_no = list(map(lambda x: x if num_lst[x] % 2 == 0 else "no", range(len(num_lst))))
#
# even_list = list(filter(lambda y: y != "no", found_or_no))
even_list = [found_or_no.index(element) for element in found_or_no if element != "no"]
# print(found_or_no)
print(even_list)
