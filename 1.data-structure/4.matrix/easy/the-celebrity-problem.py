"""
A celebrity is a person who is known to all but does not know anyone at a party. A party is being organized by some people. A square matrix mat[][] of size n*n is used to represent people at the party such that if an element of row i and column j is set to 1 it means ith person knows jth person. You need to return the index of the celebrity in the party, if the celebrity does not exist, return -1.

Note: Follow 0-based indexing.

Examples:

Input: mat[][] = [[1, 1, 0],
                [0, 1, 0],
                [0, 1, 1]]
Output: 1
Explanation: 0th and 2nd person both know 1st person and 1st person does not know anyone. Therefore, 1 is the celebrity person.

Input: mat[][] = [[1, 1],
                [1, 1]]
Output: -1
Explanation: Since both the people at the party know each other. Hence none of them is a celebrity person.

Input: mat[][] = [[1]]
Output: 0

Constraints:
1 ≤ mat.size() ≤ 1000
0 ≤ mat[i][j] ≤ 1
mat[i][i] = 1

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)
"""


class Solution:
    def celebrity_problem(self, mat):
        size = len(mat)

        # Iteration on row for diagonal as i-th person
        for i in range(size):

            # Counting number of other person who knows i-th person
            knows_count = 0
            for row in range(size):
                if row == i:
                    continue
                # Checking whether entire column (except the person) is 1 as this means the row-th person knows column(i-th) person
                if mat[row][i] == 1:
                    knows_count += 1

            # Counting number of other person who does not know i-th person
            unknowns_count = 0
            for col in range(size):
                if col == i:
                    continue
                # Checking whether entire row (except the person) is 0 as this means the row(i-th) person does not know col-th person
                if mat[i][col] == 0:
                    unknowns_count += 1

            # For i-th person to be celebrity,
            # ith person should be known by everyone else but ith person should not know any other person
            if knows_count == unknowns_count == size - 1:
                return i

        return -1


def main():
    n = int(input("Enter the size: ").strip())
    print("Enter the matrix")
    mat = [list(map(int, input().strip().split()))[:n] for _ in range(n)]

    solution = Solution()
    print(solution.celebrity_problem(mat))


if __name__ == "__main__":
    main()
