"""
Given a matrix of distinct values and a sum. The task is to find all the pairs in a given matrix whose summation is equal to the given sum. Each element of a pair must be from different rows i.e; the pair must not lie in the same row.

Examples:

    Input : mat[][] = {{1, 3, 2, 4},
                      {5, 8, 7, 6},
                      {9, 10, 13, 11},
                      {12, 0, 14, 15}}
            sum = 11
    Output: (1, 10), (3, 8), (2, 9), (4, 7), (11, 0)

    Input : mat[][] = {{1, 5, 7},
                      {2, 6, 8},
                      {3, 4, 9}}
            sum = 11
    Output : (2, 9), (3, 8), (5, 6), (7, 4)
"""


class Solution:
    def pair_with_given_sum_from_different_row(self, mat, n, sum):
        row_hash_map = {}
        result = []
        for i in range(n):
            for j in range(n):
                complement_value = sum - mat[i][j]
                if complement_value in row_hash_map:
                    complement_value_row = row_hash_map[complement_value]
                    # Condition to avoid pair duplication
                    if complement_value_row < i:
                        pair = (mat[i][j], complement_value)
                        result.append(pair)
                # Adding matrix value as key and value as row number in dictionary
                row_hash_map[mat[i][j]] = i
        return result


def pretty_print_matrix(mat: list[list[int]]) -> None:
    print("Matrix prettify")
    for row in mat:
        for ele in row:
            print(ele, end=" ")
        print("")


def main():
    n = int(input("Enter number of rows and columns of matrix: "))
    mat = [list(map(int, input().strip().split()))[:n] for _ in range(n)]
    sum = int(input("Enter the target sum: "))
    solution = Solution()
    print(solution.pair_with_given_sum_from_different_row(mat, n, sum))


if __name__ == "__main__":
    main()
