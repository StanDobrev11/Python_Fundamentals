command = input()

by_score = {}
by_language = {}
while command != 'exam finished':
    command = command.split('-')
    if 'banned' in command:
        username = command[0]
        del by_score[username]
        command = input()
        continue
    username, language, points = command
    if username not in by_score:
        by_score[username] = []
    by_score[username].append(int(points))
    if language not in by_language:
        by_language[language] = []
    by_language[language].append(username)

    command = input()

print('Results:')
for key, value in by_score.items():
    print(f'{key} | {max(value)}')
print('Submissions:')
for key, value in by_language.items():
    print(f'{key} - {len(value)}')
