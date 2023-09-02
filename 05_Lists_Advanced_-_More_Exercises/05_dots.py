rows_of_board = 6
board_view = []
for _ in range(rows_of_board):
    line = input().split()
    board_view.append(line)

print(*board_view, sep="\n")
# 6 - 18
# . . - . - .
# - . . . . .
# - . - - - -
# - . . - - -
# - . . . . -
# - - - . . -
