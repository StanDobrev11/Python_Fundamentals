def add(people):
    train_list[-1] += people


def insert(train_wagon, people):
    train_list[train_wagon] += people


def leave(train_wagon, people):
    train_list[train_wagon] -= people


train_length = int(input())
train_list = [0 for wagon in range(train_length)]
command = input()
while command != "End":
    command = command.split()
    if command[0] == "add":
        add(int(command[1]))
    elif command[0] == "insert":
        insert(int(command[1]), int(command[2]))
    elif command[0] == "leave":
        leave(int(command[1]), int(command[2]))
    command = input()

print(train_list)
