command = input()

study_program = {}

while command != 'end':
    course, student = command.split(' : ')
    if course not in study_program:
        study_program[course] = []

    study_program[course].append(student)
    command = input()

for key, value in study_program.items():
    print(f'{key}: {len(value)}')
    for name in value:
        print(f"-- {name}")
