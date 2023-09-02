key = int(input())
number_of_symbols = int(input())

result = ""
for each_symbol in range(number_of_symbols):
    coded = input()
    decoded = ord(coded) + key
    result += chr(decoded)

print(result)
