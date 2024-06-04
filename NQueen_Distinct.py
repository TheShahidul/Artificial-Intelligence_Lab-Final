class NQueen:
    def __init__(self, a):
        self.N = a
        self.solutions = []

    def print_solution(self, board):
        for i in range(self.N):
            for j in range(self.N):
                print(" " + str(board[i][j]) + " ", end="")
            print()
        print()
                                            #shahidul_213902017
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
            self.solutions.append([row[:] for row in grid])
            return

        for i in range(self.N):
            if self.is_safe(grid, i, col):
                grid[i][col] = 1
                self.solve_nq_util(grid, col + 1)
                grid[i][col] = 0

    def solve_nq(self):
        grid = [[0] * self.N for _ in range(self.N)]
        self.solve_nq_util(grid, 0)
        return self.solutions


def main():
    n = int(input("Number of queens to place: "))
    queen = NQueen(n)
    solutions = queen.solve_nq()
    print("Total distinct solutions:", len(solutions))
    for idx, solution in enumerate(solutions, start=1):
        print("Solution", idx)
        queen.print_solution(solution)


if __name__ == "__main__":
    main()
