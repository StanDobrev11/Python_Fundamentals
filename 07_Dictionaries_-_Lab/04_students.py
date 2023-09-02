command = input()

student_by_id = {}
courses = {}
while len(command.split(':')) > 1:
    name, id, course = command.split(':')
    student_by_id[id] = name

    if course not in courses:
        courses[course] = []
    courses[course].append(id)

    command = input()

target_course = command
if '_' in target_course:
    target_course = target_course.replace('_', ' ')

if target_course in courses:
    for id in courses[target_course]:
        print(f'{student_by_id[id]} - {id}')
