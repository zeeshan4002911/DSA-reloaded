"""
Given an incomplete Sudoku configuration in terms of a 9x9  2-D square matrix(mat[][]) the task to check if the current configuration is valid or not where a 0 represents an empty block.
Note: Current valid configuration does not ensure validity of the final solved sudoku.

Examples:

Input: mat[][] = [
[3, 0, 6, 5, 0, 8, 4, 0, 0]
[5, 2, 0, 0, 0, 0, 0, 0, 0]
[0, 8, 7, 0, 0, 0, 0, 3, 1]
[0, 0, 3, 0, 1, 0, 0, 8, 0]
[9, 0, 0, 8, 6, 3, 0, 0, 5]
[0, 5, 0, 0, 9, 0, 6, 0, 0]
[1, 3, 0, 0, 0, 0, 2, 5, 0]
[0, 0, 0, 0, 0, 0, 0, 7, 4]
[0, 0, 5, 2, 0, 6, 3, 0, 0]
]
Output: true
Explaination: It is possible to have aproper sudoku.

Input: mat[][] = [
[3, 0, 3, 5, 0, 8, 4, 0, 0]
[5, 2, 0, 0, 0, 0, 0, 0, 0]
[0, 8, 7, 0, 0, 0, 0, 3, 1]
[0, 0, 3, 0, 1, 0, 0, 8, 0]
[9, 0, 0, 8, 6, 3, 0, 0, 5]
[0, 5, 0, 0, 9, 0, 6, 0, 0]
[1, 3, 0, 0, 0, 0, 2, 5, 0]
[0, 0, 0, 0, 0, 0, 0, 7, 4]
[0, 0, 5, 2, 0, 6, 3, 0, 0]
]
Output: false
Explaination: It is not possible to have aproper sudoku.

Input: mat[][] = [
[2, 0, 2, 5, 0, 8, 4, 0, 0]
[5, 2, 0, 0, 0, 0, 0, 0, 0]
[0, 8, 7, 0, 0, 0, 0, 3, 1]
[0, 0, 3, 0, 1, 0, 0, 8, 0]
[9, 0, 0, 8, 6, 3, 0, 0, 5]
[0, 5, 0, 0, 9, 0, 6, 0, 0]
[1, 3, 0, 0, 0, 0, 2, 5, 0]
[0, 0, 0, 0, 0, 0, 0, 7, 4]
[0, 0, 5, 2, 0, 6, 3, 0, 0]
]
Output: false
Explaination: It is not possible to have aproper sudoku.

Constraints:
0 ≤ mat[i][j] ≤ 9

Expected Complexities
Time Complexity: O(n^2)
Auxiliary Space: O(1)
"""


class Solution:
    def is_sudoku_valid(self, mat):
        # Fixed Array for storing the count of chunk/sub matrix number occurrence of sudoku
        row_mark_arr = [0] * 9
        col_mark_arr = [0] * 9
        sub_matrix_mark_arr = [0] * 9

        # starting index pointers for 3 x 3 sub matrix
        for i in range(9):

            p, q = 0, 0
            for j in range(9):
                row_ele = mat[i][j]
                if row_ele > 0:
                    row_mark_arr[row_ele - 1] += 1

                col_ele = mat[j][i]
                if col_ele > 0:
                    col_mark_arr[col_ele - 1] += 1

                # Index mapping modified formula
                r = (i // 3) * 3 + p
                c = (i % 3) * 3 + q

                # Incrementing the pointer of row and column to iterate over 3 x 3 sub matrix
                q += 1
                if q >= 3:
                    q = 0
                    p += 1

                sub_matrix_ele = mat[r][c]
                if sub_matrix_ele > 0:
                    sub_matrix_mark_arr[sub_matrix_ele - 1] += 1

            # Check of presence of 1-9 digits for each row and column of matrix
            row_col_check_result = (
                self.check_mark_arr(row_mark_arr)
                and self.check_mark_arr(col_mark_arr)
                # and self.check_mark_arr(sub_matrix_mark_arr)
            )

            # Reset of count array for next row/column iteration
            self.reset_mark_arr(row_mark_arr)
            self.reset_mark_arr(col_mark_arr)
            self.reset_mark_arr(sub_matrix_mark_arr)

            # In case of more than one same digit presence for any row/column
            if row_col_check_result is False:
                return False

        return True

    def check_mark_arr(self, count_arr):
        for count in count_arr:
            if count > 1:
                return False
        return True

    def reset_mark_arr(self, count_arr):
        for i in range(9):
            count_arr[i] = 0


def main():
    print("Enter th sudoku matrix")
    mat = [list(map(int, input().strip().split()))[:9] for _ in range(9)]

    solution = Solution()
    result = solution.is_sudoku_valid(mat)
    print(result)


if __name__ == "__main__":
    main()
