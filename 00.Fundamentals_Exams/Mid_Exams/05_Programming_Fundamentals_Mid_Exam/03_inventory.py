def collect(lst: list, itm):
    """- you should add the given item to your inventory.
    If the item already exists, you should skip this line."""
    if itm not in lst:
        lst.append(itm)
    return lst


def drop(lst: list, itm):
    """you should remove the item from your inventory if it exists."""
    if itm in lst:
        lst.remove(itm)
    return lst


def renew(lst: list, itm):
    """if the given item exists,
    you should change its position and put it last in your inventory."""
    if itm in lst:
        lst.remove(itm)
        lst.append(itm)
    return lst


def combine_items(lst: list, itm_1, itm_2):
    """you should check if the old item exists.
    If so, add the new item after the old one. Otherwise, ignore the command."""
    if itm_1 in lst:
        lst.insert(lst.index(itm_1) + 1, itm_2)
    return lst


craft_list = input().split(", ")

command = input()
while command != "Craft!":
    command = command.split(' - ')
    item = command[1]
    if command[0] == "Collect":
        craft_list = collect(craft_list, item)
    elif command[0] == "Drop":
        craft_list = drop(craft_list, item)
    elif command[0] == "Combine Items":
        item_1, item_2 = command[1].split(":")
        craft_list = combine_items(craft_list, item_1, item_2)
    elif command[0] == "Renew":
        craft_list = renew(craft_list, item)

    command = input()

print(*craft_list, sep=", ")