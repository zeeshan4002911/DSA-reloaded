"""
You are given a rectangular matrix mat[][] of size n x m, and your task is to return an array while traversing the matrix in spiral form.

Examples:

Input: mat[][] = [[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]]
Output: [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
Explanation:

Input: mat[][] = [[2, 7, 10],
                [5, 1, 3],
                [4, 2, 8]]
Output: [2, 7, 10, 3, 8, 2, 4, 5, 1]
Explanation: Applying same technique as shown above.

Input: mat[][] = [[32, 44, 27, 23],
                [54, 28, 50, 62]]
Output: [32, 44, 27, 23, 62, 50, 28, 54]
Explanation: Applying same technique as shown above, output will be [32, 44, 27, 23, 62, 50, 28, 54].

Constraints:
1 ≤ n, m ≤1000
0 ≤ mat[i][j] ≤100

Expected Complexities
Time Complexity: O(n * m)
Auxiliary Space: O(1)
"""


class Solution:
    def boundary_traversal(self, mat):
        result = []
        row = len(mat)
        col = len(mat[0])
        size = row * col

        i, j = 0, -1
        orientation = "right"
        # Decay factor for length of row/column decrease on each complete loop
        d_fac = 0

        for _ in range(size):
            if orientation == "right":
                j += 1
                if j == col - 1 - d_fac:
                    orientation = "down"
            elif orientation == "down":
                i += 1
                if i == row - 1 - d_fac:
                    orientation = "left"
            elif orientation == "left":
                j -= 1
                if j == 0 + d_fac:
                    orientation = "up"
                    # Increment of decay factor
                    d_fac += 1
            elif orientation == "up":
                i -= 1
                if i == 0 + d_fac:
                    orientation = "right"

            result.append(mat[i][j])

        return result


def main():
    n = int(input("Enter the row: ").strip())
    m = int(input("Enter the column: ").strip())
    print("Enter the matrix")
    mat = [list(map(int, input().strip().split()))[:m] for _ in range(n)]

    solution = Solution()
    print(solution.boundary_traversal(mat))


if __name__ == "__main__":
    main()
