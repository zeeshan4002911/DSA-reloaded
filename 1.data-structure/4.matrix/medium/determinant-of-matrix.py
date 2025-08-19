"""
Given a square matrix of size n*n. The task is to find the determinant of this matrix.

Example 1:

Input:
n = 4
matrix[][] = {{1, 0, 2, -1},
              {3, 0, 0, 5},
              {2, 1, 4, -3},
              {1, 0, 5, 0}}
Output: 30
Explanation:
Determinant of the given matrix is 30.

Example 2:

Input:
n = 3
matrix[][] = {{1, 2, 3},
              {4, 5, 6},
              {7, 10, 9}}
Output: 12
Explanation:
Determinant of the given matrix is 12.
1 * (5*9 - 6 * 10) - 2 * (4 * 9 - 7 * 6) + 3 * (4 * 10 - 7 * 5)

Your Task:
You don't need to read input or print anything. Complete the function determinantOfMatrix() that takes matrix and its size n as input parameters and returns the determinant of the matrix.

Expected Time Complexity: O(N^4)
Expected Auxiliary Space: O(N^2)

Constraints:
1 <= N <= 10
-10 <= mat[i][j] <= 10
"""


class Solution:
    def calculate_determinant(self, mat, n):
        # Edge case for matrix size 1 x 1
        if n == 1:
            return mat[0][0]

        # Base case to stop recursion for 2 x 2 matrix size
        elif n == 2:
            return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]

        result = 0
        for col in range(n):
            
            # Creation of minor matrix, without the first row and the column of cofactor
            sub_mat = [[0] * (n - 1) for _ in range(n - 1)]
            for i in range(1, n):
                k = 0
                for j in range(n):
                    if j == col:
                        continue
                    sub_mat[i - 1][k] = mat[i][j]
                    k += 1

            # Add/Subtract based on laplace expansion formula starting from +ve sign
            if col % 2 == 0:
                result += mat[0][col] * self.calculate_determinant(sub_mat, n - 1)
            else:
                result -= mat[0][col] * self.calculate_determinant(sub_mat, n - 1)

        return result


def main():
    n = int(input("Enter the size of matrix: ").strip())
    print("Enter first matrix")
    mat = [list(map(int, input().strip().split()))[:n] for _ in range(n)]

    solution = Solution()
    print(solution.calculate_determinant(mat, n))


if __name__ == "__main__":
    main()


"""
## Laplace Expansion Formula example :
The cofactor of an element is a matrix that we can get by removing the row and column of that element from that matrix.

     A = | a b c |
         | d e f |
         | g h i |

Expanding along the first row.

     det(A) = a * |e f| - b * |d f| + c * |d e|
                  |h i|       |g i|       |g h|
"""
