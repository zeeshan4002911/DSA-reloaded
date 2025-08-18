"""
You are given two square matrices, a[][] and b[][], each of size n x n. Your task is to compute the sum of these two matrices and store the result in the matrix a[][] itself.

Examples:

Input: a[][] = [[1, 2], [3, 4]],
       b[][] = [[4, 3], [2, 1]]
Output: [[5, 5], [5, 5]]
Explanation: The will be: [[5, 5], [5, 5]] on adding the corresponding elements of both matrices.

Input: a[][] = [[7, 8], [9, 10]],
       b[][] = [[1, 2], [3, 4]]
Output: [[8, 10], [12, 14]]
Explanation: The result will be [[8, 10], [12, 14]] after adding the corresponding elements of both matrices.

Constraints:
1 <= n <= 100

Expected Complexities
Time Complexity: O(n^2)
Auxiliary Space: O(1)
"""

import os, sys

# Adding parent path to path to access helper file
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pretty_print_matrix as helper


class Solution:
    def addition_of_matrices(self, mat_1, mat_2, n):
        result = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                result[i][j] = mat_1[i][j] + mat_2[i][j]
        
        return result


def main():
    n = int(input("Enter the size of matrix: ").strip())
    print("Enter first matrix")
    mat_1 = [list(map(int, input().strip().split()))[:n] for _ in range(n)]
    print("Enter second matrix")
    mat_2 = [list(map(int, input().strip().split()))[:n] for _ in range(n)]

    solution = Solution()
    result = solution.addition_of_matrices(mat_1, mat_2, n)
    helper.pretty_print_matrix(result)


if __name__ == "__main__":
    main()
