number_of_strings = int(input())
key_word = input()

list_of_phrases = []
list_key_word = []
for each in range(number_of_strings):
    phrase = input()
    list_of_phrases.append(phrase)

print(list_of_phrases)

for index in range(len(list_of_phrases) - 1, -1, -1):
    phrase = list_of_phrases[index]
    if key_word not in phrase:
        list_of_phrases.remove(phrase)

print(list_of_phrases)
