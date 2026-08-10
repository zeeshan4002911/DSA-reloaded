"""
Given an undirected, weighted graph with V vertices numbered from 0 to V-1 and E edges, represented by 2d array edges[][], where edges[i]=[u, v, w] represents the edge between the nodes u and v having w weight.
Find the shortest distance of all the vertices from the source vertex src, and return an array of integers where the ith element denotes the shortest distance between ith node and source vertex src.

Note: The Graph is connected and doesn't contain any negative weight edge.
It is guaranteed that all the shortest distance will fit in a 32-bit integer.

Examples:

Input: V = 3, edges[][] = [[0, 1, 1], [1, 2, 3], [0, 2, 6]], src = 2
Output: [4, 3, 0]
Explanation:

Shortest Paths:
For 2 to 0 minimum distance will be 4. By following path 2 -> 1 -> 0
For 2 to 1 minimum distance will be 3. By following path 2 -> 1
For 2 to 2 minimum distance will be 0. By following path 2 -> 2

Input: V = 5, edges[][] = [[0, 1, 4], [0, 2, 8], [1, 4, 6], [2, 3, 2], [3, 4, 10]], src = 0
Output: [0, 4, 8, 10, 10]
Explanation:

Shortest Paths:
For 0 to 1 minimum distance will be 4. By following path 0 -> 1
For 0 to 2 minimum distance will be 8. By following path 0 -> 2
For 0 to 3 minimum distance will be 10. By following path 0 -> 2 -> 3
For 0 to 4 minimum distance will be 10. By following path 0 -> 1 -> 4

Constraints:
1 ≤ V ≤ 10^6
1 ≤ E = edges.size() ≤ 10^6
0 ≤ edges[i][0], edges[i][1] ≤ V-1
0 ≤ edges[i][2] ≤ 10^4
0 ≤ src < V

Expected Complexities
Time Complexity: O((V + E) log V)
Auxiliary Space: O(V)
"""

import heapq


class Solution:
    def dijkstra(self, V: int, edges: list[list[int]], src: int) -> list[int]:
        adj_lst = self._convert_edges_to_adj(V, edges)
        # To store shortest distance of each vertex from source, initially set to infinity
        result = [float("inf")] * V
        # Setting source distance to zero
        result[src] = 0

        # Heap contains tuples of (distance, vertex)
        min_heap = [(0, src)]
        visited = [0] * V

        while min_heap:
            # Selecting the shortest distanced for relaxing other vertices
            distance, curr = heapq.heappop(min_heap)

            # Skip processing if we already found a shorter path to this vertex
            if visited[curr]:
                continue
            visited[curr] = 1

            neighbours = adj_lst[curr]
            for neighbour in neighbours:
                nbr_v, weight = neighbour[0], neighbour[1]
                relaxed_weight = distance + weight

                # For not visited node, relaxation of weight (Updating the short path if we found shorter one)
                if visited[nbr_v] == 0 and relaxed_weight < result[nbr_v]:
                    result[nbr_v] = relaxed_weight
                    heapq.heappush(min_heap, (relaxed_weight, nbr_v))

        return result

    def _convert_edges_to_adj(
        self, v: int, edges: list[list[int]]
    ) -> list[list[tuple[int, int]]]:
        adj_lst = [[] for _ in range(v)]
        for edge in edges:
            u, v, w = edge[0], edge[1], edge[2]
            adj_lst[u].append((v, w))
            adj_lst[v].append((u, w))

        return adj_lst


def main():
    edge_lst = []
    v = int(input("Enter number of vertics: ").strip())
    e = int(input("Enter number of edges: ").strip())

    i = e
    while i > 0:
        inp = input().strip().replace(",", "").split()[:3]
        inp = list(map(int, inp))
        edge_lst.append(inp)
        i -= 1

    src = int(input("Enter source vertex: ").strip())

    res = Solution().dijkstra(v, edge_lst, src)
    print(res)
    return


if __name__ == "__main__":
    main()
