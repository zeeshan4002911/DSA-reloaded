"""
Given a 2D matrix mat[][] of n rows and m columns. Return an array while traversing the matrix in ZIG-ZAG fashion.

Examples:

Input: mat[][] = [[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]]
Output: 1 2 4 7 5 3 6 8 9

Input: mat[][] = [[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]]
Output: 1 2 5 9 6 3 4 7 10 13 14 11 8 12 15 16

Constraints:
0<= mat.size(), mat[0].size() <= 1000

Expected Complexities
Time Complexity: O(n * m)
Auxiliary Space: O(1)
"""


class Solution:
    def zig_zag_traversal(self, mat):
        result = []
        row = len(mat)
        col = len(mat[0])
        if row > 0 and col > 0:
            result.append(mat[0][0])

        i, j = 0, 0
        while not (i == row - 1 and j == col - 1):
            # Right move 1 place for begining or after upward diagonal moves
            if j + 1 <= col - 1:
                j += 1
                result.append(mat[i][j])
            # Down move 1 place for last column
            elif i + 1 <= row - 1:
                i += 1
                result.append(mat[i][j])

            # Downward diagonal moves until it reach the bottom / left boundary
            while i + 1 <= row - 1 and j - 1 >= 0:
                i += 1
                j -= 1
                result.append(mat[i][j])

            # Down move 1 place after downward diagonal moves
            if i + 1 <= row - 1:
                i += 1
                result.append(mat[i][j])
            # Right move 1 for last
            elif j + 1 <= col - 1:
                j += 1
                result.append(mat[i][j])

            # Upward diagonal moves until it reach the top / right boundary
            while i - 1 >= 0 and j + 1 <= col - 1:
                i -= 1
                j += 1
                result.append(mat[i][j])

        return result


def main():
    n = int(input("Enter the row: ").strip())
    m = int(input("Enter the column: ").strip())
    print("Enter the matrix")
    mat = [list(map(int, input().strip().split()))[:m] for _ in range(n)]

    solution = Solution()
    print(solution.zig_zag_traversal(mat))


if __name__ == "__main__":
    main()
