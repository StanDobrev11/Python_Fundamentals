rows = int(input())

maze = []

for _ in range(rows):
    maze.append([x for x in input()])

cols = len(maze[0])
for row in range(rows):
    for col in range(cols):
        if maze[row][col] == 'k':
            start_row, start_col = row, col

path = []


def find_kate(row, col, maze, path, count):
    if row not in range(len(maze)) or col not in range(len(maze[0])):
        path.append(count)
        count = 0
        return
    if maze[row][col] == '#':
        return
    if maze[row][col] == 'v':
        return
    maze[row][col] = 'v'
    count += 1

    find_kate(row+1, col, maze, path, count)
    find_kate(row-1, col, maze, path, count)
    find_kate(row, col+1, maze, path, count)
    find_kate(row, col-1, maze, path, count)

    maze[row][col] = ' '



count = 0

find_kate(start_row, start_col, maze, path, count)

if len(path) == 0:
    print('Kate cannot get out')
    # print(path)
else:
    print(f'Kate got out in {max(path)} moves')
    # print(path)
