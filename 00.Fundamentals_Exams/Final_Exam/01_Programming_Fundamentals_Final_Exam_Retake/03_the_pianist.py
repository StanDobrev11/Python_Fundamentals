class Piece:

    def __init__(self, name, composer, key):
        self.name = name
        self.composer = composer
        self.key = key


number_of_pieces = int(input())

list_of_plays = {}
for _ in range(number_of_pieces):
    name, composer, key = input().split('|')
    piece = Piece(name, composer, key)
    list_of_plays[name] = piece

command = input()

while not command == 'Stop':
    command = command.split('|')
    if command[0] == 'Add':
        name, composer, key = command[1], command[2], command[3]
        if name in list_of_plays:
            print(f'{name} is already in the collection!')
        else:
            list_of_plays[name] = Piece(name, composer, key)
            print(f'{name} by {composer} in {key} added to the collection!')
    elif command[0] == 'Remove':
        name = command[1]
        if name not in list_of_plays:
            print(f'Invalid operation! {name} does not exist in the collection.')
        else:
            del list_of_plays[name]
            print(f'Successfully removed {name}!')
    elif command[0] == 'ChangeKey':
        name, new_key = command[1], command[2]
        if name not in list_of_plays:
            print(f'Invalid operation! {name} does not exist in the collection.')
        else:
            list_of_plays[name].key = new_key
            print(f'Changed the key of {name} to {new_key}!')
    command = input()

for key, value in list_of_plays.items():
    print(f"{key} -> Composer: {value.composer}, Key: {value.key}")
