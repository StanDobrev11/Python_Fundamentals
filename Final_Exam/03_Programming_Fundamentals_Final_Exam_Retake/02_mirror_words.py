import re

text_string = input()

pattern = r'(?<=(?P<sep>@|#))(?P<word>[A-Za-z]{3}([A-Za-z]+)?)(?P=sep){2}(?P<word1>[A-Za-z]{3}([A-Za-z]+)?)(?=(?P=sep))'

ttl_words = {}
matched_pairs = []
data = re.finditer(pattern, text_string)
for x in data:
    ttl_words[x.group('word')] = x.group('word1')

word_pairs = len(ttl_words)

for word, rev_word in ttl_words.items():
    if word == rev_word[::-1]:
        matched = f'{word} <=> {rev_word}'
        matched_pairs.append(matched)

if ttl_words:
    print(f'{word_pairs} word pairs found!')
    if matched_pairs:
        print('The mirror words are:')
        print(', '.join(matched_pairs))
    else:
        print('No mirror words!')
else:
    print('No word pairs found!')
    print('No mirror words!')
