text_string = input()

command = input()
while command != 'Done':
    command = command.split()
    if command[0] == 'Cut':
        idx = int(command[1])
        length = int(command[2])
        substring = text_string[idx:idx + length]
        text_string = text_string.replace(substring, '')
        print(text_string)
    elif command[0] == 'TakeOdd':
        mod_str = ''
        for idx in range(1, len(text_string), 2):
            mod_str += text_string[idx]
        text_string = mod_str
        print(text_string)
    elif command[0] == 'Substitute':
        old_str, new_str = command[1], command[2]
        if old_str in text_string:
            text_string = text_string.replace(old_str, new_str)
            print(text_string)
        else:
            print('Nothing to replace!')

    command = input()

print(f'Your password is: {text_string}')
