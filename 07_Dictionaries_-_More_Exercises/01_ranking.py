from queue import PriorityQueue


class Student:
    def __init__(self, name):
        self.name = name
        self.topics_learned = {}
        self.ttl_score = 0

    def __gt__(self, other):
        return self.ttl_score > other.ttl_score

    def add_score(self, course, score):
        if course not in self.topics_learned:
            self.topics_learned[course] = score
            self.ttl_score -= score
        else:
            if score > self.topics_learned[course]:
                self.ttl_score += self.topics_learned[course]
                self.topics_learned[course] = score
                self.ttl_score -= score


command = input()
contest_passwords = {}
while command != "end of contests":
    contest, password = command.split(':')
    if contest not in contest_passwords:
        contest_passwords[contest] = password
    command = input()

command = input()
contest_participants = {}
students_score_book = {}
while command != "end of submissions":
    contest, password, participant, score = command.split('=>')
    if participant not in students_score_book:
        students_score_book[participant] = Student(participant)

    if contest not in contest_passwords:
        command = input()
        continue
    if contest_passwords[contest] == password:
        students_score_book[participant].add_score(contest, int(score))

    command = input()

pq = PriorityQueue()
for student in students_score_book:
    pq.put(students_score_book[student])

best_student = pq.get()

print(f"Best candidate is {best_student.name} with total {abs(best_student.ttl_score)} points.")
print('Ranking:')
for student in sorted(students_score_book):
    if students_score_book[student].ttl_score == 0:
        continue
    print(students_score_book[student].name)
    for topic in sorted(students_score_book[student].topics_learned,
                        key=lambda x: students_score_book[student].topics_learned[x],
                        reverse=True):
        print(f'#  {topic} -> {students_score_book[student].topics_learned[topic]}')
