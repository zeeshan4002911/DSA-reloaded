"""
Given two integers M, N, and a 2D matrix Mat of dimensions MxN, clockwise rotate the elements in it.

Example 1:

Input:
M=3,N=3
Mat=[[1,2,3],[4,5,6],[7,8,9]]
Output:
4 1 2
7 5 3
8 9 6
Explanation:
Rotating the matrix clockwise gives this result.

Example 2:

Input:
M=2,N=3
Mat=[[1,2,3],[2,3,3]]
Output:
2 1 2
3 3 3
Explanation:
Rotating the matrix clockwise gives this result.


Your Task:
You don't need to read input or print anything. Your task is to complete the function rotateMatrix() which takes two integers M, N, and a 2D matrix as input parameters and returns the clockwise rotated matrix.


Expected Time Complexity:O(M*N)
Expected Auxillary Space:O(1)


Constraints:
1<=M,N,Mat[i][j]<=1000
"""

import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pretty_print_matrix as helper


class Solution:
    def rotate_matrix_by_1(self, mat, row, col):
        row_start, row_end = 0, row - 1
        col_start, col_end = 0, col - 1

        while row_start < row_end and col_start < col_end:
            # Boundary last clockwise element as prev_ele
            prev_ele = mat[row_start + 1][col_start]
            
            # Boundary top row iteration
            for j in range(col_start, col_end + 1):
                curr_ele = mat[row_start][j]
                mat[row_start][j] = prev_ele
                prev_ele = curr_ele
            row_start += 1

            # Boundary right column iteration
            for i in range(row_start, row_end + 1):
                curr_ele = mat[i][col_end]
                mat[i][col_end] = prev_ele
                prev_ele = curr_ele
            col_end -= 1

            if col > 1:
                # Boundary bottom row iteration
                for j in range(col_end, col_start - 1, -1):
                    curr_ele = mat[row_end][j]
                    mat[row_end][j] = prev_ele
                    prev_ele = curr_ele
                row_end -= 1

            if row > 1:
                # Boundary left column iteration
                for i in range(row_end, row_start - 1, -1):
                    curr_ele = mat[i][col_start]
                    mat[i][col_start] = prev_ele
                    prev_ele = curr_ele
                col_start += 1

        return mat


def main():
    n = int(input("Enter the row: ").strip())
    m = int(input("Enter the column: ").strip())
    print("Enter the matrix")
    mat = [list(map(int, input().strip().split()))[:m] for _ in range(n)]

    solution = Solution()
    solution.rotate_matrix_by_1(mat, n, m)
    helper.pretty_print_matrix(mat)


if __name__ == "__main__":
    main()
