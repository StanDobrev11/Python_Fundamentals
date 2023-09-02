command = input()

force_book = {}
while command != 'Lumpawaroo':
    if ' | ' in command:
        is_valid = True
        force_side, force_user = command.split(' | ')
        if force_side not in force_book:
            force_book[force_side] = []
        for key, value in force_book.items():
            if force_user in value:
                is_valid = False
        if is_valid:
            force_book[force_side].append(force_user)

    elif ' -> ' in command:
        force_user, force_side = command.split(' -> ')
        for key, value in force_book.items():
            if force_user in value:
                wrong_side = key
                force_book[wrong_side].remove(force_user)
        force_book[force_side].append(force_user)
        print(f'{force_user} joins the {force_side} side!')

    command = input()

for key, values in force_book.items():
    if len(values) == 0:
        continue
    else:
        print(f"Side: {key}, Members: {len(values)}")
        for user in values:
            print(f'! {user}')
