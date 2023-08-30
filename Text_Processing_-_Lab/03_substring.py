# def popped_string(key_idx, key_string, target_string):
#     result_string = ''
#     if key_idx >= len(key_string):
#         print(target_string)
#         return
#
#     for letter in target_string:
#         if letter != key_string[key_idx]:
#             result_string += letter
#
#     return popped_string(key_idx + 1, key_string, result_string)
#
#
# key_string = input()
# target_string = input()
#
# popped_string(0, key_string, target_string)

# key_str = input()
# target_str = input()
#
# while key_str in target_str:
#     start_idx = target_str.index(key_str)
#     end_idx = target_str.index(key_str) + len(key_str)
#
#     result_string = target_str[0:start_idx] + target_str[end_idx:]
#     target_str = result_string
#
# print(target_str)

key_str = input()
target_str = input()

while key_str in target_str:
    target_str = target_str.replace(key_str, '')

print(target_str)
