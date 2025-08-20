"""
Given a square matrix, find the adjoint and inverse of the matrix.

Adjoint (or Adjugate) of a matrix is the matrix obtained by taking the transpose of the cofactor matrix of a given square matrix is called its Adjoint or Adjugate matrix. The Adjoint of any square matrix 'A' (say) is represented as Adj(A).

Example:

5  -2  2  7
1   0  0  3
-3  1  5  0
3  -1 -9  4
For instance, the cofactor of the top left corner '5' is
 + |0   0   3|
...|1   5   0| = 3(1 * -9 - (-1) * 5) = -12.
...|-1 -9   4|
(The minor matrix is formed by deleting the row
 and column of the given entry.)
As another sample, the cofactor of the top row corner '-2' is
  -|1   0  3|
...|-3  5  0| = - [1 (20 - 0) - 0 + 3 (27 - 15)] = -56.
...|3  -9  4|
Proceeding like this, we obtain the matrix
[-12  -56   4   4]
[76   208   4   4]
[-60  -82  -2  20]
[-36  -58  -10 12]
Finally, to get the adjoint, just take the previous
matrix's transpose:
[-12   76 -60  -36]
[-56  208 -82  -58]
[4     4   -2  -10]
[4     4   20   12]
"""

import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pretty_print_matrix as helper


class Solution:
    def calculate_adjoint(self, mat):
        # Adjoint matrix will be Transpose of matrix which is having cofactor matrix determinant for each element
        n = len(mat)
        adj = [[0] * n for _ in range(n)]

        if n == 1:
            adj[0][0] = 1
            return

        for i in range(n):
            for j in range(n):
                cofactor_mat = self.get_cofactor(mat, i, j, n)
                # Sign change due to Transpose
                sign = +1 if (i + j) % 2 == 0 else -1
                # Placing cofactor determinant of i, j to j, i for Transpose
                adj[j][i] = sign * self.calculate_determinant(cofactor_mat)

        return adj

    def calculate_inverse(self, mat, adj):
        """
        Formula: A ^ -1 = Adj|A| / det(A)
        """
        det = self.calculate_determinant(mat)

        if det == 0:
            return "Signular matrix, determinant is 0."

        n = len(adj)
        inv = [[round(adj[i][j] / det, 2) for j in range(n)] for i in range(n)]
        return inv

    def get_cofactor(self, mat, row, col, n):
        # Creation of minor matrix, without the row and the column of cofactor
        sub_mat = [[0] * (n - 1) for _ in range(n - 1)]
        p = 0
        q = 0
        for i in range(n):
            for j in range(n):
                if i == row or j == col:
                    continue
                sub_mat[p][q] = mat[i][j]
                q += 1
                if q == n - 1:
                    q = 0
                    p += 1

        return sub_mat

    def calculate_determinant(self, mat):
        n = len(mat)
        # Edge case for matrix size 1 x 1
        if n == 1:
            return mat[0][0]

        # Base case to stop recursion for 2 x 2 matrix size
        elif n == 2:
            return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]

        result = 0
        for col in range(n):
            cofactor_mat = self.get_cofactor(mat, 0, col, n)
            # Add/Subtract based on laplace expansion formula starting from +ve sign
            sign = +1 if col % 2 == 0 else -1
            result += sign * mat[0][col] * self.calculate_determinant(cofactor_mat)

        return result


def main():
    n = int(input("Enter the size of matrix: ").strip())
    print("Enter matrix")
    mat = [list(map(int, input().strip().split()))[:n] for _ in range(n)]

    solution = Solution()
    adj = solution.calculate_adjoint(mat)
    print("Adjoint/Adjugate Matrix")
    helper.pretty_print_matrix(adj)

    result = solution.calculate_inverse(mat, adj)
    print("Inverse of Matrix")
    if isinstance(result, str):
        print(result)
    else:
        helper.pretty_print_matrix(result)


if __name__ == "__main__":
    main()
