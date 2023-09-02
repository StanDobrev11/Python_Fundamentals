string = input()
key = input()

str_list = string.split()
palindrome_lst = [el for el in str_list if el == el[::-1]]

print(palindrome_lst)
print(f'Found palindrome {palindrome_lst.count(key)} times')