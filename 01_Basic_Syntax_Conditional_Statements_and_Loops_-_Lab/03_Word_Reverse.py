word = input()

reversed_word = word[::-1]

reversed_word_1 = ""
for i in range(len(word) - 1, -1, -1):
    reversed_word_1 += word[i]

print(reversed_word)
print(reversed_word_1)
