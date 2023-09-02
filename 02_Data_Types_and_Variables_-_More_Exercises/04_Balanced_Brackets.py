number_of_iterations = int(input())

bracket_count = 0
is_balanced = True
for each in range(number_of_iterations):
    symbol = input()
    if symbol == "(":
        if bracket_count != 0:
            is_balanced = False
        bracket_count += 1
    elif symbol == ")":
        bracket_count -= 1
        if bracket_count < 0:
            is_balanced = False

if bracket_count == 0 and is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
