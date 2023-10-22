phones = [x for x in input().split(', ')]

command = input()

while command != 'End':
    command, phone = command.split(' - ')

    if command == "Add":
        if phone not in phones:
            phones.append(phone)

    elif command == "Remove":
        if phone in phones:
            phones.remove(phone)

    elif command == "Bonus phone":
        old_phone, new_phone = phone.split(':')
        if old_phone in phones:
            old_phone_idx = phones.index(old_phone)
            phones.insert(old_phone_idx + 1, new_phone)

    elif command == "Last":
        try:
            idx = phones.index(phone)
            phones.pop(idx)
            phones.append(phone)
        except ValueError:
            pass

    command = input()

print(', '.join(phones))


"""
SamsungA50, MotorolaG5, IphoneSE
Add - Iphone10
Remove - IphoneSE
End

SamsungA50, MotorolaG5, HuaweiP10
Last - SamsungA50
Add - MotorolaG5
Last - Pinkp
End
"""