number_of_iterations = int(input())

bracket_count = 0
is_balanced = True
for each in range(number_of_iterations):
    symbol = input()
    if symbol == "(":
        bracket_count += 1
    if symbol == ")" and (bracket_count < 0 or bracket_count > 1):
        is_balanced = False
    if symbol == ")":
        bracket_count -= 1

if bracket_count == 0 and is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
