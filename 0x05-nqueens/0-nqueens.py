#!/usr/bin/python3
""" N Queens Problem Solver """
import sys


class NQueen:
    """ Class to solve the N Queens problem """

    def __init__(self, n):
        """ Initialize the NQueen solver """
        self.n = n
        self.x = [0 for i in range(n + 1)]
        self.res = []

    def place(self, k, i):
        """ Check if a queen can be placed at position (k, i)
        """

        # j checks from 1 to k - 1 (Up to previous queen)
        for j in range(1, k):
            # There is already a queen in column
            # or a queen in same diagonal
            if self.x[j] == i or \
               abs(self.x[j] - i) == abs(j - k):
                return 0
        return 1

    def nQueen(self, k):
        """ Solve the N Queens problem using backtracking
        Args:
        k (int): Current row number
        """
        # i goes from column 1 to column n (1st column is 1st index)
        for i in range(1, self.n + 1):
            if self.place(k, i):
                # Queen can be placed in i column
                self.x[k] = i
                if k == self.n:
                    # Placed all 4 Queens (A solution was found)
                    solution = []
                    for i in range(1, self.n + 1):
                        solution.append([i - 1, self.x[i] - 1])
                    self.res.append(solution)
                else:
                    # Need to place more Queens
                    self.nQueen(k + 1)
        return self.res


# Main

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

N = sys.argv[1]

try:
    N = int(N)
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

queen = NQueen(N)
res = queen.nQueen(1)

for i in res:
    print(i)
