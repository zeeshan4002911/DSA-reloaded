"""
Given a matrix mat[][] of size n x m, the task is to traverse this matrix using recursion.
Examples:

    Input: mat[][] = [[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]]
    Output: 1 2 3 4 5 6 7 8 9

    Input: mat[][] = [[11, 12, 13],
                     [14, 15, 16],
                     [17, 18, 19]]
    Output: 11 12 13 14 15 16 17 18 19
"""


class Solution:
    def flatten_matrix(self, mat, row, col):
        return self.traverse_matrix_rec_helper(mat, 0, 0, row, col, [])

    def traverse_matrix_rec_helper(self, mat, i, j, row, col, result):
        if i >= row:
            return result

        result.append(mat[i][j])

        # Chaning the i and j for iteration on matrix
        j += 1
        if j == col:
            i += 1
            j = 0

        return self.traverse_matrix_rec_helper(mat, i, j, row, col, result)


def main():
    row = int(input("Enter the Row of matrix: ").strip())
    col = int(input("Enter the Column of matrix: ").strip())
    print("Enter first matrix")
    mat = [list(map(int, input().strip().split()))[:col] for _ in range(row)]

    solution = Solution()
    print(solution.flatten_matrix(mat, row, col))


if __name__ == "__main__":
    main()
