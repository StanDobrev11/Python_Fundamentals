letters = input().split(', ')
# dictionary = {}
# for letter in letters:
#     if letter not in dictionary:
#         dictionary[letter] = ord(letter)

test_dict = {x: ord(x) for x in letters}
# print(dictionary)

print(test_dict)
