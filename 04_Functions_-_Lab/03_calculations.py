def calculator(oper, num_1, num_2):
    if oper == "multiply":
        return num_1 * num_2
    elif oper == "divide":
        return int(num_1 / num_2)
    elif oper == "add":
        return num_1 + num_2
    elif oper == "subtract":
        return num_1 - num_2


operator = input()
number_1 = float(input())
number_2 = float(input())

print(int(calculator(operator, number_1, number_2)))
