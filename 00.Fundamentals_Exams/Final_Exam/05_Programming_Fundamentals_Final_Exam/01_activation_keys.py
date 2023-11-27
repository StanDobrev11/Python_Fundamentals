def contains(substring: str):
    if substring in raw_key:
        print(f"{raw_key} contains {substring}")
    else:
        print("Substring not found!")

    return raw_key


def flip_it(case, *indices):  # Upper/Lower>>>{startIndex}>>>{endIndex}":
    """ Changes the substring between the given indices (the end index is exclusive)
    to upper or lower case and then prints the activation key """

    start_idx, end_idx = [int(x) for x in indices]

    substring = raw_key[start_idx:end_idx].upper() if case == 'Upper' else raw_key[start_idx:end_idx].lower()

    updated_key = raw_key[:start_idx] + substring + raw_key[end_idx:]
    print(updated_key)
    return updated_key


def slice_it(*indices):
    """ Deletes the characters between the start and end indices
    (the end index is exclusive) and prints the activation key """

    start_idx, end_idx = [int(x) for x in indices]

    updated_key = raw_key[:start_idx] + raw_key[end_idx:]
    print(updated_key)
    return updated_key


mapper = {
    'Contains': contains,
    'Flip': flip_it,
    'Slice': slice_it
}

raw_key = input()

command_line = input()

while command_line != 'Generate':
    command, *rest = command_line.split('>>>')

    if command in mapper:
        raw_key = mapper[command](*rest)

    command_line = input()

print(f"Your activation key is: {raw_key}")
