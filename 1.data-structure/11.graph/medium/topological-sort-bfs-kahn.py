"""
The idea is to use Kahn's Algorithm, which applies BFS to generate a valid topological ordering.
We first compute the in-degree of every vertex representing how many incoming edges each vertex has.
Then, all vertices with an in-degree of 0 are added to a queue, as they can appear first in the ordering.
We repeatedly remove a vertex from the queue, add it to our result list, and reduce the in-degree of all its adjacent vertices. If any of those vertices now have an in-degree of 0, they are added to the queue.
This process continues until the queue is empty, and the resulting order represents one valid topological sort of the graph.
"""

"""
Given a Directed Acyclic Graph (DAG) with V vertices numbered from 0 to V - 1 and E directed edges represented by a 2D array edges[][], where edges[i] = [u, v] denotes a directed edge from vertex u to vertex v, return a topological ordering of all the vertices.

A topological ordering is a linear ordering of the vertices such that for every directed edge u -> v, vertex u appears before vertex v in the ordering.

Examples:

Input: V = 5, E = 4, edges[][] = [[0, 1], [1, 2], [3, 2], [3, 4]]

Output: The output true denotes that the order is valid. Few valid Topological orders for the given graph are:
[0, 3, 1, 4, 2]
[3, 0, 4, 2, 1]

Input: V = 6, E = 6, edges[][] = [[0, 1], [1, 2], [2, 3], [5, 2], [5, 1], [4, 5]]

Output: The output true denotes that the order is valid. Few valid Topological orders for the graph are:
[0, 4, 5, 1, 2, 3]
[4, 5, 0, 1, 2, 3]

Constraints:
2  ≤  V  ≤  5 x 10^3
1  ≤  E = edges.size()  ≤  min[10^5, (V * (V - 1)) / 2]
0 ≤ edges[i][0], edges[i][1] < V
"""

from collections import deque


class Solution:
    def topoSort_kahn_algo(self, V, edges):
        # Kahn's Algorithm
        adj_lst = self._convert_edges_to_adj(V, edges)
        result = []
        queue = deque()
        # Calculate in-degree of each node
        # Iterate over each neighbour of node and increase the count
        in_degrees = [0] * V
        for u, neighbours in enumerate(adj_lst):
            for v in neighbours:
                in_degrees[v] += 1

        # Adding all the zero in-degree vertex to queue
        for u, in_degree in enumerate(in_degrees):
            if in_degree == 0:
                queue.append(u)

        while queue:
            curr = queue.popleft()
            # Adding zero in-degree node to our result based on their order
            result.append(curr)

            neighbours = adj_lst[curr]
            for neighbour in neighbours:
                # Reducing in-degree from all neighbours
                in_degrees[neighbour] -= 1
                # Adding zero in-degree vertex to queue
                if in_degrees[neighbour] == 0:
                    queue.append(neighbour)

        return result

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

    res = Solution().topoSort_kahn_algo(v, edge_lst)
    print(res)
    return


if __name__ == "__main__":
    main()
