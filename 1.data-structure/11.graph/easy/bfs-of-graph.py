"""
Given a connected undirected graph containing V vertices, represented by a 2-d adjacency list adj[][], where each adj[i] represents the list of vertices connected to vertex i. Perform a Breadth First Search (BFS) traversal starting from vertex 0, visiting vertices from left to right according to the given adjacency list, and return a list containing the BFS traversal of the graph.

Note: Do traverse in the same order as they are in the given adjacency list.

Examples:

Input: adj[][] = [[2, 3, 1], [0], [0, 4], [0], [2]]

Output: [0, 2, 3, 1, 4]
Explanation: Starting from 0, the BFS traversal will follow these steps:
Visit 0 → Output: 0
Visit 2 (first neighbor of 0) → Output: 0, 2
Visit 3 (next neighbor of 0) → Output: 0, 2, 3
Visit 1 (next neighbor of 0) → Output: 0, 2, 3, 1
Visit 4 (neighbor of 2) → Final Output: 0, 2, 3, 1, 4

Input: adj[][] = [[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]

Output: [0, 1, 2, 3, 4]
Explanation: Starting from 0, the BFS traversal proceeds as follows:
Visit 0 → Output: 0
Visit 1 (the first neighbor of 0) → Output: 0, 1
Visit 2 (the next neighbor of 0) → Output: 0, 1, 2
Visit 3 (the first neighbor of 2 that hasn't been visited yet) → Output: 0, 1, 2, 3
Visit 4 (the next neighbor of 2) → Final Output: 0, 1, 2, 3, 4

Constraints:
1 ≤ V = adj.size() ≤ 10^4
0 ≤ adj[i][j] ≤ 10^4

Expected Complexities
Time Complexity: O(V + E)
Auxiliary Space: O(V + E)
"""

from collections import deque


class Solution:
    def bfs_of_graph(self, adj):
        visited = set()
        queue = deque()
        queue.append(0)
        result = []

        while queue:
            curr = queue.popleft()

            # Avoid going in loop using visited set
            if curr in visited:
                continue
            visited.add(curr)

            result.append(curr)

            # Getting the neighbours from adjacency list and then traversing each neighbour
            neighbours = adj[curr]
            for neighbour in neighbours:
                queue.append(neighbour)

        return result


def main():
    adj = []
    v = int(input("Enter number of vertices: ").strip())

    while v > 0:
        inp = input().strip().replace(",", " ").split()
        inp = list(map(int, inp))
        adj.append(inp)
        v -= 1

    soln = Solution()
    print(soln.bfs_of_graph(adj))


if __name__ == "__main__":
    main()
