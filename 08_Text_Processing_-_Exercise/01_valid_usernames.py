names = [name for name in input().split(', ')]

for name in names:
    if len(name) not in range(3, 17):
        continue
    if any(not (ch.isalnum() or ch == '-' or ch == '_') for ch in name):
        continue

    print(name)

# user_names = [name for name in input().split(', ')]
#
# for name in user_names:
#     if len(name) not in range(3, 17):
#         continue
#     is_valid = True
#
#     for ch in name:
#         if ch.isalnum() or ch == '-' or ch == '_':
#             continue
#         else:
#             is_valid = False
#             break
#
#     if is_valid:
#         print(name)


# user_names = [name for name in input().split(', ')]
# for name in user_names:
#     is_valid = True
#     if len(name) > 16 or len(name) < 3:
#         continue
#     if ' ' in name:
#         continue
#     for symbol in range(32, 45):
#         if chr(symbol) in name:
#             is_valid = False
#             break
#
#     for symbol in range(46, 48):
#         if chr(symbol) in name:
#             is_valid = False
#             break
#     for symbol in range(58, 65):
#         if chr(symbol) in name:
#             is_valid = False
#             break
#     for symbol in range(32, 44):
#         if chr(symbol) in name:
#             is_valid = False
#             break
#     for symbol in range(91, 95):
#         if chr(symbol) in name:
#             is_valid = False
#             break
#     for symbol in range(96, 97):
#         if chr(symbol) in name:
#             is_valid = False
#             break
#     for symbol in range(123, 128):
#         if chr(symbol) in name:
#             is_valid = False
#             break
#
#     if is_valid:
#         print(name)
