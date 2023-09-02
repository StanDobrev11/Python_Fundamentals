# import time
n = int(input())
people = []
for x in range(1, n + 1):
    people.append(str(x))

# people = input()
killed_every = int(input())
key = killed_every
# people = people.split()
killed = []
while len(people) != 0:
    for each_iteration in range(len(people)):
        if killed_every - len(people) > 0:
            killed_every -= len(people)
            for each in killed:
                if each in people:
                    people.remove(each)
                # print(people)
        else:
            killed.append(people[killed_every - 1])
            killed_every += key

print(f'[{",".join(killed)}]')
