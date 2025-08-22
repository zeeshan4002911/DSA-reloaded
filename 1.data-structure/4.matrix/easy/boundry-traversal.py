"""
You are given a matrix mat[][] . Return the boundary traversal on the matrix in a clockwise manner starting from the first row of the matrix.

Examples:

Input: mat[][] = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15,16]]
Output: [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5]
Explanation: The boundary traversal is: [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5]

Input:mat[][] = [[12, 11, 10, 9],[8, 7, 6, 5],[4, 3, 2, 1]]
Output: [12, 11, 10, 9, 5, 1, 2, 3, 4, 8]
Explanation: The boundary traversal is: [12, 11, 10, 9, 5, 1, 2, 3, 4, 8]

Input:mat[][] = [[12, 11],[4, 3]]
Output: [12, 11, 3, 4]
Explanation: The boundary traversal is: [12, 11, 3, 4]

Constraints:
1 ≤ mat.size()≤ 1000
1 ≤ mat[0].size() ≤ 1000
0 ≤ mat[i][j] ≤ 1000

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(n)
"""


class Solution:
    def boundary_traversal(self, mat):
        result = []
        row = len(mat)
        col = len(mat[0])

        # For traversing the first row from first column (index = 0) till the last column (index = col - 1)
        for j in range(col):
            result.append(mat[0][j])

        # For traversing the last column from second row (index = 1) till last row (index = row - 1)
        for i in range(1, row):
            result.append(mat[i][col - 1])

        if row > 1:
            # For traversing the last row from second last column (index = col - 2) till first column (index = 0)
            for j in range(col - 2, -1, -1):
                result.append(mat[row - 1][j])

        if col > 1:
            # For traversing the first column from second last row (index = row - 2) till below the first row (index = 1) for complete cycle
            for i in range(row - 2, 0, -1):
                result.append(mat[i][0])

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
