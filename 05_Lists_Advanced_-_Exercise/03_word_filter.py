line = input()

even_elements = list(filter(lambda x: len(x) % 2 == 0, line.split()))

for element in even_elements:
    print(element)
