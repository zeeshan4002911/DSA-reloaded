"""
Given a square matrix mat[][], the task is to swap the elements of the major and minor diagonals.

    Major Diagonal: Elements that lie from the top-left corner to the bottom-right corner of the matrix (i.e., where row index equals column index).

    Minor Diagonal: Elements that lie from the top-right corner to the bottom-left corner (i.e., where the sum of row and column indices equals n - 1).

Examples:

Input: mat[][] = [[0, 1, 2],
                [3, 4, 5],
                [6, 7, 8]]
Output: [[2, 1, 0],
        [3, 4, 5],
        [8, 7, 6]]
Explanation: Major Diagonal = [0, 4, 8], Minor Diagonal = [2, 4, 6]. We are required to swap the diagonal elements of same row, thus after doing so, major diagonal will become minor and vice-versa.

Input: mat[][] = [[2, 3],
                [5, 4]]
Output: [[3, 2],
         [4, 5]]
Explanation: Major Diagonal = [2, 4], Minor Diagonal = [3, 5]. We are required to swap the diagonal elements of same row, thus after doing so, major diagonal will become minor and vice-versa.

Constraints:
1 ≤ mat.size() ≤ 500
1 ≤ mat[i][j] ≤ 10^6

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)
"""

import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pretty_print_matrix as helper


class Solution:
    def swap_diagonals(self, mat):
        size = len(mat)

        for i in range(size):
            # Column index for minor diagonal element
            j = size - 1 - i
            # Swap of diagonal elements
            mat[i][i], mat[i][j] = mat[i][j], mat[i][i]

        return mat


def main():
    n = int(input("Enter the size: ").strip())
    print("Enter the matrix")
    mat = [list(map(int, input().strip().split()))[:n] for _ in range(n)]

    solution = Solution()
    solution.swap_diagonals(mat)
    helper.pretty_print_matrix(mat)


if __name__ == "__main__":
    main()
