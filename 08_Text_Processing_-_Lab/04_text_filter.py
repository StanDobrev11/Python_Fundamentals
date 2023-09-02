banned_words = [word for word in input().split(', ')]
text = input()

for word in banned_words:
    if word in text:
        symbols = '*' * len(word)
        text = text.replace(word, symbols)

print(text)