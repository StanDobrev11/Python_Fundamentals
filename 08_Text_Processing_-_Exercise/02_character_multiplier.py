list_strings = [x for x in input().split()]

min_len = len(list_strings[0]) if len(list_strings[0]) <= len(list_strings[1]) else len(list_strings[1])

remaining_str = ''
for string in list_strings:
    if len(string) == min_len:
        continue

    remaining_str = string[min_len:]

result = 0
for idx in range(min_len):
    result += ord(list_strings[0][idx]) * ord(list_strings[1][idx])

for symbol in remaining_str:
    result += ord(symbol)

print(result)
