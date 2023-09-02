string = input()
string = string.split()

abs_string = list(map(abs, list(map(float, string))))
print(abs_string)
