"""
You are given n courses, labeled from 0 to n - 1 and a 2d array prerequisites[][] where prerequisites[i] = [x, y] indicates that we need to take course  y first if we want to take course x.

Find the ordering of courses we should take to complete all the courses.

Note: There may be multiple correct orders, you just need to return any one of them. If it is impossible to finish all tasks, return an empty array. The Driver code will print true if you return any correct order of courses else it will print false. 

Examples:

Input: n = 3, prerequisites[][] = [[1, 0], [2, 1]]
Output: true
Explanation: To take course 1, you must finish course 0. To take course 2, you must finish course 1. So the only valid order is [0, 1, 2].

Input: n = 4, prerequisites[][] = [[2, 0], [2, 1], [3, 2]]
Output: true
Explanation: Course 2 requires both 0 and 1. Course 3 requires course 2. Hence, both [0, 1, 2, 3] and [1, 0, 2, 3] are valid.

Constraints:
1 ≤ n ≤ 10^4
0 ≤ prerequisites.size() ≤ 10^5
0 ≤ prerequisites[i][0], prerequisites[i][1] < n
All prerequisite pairs are unique
prerequisites[i][0] ≠ prerequisites[i][1]

Expected Complexities
Time Complexity: O(n + m)
Auxiliary Space: O(n + m)
"""



from collections import deque


class Solution:
    def canFinish(self, n: int, pre: list[list[int]]) -> list[int]:
        adj_lst = self._convert_edges_to_adj(n, pre)
        # Topological sort order is possible if all courses are possible to comlete

        processing_queue = deque()
        topo_order = []
        in_degrees = [0] * n
        for u, neighbours in enumerate(adj_lst):
            for neighbour in neighbours:
                in_degrees[neighbour] += 1

        for u, in_degree in enumerate(in_degrees):
            if in_degree == 0:
                processing_queue.append(u)

        processing_count = 0

        # Kahn's Algorithm
        while processing_queue:
            curr = processing_queue.popleft()
            processing_count += 1
            topo_order.append(curr)

            neighbours = adj_lst[curr]
            for neighbour in neighbours:
                in_degrees[neighbour] -= 1
                if in_degrees[neighbour] == 0:
                    processing_queue.append(neighbour)

        # Possible topological order i.e., courses can be completed
        if processing_count == n:
            return topo_order
        # If vertex are getting skipped due to not having zero in degree then it's not DAG
        if processing_count < n:
            return []
        return []

    def _convert_edges_to_adj(self, v: int, edges: list[list[int]]) -> list[list[int]]:
        adj_lst = [[] for _ in range(v)]
        for edge in edges:
            course, prereq = edge[0], edge[1]
            # prereq points to the course it unlocks
            adj_lst[prereq].append(course)

        return adj_lst


def main():
    n = int(input("Enter number of course: ").strip())
    m = int(input("Enter number of prerequisit: ").strip())
    pre = [[]] * m
    for i in range(m):
        inp = input().strip().replace(",", " ").split()[:2]
        inp = list(map(int, inp))
        pre[i] = inp

    print(Solution().canFinish(n, pre))


if __name__ == "__main__":
    main()
