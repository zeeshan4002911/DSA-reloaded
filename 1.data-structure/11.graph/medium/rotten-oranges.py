"""
Given a matrix mat[][], where each cell in the matrix can have values 0, 1 or 2 which has the following meaning:
0 : Empty cell
1 : Cell have fresh oranges
2 : Cell have rotten oranges

Your task is to determine the minimum time required so that all the oranges become rotten. A rotten orange at index (i, j) can rot other fresh orange at indexes (i-1, j), (i+1, j), (i, j-1), (i, j+1) (up, down, left and right) in a unit time.

Note: If it is impossible to rot every orange then simply return -1.

Examples:

Input: mat[][] = [[2, 1, 0, 2, 1], [1, 0, 1, 2, 1], [1, 0, 0, 2, 1]]
Output: 2
Explanation: Oranges at positions (0,0), (0,3), (1,3), and (2,3) will rot adjacent fresh oranges in successive time frames.
All fresh oranges become rotten after 2 units of time.

Input: mat[][] = [[2, 1, 0, 2, 1], [0, 0, 1, 2, 1], [1, 0, 0, 2, 1]]
Output: -1
Explanation: Oranges at positions (0,0), (0,3), (1,3), and (2,3) rot some fresh oranges,
but the fresh orange at (2,0) can never be reached, so not all oranges can rot.

Constraints:
1 ≤ mat.size() ≤ 500
1 ≤ mat[0].size() ≤ 500
mat[i][j] = {0, 1, 2}

Expected Complexities
Time Complexity: O(n * m)
Auxiliary Space: O(n * m)
"""

from collections import deque


class Solution:
    def rotten_oranges(self, mat):
        visited = set()
        queue = deque()

        r = len(mat)
        c = len(mat[0])

        for i in range(r):
            for j in range(c):
                pos = f"{i},{j}"
                if pos not in visited and mat[i][j] == 2:
                    visited.add(pos)
                    # Adding all rotten oranges to the queue for processing
                    queue.append((i, j))

        elapsed_time = 0
        while queue:
            size = len(queue)
            rot_change = False

            # Processing all the rotten oranges at once level as time (elapsed time)
            """
            If we do graph component by component traversal then in case of two rotten orange at two differnet corner change the fresh orange incorrectly as the maximum distance from the furthest one will get considered
            """
            for _ in range(size):
                i, j = queue.popleft()

                # Getting the neighbours from matrix and then traversing each neighbour
                neighbours = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
                for neighbour in neighbours:
                    i1, j1 = neighbour
                    if i1 < 0 or i1 >= r or j1 < 0 or j1 >= c:
                        continue
                    if mat[i1][j1] == 0:
                        continue

                    pos = f"{i1},{j1}"
                    if pos not in visited:
                        visited.add(pos)

                        # For fresh orange traversing and converting to rotten
                        if mat[i1][j1] == 1:
                            mat[i1][j1] = 2
                            queue.append((i1, j1))
                            rot_change = True

            if rot_change:
                elapsed_time += 1

        # Checking the presence of any fresh orange post the maximum elapsed time
        for i in range(r):
            for j in range(c):
                if mat[i][j] == 1:
                    return -1

        return elapsed_time


def main():
    mat = []
    r = int(input("Enter number of rows: ").strip())
    c = int(input("Enter number of columns: ").strip())

    i = 0
    while i < r:
        inp = input().strip().replace(",", " ").split()[:c]
        inp = list(map(int, inp))
        mat.append(inp)
        i += 1

    soln = Solution()
    print(soln.rotten_oranges(mat))


if __name__ == "__main__":
    main()
