class NQueen:
    def __init__(self, a):
        self.N = a

    def print_solution(self, board):
        for i in range(self.N):
            for j in range(self.N):
                print(" " + str(board[i][j]) + " ", end="")
            print()

    def is_safe(self, grid, row, col):
        for i in range(col):
            if grid[row][i] == 1:
                return False

        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if grid[i][j] == 1:
                return False

        for i, j in zip(range(row, self.N), range(col, -1, -1)):
            if grid[i][j] == 1:
                return False

        return True

    def solve_nq_util(self, grid, col):
        if col >= self.N:
            return True

        for i in range(self.N):
            if self.is_safe(grid, i, col):
                grid[i][col] = 1

                if self.solve_nq_util(grid, col + 1):
                    return True

                grid[i][col] = 0

        return False

    def solve_nq(self):
        grid = [[0] * self.N for _ in range(self.N)]

        if not self.solve_nq_util(grid, 0):
            print("Solution does not exist for", self.N, "queens")
            return False

        print("Solution found for", self.N, "queens")
        self.print_solution(grid)
        return True


def main():
    n = int(input("Number of queens to place: "))
    queen = NQueen(n)
    queen.solve_nq()


if __name__ == "__main__":
    main()
