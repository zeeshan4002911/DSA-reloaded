"""
Given a square matrix mat[][] of order n*n, the task is to check if it is an Idempotent Matrix or not.

Idempotent matrix: A matrix is said to be an idempotent matrix if the matrix multiplied by itself returns the same matrix, i.e. the matrix mat[][] is said to be an idempotent matrix if and only if M * M = M.

Examples:

    Input: mat[][] = [[2, -2, -4],
                     [-1, 3, 4],
                     [1, -2, -3]]

    Output: True
    Explanation:  Given matrix if multiplied by itself returns the same matrix.
    Idempotent-Matrix



    Input: mat[][] = [[1, 2],
                     [3, 4]]
    Output: False
    Explanation: Given matrix if multiplied by itself returns the different matrix.
"""


class Solution:
    def check_idempotent_matrix(self, mat):
        n = len(mat)

        result = [[0] * n for _ in range(n)]

        # Matrix multiplication to itself (mat x mat)
        for i in range(n):
            for j in range(n):
                local_sum = 0
                for k in range(n):
                    local_sum += mat[i][k] * mat[k][j]
                result[i][j] = local_sum

        # Equality check between mat x mat and mat
        for i in range(n):
            for j in range(n):
                if result[i][j] != mat[i][j]:
                    return False

        return True


def main():
    n = int(input("Enter the size: ").strip())
    print("Enter the matrix")
    mat = [list(map(int, input().strip().split()))[:n] for _ in range(n)]

    solution = Solution()
    print(solution.check_idempotent_matrix(mat))


if __name__ == "__main__":
    main()
