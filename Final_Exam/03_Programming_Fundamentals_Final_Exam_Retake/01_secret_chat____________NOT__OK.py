coded_msg = input()

command = input()
while command != 'Reveal':
    command = command.split(':|:')
    if command[0] == 'InsertSpace':
        idx = int(command[1])
        coded_msg = coded_msg[0:idx] + ' ' + coded_msg[idx:]
        print(coded_msg)

    elif command[0] == 'Reverse':
        substring = command[1]
        if substring in coded_msg:
            start_idx = coded_msg.index(substring)
            end_idx = start_idx + len(substring)
            substring = substring[::-1]
            coded_msg = coded_msg[:start_idx] + substring + coded_msg[end_idx:]
            print(coded_msg)
        else:
            print('error')

    elif command[0] == 'ChangeAll':
        substring, replacement = command[1], command[2]
        if substring in coded_msg:
            coded_msg = coded_msg.replace(substring, replacement)
            print(coded_msg)

    command = input()

print(f'You have a new text message: {coded_msg}')
