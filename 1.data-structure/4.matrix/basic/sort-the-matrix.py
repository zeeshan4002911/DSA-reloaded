"""
Given an NxN matrix Mat. Sort all elements of the matrix.

Example 1:

Input:
N=4
Mat=[[10,20,30,40],
[15,25,35,45]
[27,29,37,48]
[32,33,39,50]]
Output:
10 15 20 25
27 29 30 32
33 35 37 39
40 45 48 50
Explanation:
Sorting the matrix gives this result.

Example 2:

Input:
N=3
Mat=[[1,5,3],[2,8,7],[4,6,9]]
Output:
1 2 3
4 5 6
7 8 9
Explanation:
Sorting the matrix gives this result.

Your Task:
You don't need to read input or print anything. Your task is to complete the function sortedMatrix() which takes the integer N and the matrix Mat as input parameters and returns the sorted matrix.


Expected Time Complexity:O(N^2 * LogN)
Expected Auxillary Space:O(N^2)


Constraints:
1<=N<=1000
1<=Mat[i][j]<=10^5
"""

import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pretty_print_matrix as helper


class Solution:
    # TC - O(N^2 * LogN), SC - O(N^2)
    def sort_matrix(self, mat, n):
        rows = cols = n
        flatten_mat = []

        for i in range(rows):
            for j in range(cols):
                flatten_mat.append(mat[i][j])
        flatten_mat.sort()
        k = 0
        for i in range(rows):
            for j in range(cols):
                mat[i][j] = flatten_mat[k]
                k += 1
        return mat

    # TC - O((N x N) x (N x N)), SC - O(1)
    def sort_matrix_inplace(self, mat, n):
        size = n * n
        """
        # Index mapping
        row, col = index / col, index % col
        """

        for _ in range(size):
            for j in range(size - 1):
                curr_row = j // n
                curr_col = j % n
                next_row = (j + 1) // n
                next_col = (j + 1) % n
                if mat[curr_row][curr_col] > mat[next_row][next_col]:
                    # Swap for bubble sort
                    (mat[curr_row][curr_col], mat[next_row][next_col]) = (
                        mat[next_row][next_col],
                        mat[curr_row][curr_col],
                    )


def main():
    n = int(input("Enter size of matrix: ").strip())
    print("Enter the matrix")
    mat = [list(map(int, input().strip().split()))[:n] for _ in range(n)]
    solution = Solution()
    solution.sort_matrix(mat, n)
    helper.pretty_print_matrix(mat)


if __name__ == "__main__":
    main()
