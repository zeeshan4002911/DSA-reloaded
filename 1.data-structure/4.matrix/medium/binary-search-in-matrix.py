"""
Given a strictly sorted 2D matrix mat[][] of size n x m and a number x. Find whether the number x is present in the matrix or not.
Note: In a strictly sorted matrix, each row is sorted in strictly increasing order, and the first element of the ith row (i!=0) is greater than the last element of the (i-1)th row.

Examples:

Input: mat[][] = [[1, 5, 9], [14, 20, 21], [30, 34, 43]], x = 14
Output: true
Explanation: 14 is present in the matrix, so output is true.

Input: mat[][] = [[1, 5, 9, 11], [14, 20, 21, 26], [30, 34, 43, 50]], x = 42
Output: false
Explanation: 42 is not present in the matrix.

Input: mat[][] = [[87, 96, 99], [101, 103, 111]], x = 101
Output: true
Explanation: 101 is present in the matrix.

Constraints:
1 ≤ n, m ≤ 1000
1 ≤ mat[i][j] ≤ 10^9
1 ≤ x ≤ 10^9

Expected Complexities
Time Complexity: O(log(n * m))
Auxiliary Space: O(1)
"""


class Solution:
    def binary_search_in_matrix(self, mat, target):
        low = 0
        n = len(mat)
        m = len(mat[0])
        high = n * m - 1

        while low < high:
            mid = low + (high - low) // 2
            # Index mapping [row = index / total_col, col = index % total_col]
            row = mid // m
            col = mid % m
            
            if target == mat[row][col]:
                return True
            elif target < mat[row][col]:
                high = mid - 1
            else:
                low = mid + 1
        return False


def main():
    n = int(input("Enter row of matrix: ").strip())
    m = int(input("Enter column of matrix: ").strip())
    mat = [list(map(int, input().strip().split()))[:m] for _ in range(n)]
    x = int(input("Enter the target for search: ").strip())
    solution = Solution()
    print(solution.binary_search_in_matrix(mat, x))


if __name__ == "__main__":
    main()
