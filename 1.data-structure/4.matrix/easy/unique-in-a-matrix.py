"""
Given a matrix mat[][] having n rows and m columns. The task is to find unique elements in the matrix i.e., those elements which are not repeated in the matrix or those elements whose frequency is 1.

Examples:

    Input:
    mat[][] = [[2, 1, 4, 3],
              [1, 2, 3, 2],
              [3, 6, 2, 3],
              [5, 2, 5, 3]]
    Output: 4 6

    Input:
    mat[][] = [[1, 2],
              [2, 1]]
    Output: No unique element in the matrix
"""


class Solution:
    def unique_in_a_matrix(self, mat):
        hash_map = {}
        for row in mat:
            for ele in row:
                if ele not in hash_map:
                    hash_map[ele] = 1
                else:
                    hash_map[ele] += 1
        
        result = []
        for key, value in hash_map.items():
            # Only unique element having one occurence
            if value == 1:
                result.append(key)

        return result


def main():
    n = int(input("Enter the row: ").strip())
    m = int(input("Enter the column: ").strip())
    print("Enter the matrix")
    mat = [list(map(int, input().strip().split()))[:m] for _ in range(n)]

    solution = Solution()
    print(solution.unique_in_a_matrix(mat))


if __name__ == "__main__":
    main()
