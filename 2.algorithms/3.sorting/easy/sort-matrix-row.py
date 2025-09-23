"""
Given a 2D array, sort each row of this array and print the result.

Examples:

Input : mar[][] = [ [77, 11, 22, 3],
                  [11, 89, 1, 12],
                  [32, 11, 56, 7],
                  [11, 22, 44, 33] ]
Output : mat[][] = [ [3, 11, 22, 77],
                   [1, 11, 12, 89],
                   [7, 11, 32, 56],
                   [11, 22, 33, 44] ]
Input : mat[][] = [ [8, 6, 4, 5],
                  [3, 5, 2, 1],
                  [9, 7, 4, 2],
                  [7, 8, 9, 5] ]
Output :mat[][] = [ [4, 5, 6, 8],
                  [1, 2, 3, 5],
                  [2, 4, 7, 9],
                  [5, 7, 8, 9] ]
"""

from typing import List


class Solution:
    def sort_matrix_row(self, mat: List[List]) -> List[List]:
        for row in mat:
            row.sort()
        return mat


def pretty_print_matrix(mat: List[List]) -> None:
    print("Matrix prettify")
    for row in mat:
        for ele in row:
            print(ele, end=" ")
        print("")

def main():
    row = int(input("Number Rows of matrix: "))
    col = int(input("Number of Columns of matrix: "))

    mat = [list(map(int, input().strip().split()))[:col] for _ in range(row)]
    solution = Solution()
    pretty_print_matrix(solution.sort_matrix_row(mat))


if __name__ == "__main__":
    main()
