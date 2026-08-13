"""
Given a weighted graph with V vertices numbered from 0 to V-1 and E edges, represented by a 2d array edges[][], where edges[i] = [u, v, w] represents a direct edge from node u to v having w edge weight. You are also given a source vertex src.

Compute the shortest distances from the src to all other vertices. If a vertex is unreachable from the src, its distance should be marked as 108. Additionally, if the graph contains a negative weight cycle, return [-1] to indicate that shortest paths cannot be reliably computed.

Examples:

Input: V = 5, edges[][] = [[1, 3, 2], [4, 3, -1], [2, 4, 1], [1, 2, 1], [0, 1, 5]], src = 0

Output: [0, 5, 6, 6, 7]
Explanation: Shortest Paths:
For 0 to 1 minimum distance will be 5. By following path 0 -> 1
For 0 to 2 minimum distance will be 6. By following path 0 -> 1 -> 2
For 0 to 3 minimum distance will be 6. By following path 0 -> 1 -> 2 -> 4 -> 3
For 0 to 4 minimum distance will be 7. By following path 0 -> 1 -> 2 -> 4

Input: V = 4, edges[][] = [[0, 1, 4], [1, 2, -6], [2, 3, 5], [3, 1, -2]], src = 0

Output: [-1]
Explanation: The graph contains a negative weight cycle formed by the path 1 -> 2 -> 3 -> 1, where the total weight of the cycle is negative.

Constraints:
1 ≤ V ≤ 100
1 ≤ E = edges.size() ≤ V*(V-1)
-1000 ≤ w ≤ 1000
0 ≤ src < V
Expected Complexities
Time Complexity: O(V * E)
Auxiliary Space: O(V)
"""


class Solution:
    def bellmanFord(self, V: int, edges: list[list[int]], src: int) -> list[int]:
        # As per question it's mentioned to have unreachable vertex with value of 10^8
        distance = [10**8] * V
        distance[src] = 0

        # Bellman ford Algorithm: V - 1 relaxations
        for i in range(V - 1):
            for edge in edges:
                s, t, w = edge
                if distance[s] + w < distance[t] and distance[s] != 10**8:
                    distance[t] = distance[s] + w

        # Check for negative weight cycle
        for edge in edges:
            s, t, w = edge
            if distance[s] + w < distance[t] and distance[s] != 10**8:
                return [-1]

        return distance


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

    res = Solution().bellmanFord(v, edge_lst, src)
    print(res)
    return


if __name__ == "__main__":
    main()
