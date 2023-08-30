text = input()

result_text = text[0]
for idx in range(1, len(text)):
    if text[idx] == text[idx - 1]:
        continue
    result_text += text[idx]

print(result_text)
