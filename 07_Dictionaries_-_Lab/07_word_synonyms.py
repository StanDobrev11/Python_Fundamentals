n = int(input())

dict1 = {}
for _ in range(n):
    key = input()
    value = input()
    if key not in dict1:
        dict1[key] = []
    dict1[key].append(value)
# lst = []
# for iteration in range(2 * n):
#     lst.append(input())
#
# dict1 = {}
#
# for idx in range(0, len(lst), 2):
#     key = lst[idx]
#     value = lst[idx + 1]
#     if key not in dict1:
#         dict1[key] = []
#     dict1[key].append(value)

for key, value in dict1.items():
    print(f'{key} - {", ".join(value)}')

