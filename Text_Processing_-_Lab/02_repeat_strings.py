sequence = [string for string in input().split()]

result_string = ''
for string in sequence:
    n = len(string)
    result_string += string * n

print(result_string)

