command_list = ["coding", "dog", "cat", "movie"]
coffee = 0
while True:
    multiply = 1
    commands = input()
    if commands == "END":
        break
    if commands.isupper():
        multiply = 2

    commands = commands.lower()
    if commands in command_list:
        coffee += 1 * multiply

if coffee > 5:
    print("You need extra sleep")
else:
    print(coffee)
