initial_count = int(input())

txt = ""
for x in range(initial_count):
    number = int(input())
    if number == 88:
        txt = "Hello"
    elif number == 86:
        txt = "How are you?"
    elif number < 88:
        txt = "GREAT!"
    else:
        txt = "Bye."
        # print(txt)
        # break
    print(txt)

