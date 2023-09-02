command = input()

users = {}
while command != 'End':
    company, user_id = command.split(' -> ')
    if company not in users:
        users[company] = []
    if user_id not in users[company]:
        users[company].append(user_id)

    command = input()

for key, value in users.items():
    print(key)
    for item in value:
        print(f'-- {item}')