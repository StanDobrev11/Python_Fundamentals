def char_in_range(start, end):
    for char in range(ord(start) + 1, ord(end)):
        print(chr(char), end=" ")


start = input()
end = input()

char_in_range(start, end)