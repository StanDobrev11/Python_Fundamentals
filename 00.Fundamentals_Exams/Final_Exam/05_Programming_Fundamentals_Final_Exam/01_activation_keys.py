def flip(activation_key, morph_to, start_idx, end_idx):
    morphed_string = ''
    if morph_to == 'Upper':
        morphed_string = activation_key[start_idx:end_idx].upper()
    else:
        morphed_string = activation_key[start_idx:end_idx].lower()

    return activation_key[0:start_idx] + morphed_string + activation_key[end_idx:]


def slice_it(activation_key, start_idx, end_idx):
    return activation_key[0:start_idx] + activation_key[end_idx:]


activation_key = input()

command = input()

while command != 'Generate':
    command = command.split('>>>')
    if command[0] == 'Contains':
        substring = command[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif command[0] == 'Flip':
        morph_to, start_idx, end_idx = command[1], int(command[2]), int(command[3])
        activation_key = flip(activation_key, morph_to, start_idx, end_idx)
        print(activation_key)
    elif command[0] == 'Slice':
        start_idx, end_idx = int(command[1]), int(command[2])
        activation_key = slice_it(activation_key, start_idx, end_idx)
        print(activation_key)
    command = input()

print(f'Your activation key is: {activation_key}')
