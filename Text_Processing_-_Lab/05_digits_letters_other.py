string = input()

nums = ''
letters = ''
symbols = ''
for ch in string:
    if ch.isdigit():
        nums += ch
    elif ch.isalpha():
        letters += ch
    else:
        symbols += ch

print(nums)
print(letters)
print(symbols)
