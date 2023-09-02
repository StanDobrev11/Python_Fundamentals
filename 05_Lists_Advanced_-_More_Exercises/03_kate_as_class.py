class EscapeMaze:
    def __init__(self):
        self.maze = self.input_maze()
        self.is_out = False

    @staticmethod
    def input_maze():
        rows_in_maze = int(input())
        return [list(input()) for _ in range(rows_in_maze)]

    def print_maze(self):
        print(*self.maze, sep="\n")
        print()
        print(em.find_kate())

    def check_row_len(self):
        pass

    def empty_space(self):
        pass

    def check_vertical(self):
        pass
        # check up
        # if
        # for row in self.maze:
        #     if self.maze.index(row) == em.find_kate()[0] - 1:




    def find_kate(self):
        for row in self.maze:
            for col in row:
                if "k" in col:
                    kate_row, kate_col = self.maze.index(row), row.index(col)
                    return kate_row, kate_col




if __name__ == "__main__":
    em = EscapeMaze()
    em.print_maze()

# 5
######
##  k#
## ###
## ###
## ###
