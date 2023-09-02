elements = input().split()

bakery = {}

# while elements:
#     bakery[elements[0]] = int(elements[1])
#     elements.pop(0)
#     elements.pop(0)
for i in range(0, len(elements), 2):
    key = elements[i]
    value = elements[i + 1]
    bakery[key] = int(value)

print(bakery)
