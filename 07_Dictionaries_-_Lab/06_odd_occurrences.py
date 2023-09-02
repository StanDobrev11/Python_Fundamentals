words = input().split()

for idx in range(len(words)):
    words[idx] = words[idx].lower()

to_print = []
for idx in range(len(words)):
    if words[idx] in to_print:
        continue
    word_count = words.count(words[idx])
    if word_count % 2 == 1:
        to_print.append(words[idx])

print(*to_print)
