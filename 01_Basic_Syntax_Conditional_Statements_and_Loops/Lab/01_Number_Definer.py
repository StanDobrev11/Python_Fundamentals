number = float(input())

first_word = ""
second_word = ""
if number == 0:
    print("zero")
elif number < 0:
    second_word = 'negative'
else:
    second_word = 'positive'

if number != 0 and abs(number) < 1:
    first_word = "small "
elif number != 0 and abs(number) > 1000000:
    first_word = "large "

print(f"{first_word}{second_word}")
