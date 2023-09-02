def out_of_stock(gift):
    for item in range(len(list_to_buy)):
        if list_to_buy[item] == gift:
            list_to_buy[item] = "None"


def required(gift, index):
    is_valid = True
    while is_valid:
        try:
            list_to_buy[index] = gift
            break
        except IndexError:
            is_valid = False


def just_in_case(gift):
    list_to_buy[-1] = gift


gifts_to_buy = input()

list_to_buy = gifts_to_buy.split()
have_money = True
while have_money:
    command = input()
    if command == "No Money":
        have_money = False
        break
    command = command.split()
    if command[0] == "OutOfStock":
        gift = command[1]
        out_of_stock(gift)
    elif command[0] == "Required":
        gift = command[1]
        index = int(command[2])
        required(gift, index)
    elif command[0] == "JustInCase":
        gift = command[1]
        just_in_case(gift)

for i in range(len(list_to_buy)):
    if "None" in list_to_buy:
        list_to_buy.remove("None")

print(*list_to_buy)
