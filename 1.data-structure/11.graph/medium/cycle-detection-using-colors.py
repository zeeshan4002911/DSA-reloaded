"""
Given a directed graph represented by the number of vertices V and a list of directed edges, determine whether the graph contains a cycle.

Your task is to implement a function that accepts V (number of vertices) and edges (an array of directed edges where each edge is a pair [u, v]), and returns true if the graph contains at least one cycle, otherwise returns false.

Example:

    Input:  V = 4, edges[][] = [[0, 1], [0, 2], [1, 2], [2, 0], [2, 3], [3, 3]]
    Output: true
    Explanation: This diagram clearly shows a cycle 0 → 2 → 0

    Input: V = 4, edges[][] = [[0, 1], [0, 2], [1, 2], [2, 0], [2, 3], [3, 3]]
    Output: false
    Explanation: The diagram clearly shows no cycle.
"""

from collections import deque


class Solution:
    def directed_graph_cycle(self, v, edge_lst):
        adj_lst = self.convert_edge_to_adj_list(v, edge_lst)

        """
        0: white/unvisited
        1: gray/currently in recursive stack
        2: black/visted (processing finished)
        """
        colors_lst = [0] * v
        stack = deque()

        # For processing each vertex
        for i in range(v):
            if colors_lst[i] == 0:
                stack.append((i, False))

                # DFS For each vertex
                while stack:
                    curr, is_processed = stack.pop()

                    if is_processed:
                        # Once the dfs for current path is done removing from recStack
                        colors_lst[curr] = 2
                        continue

                    if colors_lst[curr] == 1:
                        # Found: In case if for a current dfs same node gets reached
                        return True

                    if colors_lst[curr] == 2:
                        continue

                    # Marking for processing start
                    colors_lst[curr] = 1

                    # Adding processed marker to mark the end of dfs for curr node
                    stack.append((curr, True))

                    neighbours = adj_lst[curr]
                    size = len(neighbours)
                    for i in range(size - 1, -1, -1):
                        if colors_lst[neighbours[i]] != 2:
                            stack.append((neighbours[i], False))

        return False

    def undirected_graph_cycle(self, v, edge_lst):
        adj_lst = self.convert_edge_to_adj_list(v, edge_lst, True)

        """
        0: white/unvisited
        1: gray/currently in recursive stack
        2: black/visted (processing finished)
        """
        colors_lst = [0] * v
        stack = deque()

        # For processing each vertex
        for i in range(v):
            if colors_lst[i] == 0:
                stack.append((i, False, float("inf")))

                # DFS For each vertex
                while stack:
                    curr, is_processed, parent = stack.pop()

                    if is_processed:
                        # Once the dfs for current path is done removing from recStack
                        colors_lst[curr] = 2
                        continue

                    if colors_lst[curr] == 1:
                        # Found: In case if for a current dfs same node gets reached
                        return True

                    if colors_lst[curr] == 2:
                        continue

                    # Marking for processing start
                    colors_lst[curr] = 1

                    # Adding processed marker to mark the end of dfs for curr node
                    stack.append((curr, True, parent))

                    neighbours = adj_lst[curr]
                    size = len(neighbours)
                    for i in range(size - 1, -1, -1):
                        # Condition to skip the processing for undirected graph (current to parent link)
                        if neighbours[i] == parent:
                            continue

                        if colors_lst[neighbours[i]] != 2:
                            stack.append((neighbours[i], False, curr))

        return False

    def convert_edge_to_adj_list(self, v, edge_lst, undirected=False):
        adj_lst = [[] for _ in range(v)]
        for edge in edge_lst:
            u = edge[0]
            v = edge[1]
            adj_lst[u].append(v)

            # For undirected graph adjacency list
            if undirected:
                adj_lst[v].append(u)
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
