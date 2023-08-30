key = input().split()

coded_msg = input()
while coded_msg != 'find':
    decrypted_msg = ''
    key_idx = 0
    for idx, ch in enumerate(coded_msg):

        if key_idx >= len(key):
            key_idx = 0
        decrypted_msg += chr(ord(ch) - int(key[key_idx]))
        key_idx += 1

    treasure = ''
    coordinates = ''
    is_found = False
    for idx, ch in enumerate(decrypted_msg):
        if ch == '&' and not is_found:
            idx += 1
            while decrypted_msg[idx] != '&':
                treasure += decrypted_msg[idx]
                idx += 1
                is_found = True
        elif ch == "<":
            while ch != '>':
                idx += 1
                coordinates += decrypted_msg[idx]
                ch = decrypted_msg[idx + 1]

            print(f'Found {treasure} at {coordinates}')

    coded_msg = input()
