text = input()

for idx, symbol in enumerate(text):
    if symbol == ':':
        emoticon = ':' + text[idx + 1]
        print(emoticon)
