n = int(input())

score_book = {}
for _ in range(n):

    name = input()
    grade = float(input())
    if name not in score_book:
        score_book[name] = []

    score_book[name].append(grade)

for key, value in score_book.items():
    average = sum(value) / len(value)
    if average >= 4.5:
        print(f'{key} -> {average:.2f}')