"""
Given an undirected graph with V vertices and E edges, represented as a 2D vector edges[][], where each entry edges[i] = [u, v] denotes an edge between vertices u and v, determine whether the graph contains a cycle or not.

Note: The graph can have multiple component.

Examples:

Input: V = 4, E = 4, edges[][] = [[0, 1], [0, 2], [1, 2], [2, 3]]
Output: true
Explanation:

1 -> 2 -> 0 -> 1 is a cycle.

Input: V = 4, E = 3, edges[][] = [[0, 1], [1, 2], [2, 3]]
Output: false
Explanation:

No cycle in the graph.

Constraints:
1 ≤ V, E ≤ 10^5
0 ≤ edges[i][0], edges[i][1] < V

Expected Complexities
Time Complexity: O(V + E)
Auxiliary Space: O(V)
"""

from collections import deque


class Solution:
    def undirected_graph_cycle(self, v, edge_lst):
        adj_lst = self.convert_edge_to_adj_list(v, edge_lst)

        visited = set()
        stack = deque()

        # For processing each vertex in case of multi component graph
        for i in range(v):
            if i not in visited:
                stack.append((i, float("inf")))

                # DFS For each vertex
                while stack:
                    curr, parent = stack.pop()

                    if curr in visited:
                        continue

                    visited.add(curr)

                    neighbours = adj_lst[curr]
                    size = len(neighbours)
                    for i in range(size - 1, -1, -1):
                        if neighbours[i] not in visited:
                            stack.append((neighbours[i], curr))

                        # Cycle Case: In case if it's visited and not parent of current vertex
                        elif neighbours[i] != parent:
                            return True

        return False

    def convert_edge_to_adj_list(self, v, edge_lst):
        adj_lst = [[] for _ in range(v)]
        for edge in edge_lst:
            u = edge[0]
            v = edge[1]
            adj_lst[u].append(v)

            # For undirected graph
            adj_lst[v].append(u)
        return adj_lst

    def undirected_graph_cycle_rec(self, v, edge_lst):
        adj_lst = self.convert_edge_to_adj_list(v, edge_lst)
        visited = [0] * v

        for i in range(v):
            if not visited[i]:
                res = self.undirected_graph_cycle_rec_helper(
                    i, visited, adj_lst, float("inf")
                )
                if res is True:
                    return True

        return False

    def undirected_graph_cycle_rec_helper(self, curr, visited, adj_lst, parent):
        # In case if current node is already visited
        if visited[curr]:
            return False

        visited[curr] = True

        neighbours = adj_lst[curr]
        for neighbour in neighbours:
            if not visited[neighbour]:
                res = self.undirected_graph_cycle_rec_helper(
                    neighbour, visited, adj_lst, curr
                )
                if res is True:
                    return True

            # Cycle Case: In case if it's visited and not parent of current vertex
            elif neighbour != parent:
                return True

        return False


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
    res = soln.undirected_graph_cycle(vertices, edge_lst)
    print(res)


if __name__ == "__main__":
    main()
