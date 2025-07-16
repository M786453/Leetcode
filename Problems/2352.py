from collections import Counter


class Solution:

    def equalPairs(self, grid):

        n = len(grid)

        equal_pairs = 0

        rows_dict = Counter([tuple(grid[i]) for i in range(n)])

        print(rows_dict)

        for i in range(n):

            col = tuple([grid[j][i] for j in range(n)])

            if col in rows_dict:

                equal_pairs += rows_dict[col]

        return equal_pairs
