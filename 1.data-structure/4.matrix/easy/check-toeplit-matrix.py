"""
Given a square matrix mat[][] of order n, your task is to check if it is a Toeplitz Matrix.

Note: A Toeplitz matrix - also called a diagonal-constant matrix - is a matrix where elements of every individual descending diagonal are same from left to right. Equivalently, for any entry mat[i][j], it is same as mat[i-1][j-1] or mat[i-2][j-2] and son on.

Examples:

    Input: mat[][] = [[6, 7, 8],
                     [4, 6, 7]
                     [1, 4, 6]]
    Output: Yes
    Explanation: All the diagonals of the given matrix are [6, 6, 6], [7, 7], [8], [4, 4], [1]. For every diagonal, as all the elements are same, the given matrix is Toeplitz Matrix.

    Input: mat[][] = [[6, 3, 8],
                     [4, 9, 7]
                     [1, 4, 6]]
    Output: No
    Explanation: The primary diagonal elements of the given matrix are [6, 9, 6]. As the diagonal elements are not same, the given matrix is not Toeplitz Matrix.
"""


class Solution:
    def check_toeplit_matrix(self, mat):
        row = len(mat)
        col = len(mat[0])

        # Starting from the second row and second col element and checking the diagonally previous element
        for i in range(1, row):
            for j in range(1, col):
                if mat[i][j] != mat[i - 1][j - 1]:
                    return False

        return True


def main():
    n = int(input("Enter the size: ").strip())
    print("Enter the matrix")
    mat = [list(map(int, input().strip().split()))[:n] for _ in range(n)]

    solution = Solution()
    print(solution.check_toeplit_matrix(mat))


if __name__ == "__main__":
    main()
