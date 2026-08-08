"""
Given n courses numbered from 0 to n - 1 and a 2D array pre[][], where pre[i] = [u, v] indicates that course v must be completed before course u. Check whether it is possible to complete all the courses. Return true if possible; otherwise, return false.

Examples:

Input n = 4, pre[] = [[2, 0], [2, 1], [3, 2]]
Output: true
Explanation:
To take course 2, you must first finish courses 0 and 1.
To take course 3, you must first finish course 2.
All courses can be completed, for example in the order [0, 1, 2, 3] or [1, 0, 2, 3].

Input: n = 3, pre[] = [[0, 1], [1, 2], [2, 0]]
Output: false
Explanation:
To take course 0, you must first finish course 1.
To take course 1, you must first finish course 2.
To take course 2, you must first finish course 0.
Since each course depends on the other, it is impossible to complete all courses.

Constraints:
1 ≤ n ≤ 10^4
1 ≤ n (rows) ≤ 10^5
2 ≤ m (cols) ≤ 2
0 ≤ pre[i][j] < n
All pre pairs are unique
pre[i][0] ≠ pre[i][1]

Expected Complexities
Time Complexity: O(n + m)
Auxiliary Space: O(n + m)
"""

from collections import deque


class Solution:
    def canFinish(self, n: int, pre: list[list[int]]) -> bool:
        adj_lst = self._convert_edges_to_adj(n, pre)
        # Topological sort order is possible if all courses are possible to comlete

        processing_queue = deque()
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

            neighbours = adj_lst[curr]
            for neighbour in neighbours:
                in_degrees[neighbour] -= 1
                if in_degrees[neighbour] == 0:
                    processing_queue.append(neighbour)

        # Possible topological order i.e., courses can be completed
        if processing_count == n:
            return True
        # If vertex are getting skipped due to not having zero in degree then it's not DAG
        if processing_count < n:
            return False
        return False

    def _convert_edges_to_adj(self, v: int, edges: list[list[int]]) -> list[list[int]]:
        adj_lst = [[] for _ in range(v)]
        for edge in edges:
            u, v = edge[0], edge[1]
            adj_lst[u].append(v)

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
