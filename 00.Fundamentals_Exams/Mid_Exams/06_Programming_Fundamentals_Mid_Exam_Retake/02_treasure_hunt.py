def loot(chest_list: list, commands_list: list):
    """Pick up treasure loot along the way. Insert the items at the beginning of the chest.
If an item is already contained, don't insert it.
    """
    commands_list.pop(0)
    # commands_list.reverse()
    for _ in range(len(commands_list)):
        if commands_list[0] in chest_list:
            commands_list.pop(0)
        else:
            chest_list.insert(0, commands_list.pop(0))
    return chest_list


def drop(chest_list: list, index):
    """Remove the loot at the given position and add it at the end of the treasure chest.
If the index is invalid, skip the command.
"""
    if index in range(len(chest_list)):
        chest_list.append(chest_list.pop(index))
    return chest_list


def steal(chest_list: list, qtity_of_items):
    """Someone steals the last count loot items. If there are fewer items than the given count,
    remove as much as there are.
    """
    if len(chest_list) <= qtity_of_items:
        print(*chest_list, sep=', ')
        chest_list.clear()
    else:
        stolen_list = chest_list[-qtity_of_items:]
        chest_list = chest_list[:-qtity_of_items]
        print(*stolen_list, sep=', ')
    return chest_list


def unpack(chest_list):
    single_level_chest = []
    for item in chest_list:
        if type(item) is list:
            single_level_chest.extend(item)
        else:
            single_level_chest.append(item)
    return single_level_chest


chest = input().split('|')

command = input()
while command != 'Yohoho!':
    command = command.split()
    if command[0] == 'Loot':
        chest = loot(chest, command)
    elif command[0] == 'Drop':
        chest = drop(chest, int(command[1]))
    elif command[0] == 'Steal':
        chest = steal(chest, int(command[1]))
    # print(chest)
    command = input()

if len(chest) == 0:
    print("Failed treasure hunt.")
else:
    count = 0
    chest = unpack(chest)
    for item in chest:
        count += len(item)
    average_gain = count / len(chest)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
