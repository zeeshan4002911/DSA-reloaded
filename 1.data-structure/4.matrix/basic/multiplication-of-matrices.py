"""
You are given two square matrices mat1[][] and mat2[][], each of size n × n. You have to multiply these two matrices and return the resulting matrix.

Examples:

Input: mat1[][] = [[1, 1, 1], mat2[][] = [[1, 1, 1],
                  [1, 1, 1],             [1, 1, 1],
                  [1, 1, 1]]             [1, 1, 1]]
Output: [[3, 3, 3],
        [3, 3, 3],
        [3, 3, 3]]
Explanation: After multiplying mat1 and mat2 we get the resulting matrix equal to [[3, 3, 3], [3, 3, 3], [3, 3, 3]].

Input: mat1[][] = [[1, 2], mat2[][] = [[4, 3],
                  [3, 4]]             [2, 1]]
Output: [[8, 5],
        [20, 13]]
Explanation: After multiplying mat1 and mat2 we get the resulting matrix equal to [[8, 5], [20, 13]]

Constraints:
1 ≤ n ≤ 100
1 ≤ mat1[i][j], mat2[i][j] ≤ 100

Expected Complexities
Time Complexity: O(n^3)
Auxiliary Space: O(n^2)
"""

import os, sys

# Adding parent path to path to access helper file
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pretty_print_matrix as helper


class Solution:
    def multiplication_of_matrices(self, mat1, mat2):
        row1 = len(mat1)
        col1 = len(mat1[0])
        row2 = len(mat2)
        col2 = len(mat2[0])

        if col1 != row2:
            # Number of column of first matrix and number of rows of second matrix must be equal for multiplication
            return "ERROR - Unable to proceed with multiplication"

        result = [[0] * col2 for _ in range(row1)]

        for i in range(row1):
            for j in range(col2):
                local_sum = 0
                for k in range(row2):
                    local_sum += mat1[i][k] * mat2[k][j]
                result[i][j] = local_sum

        return result


def main():
    n = int(input("Enter the size of matrix: ").strip())
    print("Enter first matrix")
    mat_1 = [list(map(int, input().strip().split()))[:n] for _ in range(n)]
    print("Enter second matrix")
    mat_2 = [list(map(int, input().strip().split()))[:n] for _ in range(n)]

    solution = Solution()
    result = solution.multiplication_of_matrices(mat_1, mat_2)
    if isinstance(result, str):
        print(result)
    else:
        helper.pretty_print_matrix(result)


if __name__ == "__main__":
    main()


"""
## Multiplying a Matrix by Another Matrix ##

To multiply a matrix by another matrix we need to do the dot product of rows and columns ... what does that mean? Let us see with an example:

To work out the answer for the 1st row and 1st column:

Matrix Multiply Dot Product
[[1 2 3],  X  [[7 8],  =  [[58    ],
[4 5 6]]      [9 10],     [      ],
              [11 12]]    [      ]]

The dot product is where we multiply matching members, then sum up:
(1, 2, 3) • (7, 9, 11)= 1x7 + 2x9 + 3x11
= 58

We match the 1st members (1 and 7), multiply them, likewise for the 2nd members (2 and 9) and the 3rd members (3 and 11), and finally sum them up.
"""
