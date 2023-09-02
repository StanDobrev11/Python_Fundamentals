vowels = ['a', 'o', 'u', 'e', 'i']

string_input = input()
# string_input = string_input.lower()
# for symbol in string_input:
#     if symbol not in vowels:
#         string_output += symbol
#
# print(string_output)
# test_2 = ""
# output = ["".join(symbol for symbol in string_input.lower() if symbol not in vowels)]
# # test_2 += str(symbol for symbol in string_input if symbol not in vowels)
# print(*output)
#

string_output = "".join([symbol for symbol in string_input.lower() if symbol not in vowels])
print(string_output)