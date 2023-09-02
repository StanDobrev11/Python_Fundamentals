def correct(lst, item_1, item_2):
    """if the item with the given old name exists, change its name with the new one.
    Otherwise, skip this command."""
    if item_1 in lst:
        lst[lst.index(item_1)] = item_2
    return lst


def urgent(lst, item_1):
    """add the item at the start of the list.
    If the item already exists, skip this command"""
    if item_1 not in lst:
        lst.insert(0, item_1)
    return lst


def unnecessary(lst, item_1):
    """remove the item with the given name, only if it exists in the list.
    Otherwise, skip this command."""
    if item_1 in lst:
        lst.remove(item_1)
    return lst


def rearrange(lst, item_1):
    """if the grocery exists in the list, remove it from its current position and
    add it at the end of the list. Otherwise, skip this command."""
    if item_1 in lst:
        lst.remove(item_1)
        lst.append(item_1)
    return lst


shopping_list = input().split('!')

command = input()
while command != "Go Shopping!":
    command = command.split()
    item = command[1]
    if command[0] == 'Correct':
        old_item, new_item = command[1], command[2]
        shopping_list = correct(shopping_list, old_item, new_item)

    elif command[0] == 'Urgent':
        shopping_list = urgent(shopping_list, item)

    elif command[0] == 'Unnecessary':
        shopping_list = unnecessary(shopping_list, item)
    elif command[0] == 'Rearrange':
        shopping_list = rearrange(shopping_list, item)
    command = input()

print(*shopping_list, sep=", ")
