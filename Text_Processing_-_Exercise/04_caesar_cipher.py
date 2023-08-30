phrase = input()

coded_string = ""
for ch in phrase:
    ch = ord(ch) + 3
    coded_string += chr(ch)

print(coded_string)
