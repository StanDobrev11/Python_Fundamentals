gift_lst = input().split()

command = input()

while not command == 'No Money':
    command = command.split()
    if command[0] == 'OutOfStock':
        gift_name = command[1]
        for gift in gift_lst:
            if gift == gift_name:
                gift_idx = gift_lst.index(gift_name)
                gift_lst[gift_idx] = 'None'
    elif command[0] == 'Required':
        gift_name, gift_idx = command[1], int(command[2])
        if gift_idx in range(len(gift_lst)):
            gift_lst[gift_idx] = gift_name
    elif command[0] == 'JustInCase':
        gift_name = command[1]
        gift_lst[-1] = gift_name

    command = input()

for gift in gift_lst:
    if gift == 'None':
        gift_lst.remove(gift)

print(' '.join(gift_lst))
