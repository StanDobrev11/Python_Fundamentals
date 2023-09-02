secret_message = input()
secret_message = secret_message.split()
decoded_message = []
for element in secret_message:
    element = list(element)
    number_in_element = "".join(list(filter(lambda x: x.isdigit(), element)))

    for _ in range(len(number_in_element)):
        element.pop(0)
    element.insert(0, chr(int(number_in_element)))
    element[1], element[-1] = element[-1], element[1]
    decoded_message.append("".join(element))

print(*decoded_message)