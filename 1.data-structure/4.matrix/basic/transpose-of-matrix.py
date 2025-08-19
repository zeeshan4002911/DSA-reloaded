"""
You are given a square matrix of size n x n. Your task is to find the transpose of the given matrix.
The transpose of a matrix is obtained by converting all the rows to columns and all the columns to rows.

Examples :

Input: mat[][] = [[1, 1, 1, 1],
                [2, 2, 2, 2],
                [3, 3, 3, 3],
                [4, 4, 4, 4]]
Output: [[1, 2, 3, 4],
       [1, 2, 3, 4],
       [1, 2, 3, 4],
       [1, 2, 3, 4]]
Explanation: Converting rows into columns and columns into rows.

Input: mat[][] =  [[1, 2],
                 [9, -2]]
Output: [[1, 9],
        [2, -2]]
Explanation: Converting rows into columns and columns into rows.

Constraints:
1 ≤ n ≤ 10^3
-109 ≤ mat[i][j] ≤10^9

Expected Complexities
Time Complexity: O(n^2)
Auxiliary Space: O(1)
"""

import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pretty_print_matrix as helper


class Solution:
    def transpose_of_square_matrix(self, mat):
        n = len(mat)

        # By swapping the diagonal element consider diagnal as axis for swap
        for i in range(n):
            # Starting from next to diagnoal column element to avoid swapping already swapped element
            # Swapping of diagnoal element is not required as it will remain there in transpose
            for j in range(i + 1, n):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

        return mat


def main():
    n = int(input("Enter the size of matrix: ").strip())
    print("Enter first matrix")
    mat = [list(map(int, input().strip().split()))[:n] for _ in range(n)]

    solution = Solution()
    solution.transpose_of_square_matrix(mat)
    helper.pretty_print_matrix(mat)


if __name__ == "__main__":
    main()
