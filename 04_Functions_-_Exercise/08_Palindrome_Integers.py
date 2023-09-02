string = input()
string = string.split(", ")

for each in string:
    each_reversed = each[::-1]
    if each_reversed == each:
        print(True)
    else:
        print(False)
