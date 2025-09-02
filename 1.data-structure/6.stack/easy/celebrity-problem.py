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

from collections import deque


class Solution:
    def celebrity_problem(self, mat):
        st = deque()
        size = len(mat)

        # Adding all the person into the stack
        for i in range(size):
            st.append(i)

        # Comparing two person and removing non-celebrity person from stack
        while len(st) > 1:
            i = st.pop()
            j = st.pop()

            # i-th person knows j-th, that means i can not be celebrity
            if mat[i][j] == 1:
                # Adding possible celebrity back to stack
                st.append(j)
            else:
                st.append(i)

        c = st.pop()
        for i in range(size):
            if i == c:
                continue
            # Everybody should know celebrity and celebrity should not know anyone
            if mat[i][c] == 0 or mat[c][i] == 1:
                return -1
        
        return c


def main():
    n = int(input("Enter size of matrix: ").strip())
    mat = [list(map(int, input().strip().split()))[:n] for _ in range(n)]

    solution = Solution()
    print(solution.celebrity_problem(mat))


if __name__ == "__main__":
    main()
