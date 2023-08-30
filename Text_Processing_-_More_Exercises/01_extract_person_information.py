n = int(input())

for _ in range(n):
    raw_text = input()
    name = ''
    age = ''
    for idx, ch in enumerate(raw_text):
        if ch == '@':
            while ch != '|':
                idx += 1
                name += raw_text[idx]
                ch = raw_text[idx + 1]
        elif ch == "#":
            while ch != '*':
                idx += 1
                age += raw_text[idx]
                ch = raw_text[idx + 1]
    print(f'{name} is {age} years old.')
