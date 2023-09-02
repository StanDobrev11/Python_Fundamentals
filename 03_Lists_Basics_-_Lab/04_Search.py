number_of_strings = int(input())
key_word = input()

list_of_phrases = []
list_key_word = []
for each in range(number_of_strings):
    phrase = input()
    list_of_phrases.append(phrase)
    if key_word in phrase:
        list_key_word.append(phrase)

print(list_of_phrases)
print(list_key_word)
