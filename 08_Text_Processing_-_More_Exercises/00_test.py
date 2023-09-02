# code = input().split()
#
# # .- -... -.-. -.. . ..-. --. .... .. --. -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..
# dict_code = {}
# num = 65
# letter = chr(num)
# for item in code:
#     letter = chr(num)
#     dict_code[item] = letter
#     num += 1
#
# print(dict_code)

new_code = input().split('/')

dict_code = {}
num = 65

for item in new_code:
    letter = chr(num)
    dict_code[item] = letter
    num += 1

print(dict_code)