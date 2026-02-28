"""
Given a connected undirected graph containing V vertices represented by a 2-d adjacency list adj[][], where each adj[i] represents the list of vertices connected to vertex i. Perform a Depth First Search (DFS) traversal starting from vertex 0, visiting vertices from left to right as per the given adjacency list, and return a list containing the DFS traversal of the graph.

Note: Do traverse in the same order as they are in the given adjacency list.

Examples:

Input: adj[][] = [[2, 3, 1], [0], [0, 4], [0], [2]]

Output: [0, 2, 4, 3, 1]
Explanation: Starting from 0, the DFS traversal proceeds as follows:
Visit 0 → Output: 0
Visit 2 (the first neighbor of 0) → Output: 0, 2
Visit 4 (the first neighbor of 2) → Output: 0, 2, 4
Backtrack to 2, then backtrack to 0, and visit 3 → Output: 0, 2, 4, 3
Finally, backtrack to 0 and visit 1 → Final Output: 0, 2, 4, 3, 1

Input: adj[][] = [[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]

Output: [0, 1, 2, 3, 4]
Explanation: Starting from 0, the DFS traversal proceeds as follows:
Visit 0 → Output: 0
Visit 1 (the first neighbor of 0) → Output: 0, 1
Visit 2 (the first neighbor of 1) → Output: 0, 1, 2
Visit 3 (the first neighbor of 2) → Output: 0, 1, 2, 3
Backtrack to 2 and visit 4 → Final Output: 0, 1, 2, 3, 4

Constraints:
1 ≤ V = adj.size() ≤ 10^4
0 ≤ adj[i][j] ≤ 10^4

Expected Complexities
Time Complexity: O(V + E)
Auxiliary Space: O(V + E)
"""

from collections import deque


class Solution:
    def dfs_of_graph(self, adj):
        visited = set()
        stack = deque()
        stack.append(0)
        result = []

        while stack:
            curr = stack.pop()

            # Avoid going in loop using visited set
            if curr in visited:
                continue
            visited.add(curr)

            result.append(curr)

            # Getting the neighbours from adjacency list and then traversing each neighbour
            neighbours = adj[curr]
            size = len(neighbours)
            # Reverse traverse to maintain the order of neighbours (Due to stack last in first out property)
            for i in range(size - 1, -1, -1):
                stack.append(neighbours[i])

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
    print(soln.dfs_of_graph(adj))


if __name__ == "__main__":
    main()
