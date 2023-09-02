string = input()

string = string.lower()
count = 0
count += string.count("sand")
count += string.count("water")
count += string.count("sun")
count += string.count("fish")

print(count)
