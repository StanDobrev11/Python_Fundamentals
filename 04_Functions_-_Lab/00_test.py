# def string_multiplier(string, multiplier):
#     return lambda a, b: a * b

# print(string_multiplier("abc", 3))


# x = lambda a, b: a * b
# print(x("abc", 3))

# def str_multi(n):
#     return lambda a: a * n
#
# multi_str = str_multi(3)
# print(multi_str("abc"))
#
#
# string = input()
# multi = int(input())
#
# print((lambda a, b: a * b)(string, multi))

# lst = [2, 4, 8, 16]
#
#
# new_lst = list(map(lambda x, y: x * y, lst, lst))
# print(new_lst)
#
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new_list = list(filter(lambda x: x % 2 == 0, lst))
# print(new_list)
# new_list = []
# new_list = [i for i in lst if i % 2 == 0]
# new_list.append(str(i) for i in lst)
# print(new_list)

# print([x for x in range(5)])
#
# print((x for x in range(5)))
#
# print(tuple(range(5)))
# lis = [1, 2, 3, 4, 5]
# my_iter = iter(lis)
# print(my_iter)
# print(next(my_iter))
# print(next(my_iter))
# StopIteration
