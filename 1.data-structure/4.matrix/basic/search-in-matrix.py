"""
Given a matrix mat[n][m] and an element target. return true if the target is present in the matrix, else return false.

Examples:

    Input : mat[][] = { {10, 51, 9},
                      {14, 20, 21},
                      {30, 24, 43} }
    target = 14
    Output: Found

    Input : mat[][] = {{31, 5, 9, 11},
                      {14, 7, 21, 26},
                      {30, 4, 43, 50} }
    target = 42
    Output: Not Found
"""


class Solution:
    def search_in_matrix(self, mat, n, target):
        # Linear search for matrix
        for row in mat:
            for ele in row:
                if ele == target:
                    return True
        return False


def main():
    n = int(input("Enter the size of matrix: ").strip())
    mat = [list(map(int, input().strip().split()))[:n] for _ in range(n)]
    target = int(input("Enter the target: ").strip())
    solution = Solution()
    print(solution.search_in_matrix(mat, n, target))


if __name__ == "__main__":
    main()
