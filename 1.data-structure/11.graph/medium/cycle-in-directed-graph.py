"""
Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges, check whether it contains any cycle or not.
The graph is represented as a 2D vector edges[][], where each entry edges[i] = [u, v] denotes an edge from vertex u to v.

Examples:

Input: V = 4, edges[][] = [[0, 1], [1, 2], [2, 0], [2, 3]]



Output: true
Explanation: The diagram clearly shows a cycle 0 → 1 → 2 → 0

Input: V = 4, edges[][] = [[0, 1], [0, 2], [1, 2], [2, 3]]


Output: false
Explanation: no cycle in the graph

Constraints:
1 ≤ V ≤ 10^5
0 ≤ E ≤ 10^5
0 ≤ edges[i][0], edges[i][1] < V

Expected Complexities
Time Complexity: O(V + E)
Auxiliary Space: O(V + E)
"""

from collections import deque


class Solution:
    def directed_graph_cycle(self, v, edge_lst):
        adj_lst = self.convert_edge_to_adj_list(v, edge_lst)

        visited = set()
        recStack = set()
        stack = deque()

        # For processing each vertex
        for i in range(v):
            if i not in visited:
                stack.append((i, False))

                # DFS For each vertex
                while stack:
                    curr, is_processed = stack.pop()

                    if is_processed:
                        # Once the dfs for current path is done removing from recStack
                        recStack.remove(curr)
                        continue

                    if curr in recStack:
                        # Found: In case if for a current dfs same node gets reached
                        return True

                    if curr in visited:
                        continue

                    visited.add(curr)
                    recStack.add(curr)

                    # Adding processed marker to mark the end of dfs for curr node
                    stack.append((curr, True))

                    neighbours = adj_lst[curr]
                    size = len(neighbours)
                    for i in range(size - 1, -1, -1):
                        stack.append((neighbours[i], False))

        return False

    def convert_edge_to_adj_list(self, v, edge_lst):
        adj_lst = [[] for _ in range(v)]
        for edge in edge_lst:
            u = edge[0]
            v = edge[1]
            adj_lst[u].append(v)
        return adj_lst


def main():
    vertices = int(input("Enter number of vertex: ").strip())
    edges = int(input("Enter number of edges: ").strip())
    edge_lst = []

    while edges > 0:
        inp = input().strip().replace(",", " ").split()
        inp = list(map(int, inp))
        edge_lst.append(inp)

        edges -= 1

    soln = Solution()
    res = soln.directed_graph_cycle(vertices, edge_lst)
    print(res)


if __name__ == "__main__":
    main()
