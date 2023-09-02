start_with = int(input())
ends_with = int(input())

result = ""
for index in range(start_with, ends_with + 1):
    chrt = chr(index)
    result += chrt + " "

print(result)
    