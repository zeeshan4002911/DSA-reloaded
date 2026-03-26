"""
Given a grid of size n*m (n is the number of rows and m is the number of columns in the grid) consisting of 'W's (Water) and 'L's (Land). Find the number of islands.

Note: An island is either surrounded by water or the boundary of a grid and is formed by connecting adjacent lands horizontally or vertically or diagonally i.e., in all 8 directions.

Examples:

Input: grid[][] = [['L', 'L', 'W', 'W', 'W'],
                ['W', 'L', 'W', 'W', 'L'],
                ['L', 'W', 'W', 'L', 'L'],
                ['W', 'W', 'W', 'W', 'W'],
                ['L', 'W', 'L', 'L', 'W']]
Output: 4
Explanation:
The image below shows all the 4 islands in the grid.


Input: grid[][] = [['W', 'L', 'L', 'L', 'W', 'W', 'W'],
                ['W', 'W', 'L', 'L', 'W', 'L', 'W']]
Output: 2
Expanation:
The image below shows 2 islands in the grid.


Constraints:
1 ≤ n, m ≤ 500
grid[i][j] = {'L', 'W'}
Expected Complexities
Time Complexity: O(n * m)
Auxiliary Space: O(n * m)
"""

from collections import deque


class Solution:
    def island_in_graph(self, mat):
        visited = set()
        result = 0
        r = len(mat)
        c = len(mat[0])

        for i in range(r):
            for j in range(c):
                pos = f"{i},{j}"
                # For each land initiating bfs to find island (connected vertex)
                if pos not in visited and mat[i][j] != "W":
                    result += 1
                    visited.add(pos)
                    self.bfs_of_graph(r, c, mat, visited, i, j)
        
        return result

    def bfs_of_graph(self, r, c, mat, visited, r1, c1):
        queue = deque()
        queue.append((r1, c1))

        while queue:
            i, j = queue.popleft()

            # Covers vertical, horizontal and diagonal vertex
            neighbours = [
                (i - 1, j),  # vertically up vertex
                (i + 1, j),  # vertically down vertex
                (i, j - 1),  # horizontally left vertex
                (i, j + 1),  # horizontally right vertex
                (i - 1, j - 1),  # top left vertex
                (i + 1, j - 1),  # bottom left vertex
                (i - 1, j + 1),  # top right vertex
                (i + 1, j + 1),  # bottom right vertex
            ]

            for neighbour in neighbours:
                i1, j1 = neighbour
                if i1 < 0 or i1 >= r or j1 < 0 or j1 >= c:
                    continue
                # Ignoring water body
                if mat[i1][j1] == "W":
                    continue

                # Avoid going in loop using visited set
                pos = f"{i1},{j1}"
                if pos not in visited:
                    visited.add(pos)

                    queue.append(neighbour)

        return


def main():
    adj_mat = []
    n = int(input("Enter number of rows: ").strip())
    m = int(input("Enter number of column: ").strip())

    while n > 0:
        inp = input().strip().replace(",", " ").split()[:m]
        inp = list(map(str.upper, inp))
        adj_mat.append(inp)
        n -= 1

    soln = Solution()
    print(soln.island_in_graph(adj_mat))


if __name__ == "__main__":
    main()
