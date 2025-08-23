"""
Given a positive integer n, return the nth row of pascal's triangle.
Pascal's triangle is a triangular array of the binomial coefficients formed by summing up the elements of previous row.

File:PascalTriangleAnimated2.gif

Examples:

Input: n = 4
Output: [1, 3, 3, 1]
Explanation: 4th row of pascal's triangle is [1, 3, 3, 1].

Input: n = 5
Output: [1, 4, 6, 4, 1]
Explanation: 5th row of pascal's triangle is [1, 4, 6, 4, 1].

Input: n = 1
Output: [1]
Explanation: 1st row of pascal's triangle is [1].

Constraints:
1 ≤ n ≤ 30

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(n)
"""


class Solution:
    def pascals_triangle(self, n):
        mat = []

        # Dynamic programming - uses previous row calculated value to generate next row
        for i in range(n):
            row = []
            for j in range(i + 1):
                # Inserting 1 for first or last element
                if j == i or j == 0:
                    row.append(1)
                # Inserting the sum of previous row current column and prev column
                else:
                    row.append(mat[i - 1][j] + mat[i - 1][j - 1])
            mat.append(row)

        return mat[n - 1]


def main():
    n = int(input("Enter the row of pascal triangle: "))
    solution = Solution()
    print(solution.pascals_triangle(n))


if __name__ == "__main__":
    main()
