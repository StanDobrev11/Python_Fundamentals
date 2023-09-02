first_row = input()
second_row = input()
third_row = input()

first_row = first_row.split()
second_row = second_row.split()
third_row = third_row.split()

winner = ""
# check horizontal
if first_row[0] == first_row[1] == first_row[2]:
    if first_row[0] == "1":
        winner = "First"
    elif first_row[0] == "2":
        winner = "Second"
elif second_row[0] == second_row[1] == second_row[2]:
    if second_row[0] == "1":
        winner = "First"
    elif second_row[0] == "2":
        winner = "Second"
elif third_row[0] == third_row[1] == third_row[2]:
    if third_row[0] == "1":
        winner = "First"
    elif third_row[0] == "2":
        winner = "Second"

# check vertical
if first_row[0] == second_row[0] == third_row[0]:
    if first_row[0] == "1":
        winner = "First"
    elif first_row[0] == "2":
        winner = "Second"
elif first_row[1] == second_row[1] == third_row[1]:
    if first_row[1] == "1":
        winner = "First"
    elif first_row[1] == "2":
        winner = "Second"
elif first_row[2] == second_row[2] == third_row[2]:
    if first_row[2] == "1":
        winner = "First"
    elif first_row[2] == "2":
        winner = "Second"

# check diagonal
if first_row[0] == second_row[1] == third_row[2]:
    if first_row[0] == "1":
        winner = "First"
    elif first_row[0] == "2":
        winner = "Second"
elif first_row[2] == second_row[1] == third_row[0]:
    if first_row[2] == "1":
        winner = "First"
    elif first_row[2] == "2":
        winner = "Second"

if winner != "":
    print(f"{winner} player won")
else:
    print("Draw!")
