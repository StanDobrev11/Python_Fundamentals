import re
from collections import deque

text = input()

pattern = r"(?<=(@|#))[A-Za-z]{3,}(\1{2})[A-Za-z]{3,}(?=\1)"

valid_data = [x.group() for x in re.finditer(pattern, text)]

matched_words = []

if not valid_data:
    print("No word pairs found!")
    print("No mirror words!")
    raise SystemExit

valid_data = deque(valid_data)
print(f"{len(valid_data)} word pairs found!")

while valid_data:
    pair = valid_data.popleft()
    pattern = r"[A-Za-z]{3,}"

    word, rev_word = re.findall(pattern, pair)

    if word == rev_word[::-1]:
        matched_words.append(f"{word} <=> {rev_word}")

if not matched_words:
    print("No mirror words!")
    raise SystemExit

print("The mirror words are:")
print(', '.join(matched_words))
