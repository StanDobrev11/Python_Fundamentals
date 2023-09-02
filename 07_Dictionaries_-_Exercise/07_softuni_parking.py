class User:
    def __init__(self, name, plate_no=''):
        self.name = name
        self.plate_no = plate_no

    def register(self, reg):
        if user.name in reg:
            print(f'ERROR: already registered with plate number {user.plate_no}')
            return
        reg[user.name] = user.plate_no
        print(f'{user.name} registered {user.plate_no} successfully')


n = int(input())
reg = {}

for idx in range(n):
    command = input().split()

    if command[0] == 'register':
        user = User(command[1], command[2])
        user.register(reg)
    else:

        if command[1] not in reg:
            print(f'ERROR: user {command[1]} not found')
        else:
            del reg[command[1]]
            print(f'{command[1]} unregistered successfully')

for user in reg:
    print(f'{user} => {reg[user]}')
