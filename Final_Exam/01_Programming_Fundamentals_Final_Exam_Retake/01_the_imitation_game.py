def change_all(substring, new_string, coded_msg):
    for ch in substring:
        coded_msg = coded_msg.replace(ch, new_string)
    return coded_msg


def insert(idx, symbol_to_insert, coded_msg):
    coded_msg = coded_msg[0:idx] + symbol_to_insert + coded_msg[idx:]
    return coded_msg


def move_it(letters_to_move, coded_msg):
    symbols_to_move = coded_msg[0:letters_to_move]
    coded_msg = coded_msg[letters_to_move:] + symbols_to_move
    return coded_msg


coded_msg = input()

command = input()

while not command == 'Decode':
    command = command.split('|')
    if command[0] == 'ChangeAll':
        substring = command[1]
        new_string = command[2]
        coded_msg = change_all(substring, new_string, coded_msg)
    elif command[0] == 'Insert':
        idx = int(command[1])
        symbol_to_insert = command[2]
        coded_msg = insert(idx, symbol_to_insert, coded_msg)
    elif command[0] == 'Move':
        letters_to_move = int(command[1])
        coded_msg = move_it(letters_to_move, coded_msg)

    command = input()

print(f'The decrypted message is: {coded_msg}')
