class Participant:
    def __init__(self, name):
        self.name = name
        self.topics_dict = {}
        self.ttl_score = 0

    # def __gt__(self, other):
    #     return self.ttl_score < other.ttl_score

    def add_score(self, course, score):
        if course not in self.topics_dict:
            self.topics_dict[course] = score
            self.ttl_score -= score
        else:
            if score < self.topics_dict[course]:
                self.ttl_score += self.topics_dict[course]
                self.topics_dict[course] = score
                self.ttl_score -= score


participants = {}
competition = {}

command = input()
while command != 'no more time':
    username, contest, points = command.split(' -> ')
    points = -int(points)
    if contest not in competition:
        competition[contest] = []

    if username not in participants:
        participants[username] = Participant(username)

    participants[username].add_score(contest, points)
    command = input()

for user in participants:
    for topic in participants[user].topics_dict:
        if topic in competition:
            competition[topic].append((user, participants[user].topics_dict[topic]))
for topic in competition:
    competition[topic].sort(key=lambda tup: tup[0])
    print(f'{topic}: {len(competition[topic])} participants')
    count = 1
    for name, score in sorted(competition[topic], key=lambda x: (x[1], x[0])):
        print(f'{count}. {name} <::> {abs(score)}')
        count += 1

sorted_participants = []
for user in participants:
    sorted_participants.append((participants[user].name, participants[user].ttl_score))

sorted_participants.sort(key=lambda x: (-x[1], x[0]))

print('Individual standings:')
count = 1
for user in sorted_participants:
    print(f'{count}. {user[0]} -> {abs(user[1])}')
    count += 1
