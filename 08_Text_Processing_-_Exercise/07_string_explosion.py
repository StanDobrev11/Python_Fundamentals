raw_string = input()

force = 0
result_string = ""
for idx, symbol in enumerate(raw_string):
    if symbol == '>':
        force += int(raw_string[idx + 1])
        result_string += symbol
        continue
    if force > 0:
        force -= 1
        continue
    result_string += symbol

print(result_string)
