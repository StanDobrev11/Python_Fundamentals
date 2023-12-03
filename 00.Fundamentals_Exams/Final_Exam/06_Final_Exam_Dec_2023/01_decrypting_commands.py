coded_str = input()

command_line = input()

while command_line != 'Finish':

    command, *rest = command_line.split()

    if command == 'Replace':
        old_ch, new_ch = rest
        coded_str = coded_str.replace(old_ch, new_ch)
        print(coded_str)

    elif command == 'Cut':
        start, end = [int(x) for x in rest]
        if start not in range(len(coded_str)) or end not in range(len(coded_str)):
            print("Invalid indices!")
            command_line = input()
            continue

        coded_str = coded_str[:start] + coded_str[end + 1:]
        print(coded_str)

    elif command == "Make":

        result = ''
        for sym in coded_str:
            if rest[0] == 'Upper':
                result += sym.upper()
            else:
                result += sym.lower()

        coded_str = result
        print(coded_str)

    elif command == 'Check':

        if rest[0] in coded_str:
            print(f"Message contains {rest[0]}")
        else:
            print(f"Message doesn't contain {rest[0]}")

    elif command == 'Sum':
        start, end = [int(x) for x in rest]

        if start not in range(len(coded_str)) or end not in range(len(coded_str)):
            print("Invalid indices!")
            command_line = input()
            continue

        substring = coded_str[start:end + 1]
        ttl_sum = 0
        for sym in substring:
            ttl_sum += ord(sym)

        print(ttl_sum)

    command_line = input()
