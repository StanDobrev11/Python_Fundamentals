type_of_input = input()
value_of_input = input()

result = ""
if type_of_input == "integer":
    result = int(value_of_input) + 1
elif type_of_input == "real":
    result = f"{1 + float(value_of_input):.2f}"
else:
    result = str(value_of_input) + "*"

print(result)
