"""
Given a Directed Acyclic Graph (DAG) with V vertices numbered from 0 to V - 1 and E directed edges represented by a 2D array edges[][], where edges[i] = [u, v] denotes a directed edge from vertex u to vertex v, return a topological ordering of all the vertices.

A topological ordering is a linear ordering of the vertices such that for every directed edge u -> v, vertex u appears before vertex v in the ordering.

Note: As there are multiple Topological orders possible, you may return any of them. If your returned Topological sort is correct then the output will be true else false.

Examples:

Input: V = 4, E = 3, edges[][] = [[3, 0], [1, 0], [2, 0]]

Output: true
Explanation: The output true denotes that the order is valid. Few valid Topological orders for the given graph are:
[3, 2, 1, 0]
[1, 2, 3, 0]
[2, 3, 1, 0]

Input: V = 6, E = 6, edges[][] = [[1, 3], [2, 3], [4, 1], [4, 0], [5, 0], [5, 2]]

Output: true
Explanation: The output true denotes that the order is valid. Few valid Topological orders for the graph are:
[4, 5, 0, 1, 2, 3]
[5, 2, 4, 0, 1, 3]

Constraints:
2  ≤  V  ≤  5 x 10^3
1  ≤  E = edges.size()  ≤  min[10^5, (V * (V - 1)) / 2]
0 ≤ edges[i][0], edges[i][1] < V
"""

from collections import deque


class Solution:
    def topoSort(self, V: int, edges: list[list[int]]) -> list[int]:
        visit_state = [0 for _ in range(V)]
        adj_lst = self._convert_edges_to_adj(V, edges)
        n = len(adj_lst)
        # Stack used for marking all neighbour visits
        result_st = deque()

        # For traversing each node of graph
        for i in range(n):
            if visit_state[i] == 0:
                self.topoSort_dfs(i, adj_lst, visit_state, result_st)

        # Topological order is reverse of stack
        result = []
        while result_st:
            result.append(result_st.pop())
        return result

    def topoSort_dfs(
        self,
        v: int,
        adj_lst: list[list[int]],
        visit_state: list[bool],
        result_st: deque[int],
    ) -> list[int]:
        st = deque()
        st.append((v, False))

        while st:
            curr, is_backtracking = st.pop()

            if is_backtracking:
                # Add to stack after visiting all it's neighbours
                visit_state[curr] = 2
                result_st.append(curr)
                continue

            if visit_state[curr] == 1:
                raise ValueError("Graph contains a cycle! Topological not possible.")
            if visit_state[curr] == 2:
                continue

            # Marking the visit of node
            visit_state[curr] = 1
            # Adding to stack with backtracking flag for getting it processed after neighbours
            st.append((curr, True))

            neighbours = adj_lst[curr]
            size = len(neighbours)
            for i in range(size - 1, -1, -1):
                st.append((neighbours[i], False))

        return

    def _convert_edges_to_adj(self, v: int, edges: list[list[int]]) -> list[list[int]]:
        adj_lst = [[] for _ in range(v)]
        for edge in edges:
            u, v = edge[0], edge[1]
            adj_lst[u].append(v)

        return adj_lst


def main():
    edge_lst = []
    v = int(input("Enter number of vertics: ").strip())
    e = int(input("Enter number of edges: ").strip())

    i = e
    while i > 0:
        inp = input().strip().replace(",", "").split()
        inp = list(map(int, inp))
        edge_lst.append(inp)
        i -= 1

    res = Solution().topoSort(v, edge_lst)
    print(res)
    return


if __name__ == "__main__":
    main()
