# def reverse_string(idx, string, reversed_string):
#     if abs(idx) > len(string):
#         print(f'{string} = {reversed_string}')
#         return
#     reversed_string += string[idx]
#     return reverse_string(idx - 1, string, reversed_string)
#
#
# string = input()
#
# while string != 'end':
#     reverse_string(-1, string, '')
#     string = input()

string = input()

while string != 'end':
    reversed_str = ""
    for symbol in reversed(string):
        reversed_str += symbol
    print(f'{string} = {reversed_str}')
    string = input()
