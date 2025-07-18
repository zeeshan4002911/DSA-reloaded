"""
Given k sorted arrays arranged in the form of a matrix of size k * k. The task is to merge them into one sorted array. Return the merged sorted array ( as a pointer to the merged sorted arrays in cpp, as an ArrayList in java, and list in python).


Examples :

Input: k = 3, arr[][] = {{1,2,3},{4,5,6},{7,8,9}}
Output: 1 2 3 4 5 6 7 8 9
Explanation: Above test case has 3 sorted arrays of size 3, 3, 3 arr[][] = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]. The merged list will be [1, 2, 3, 4, 5, 6, 7, 8, 9].

Input: k = 4, arr[][]={{1,2,3,4},{2,2,3,4},{5,5,6,6},{7,8,9,9}}
Output: 1 2 2 2 3 3 4 4 5 5 6 6 7 8 9 9
Explanation: Above test case has 4 sorted arrays of size 4, 4, 4, 4 arr[][] = [[1, 2, 2, 2], [3, 3, 4, 4], [5, 5, 6, 6], [7, 8, 9, 9 ]]. The merged list will be [1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 8, 9, 9].

Expected Time Complexity: O(k^2*Log(k))
Expected Auxiliary Space: O(k^2)

Constraints:
1 <= k <= 100
"""

import heapq


class Solution:
    # TC: O(k^2*Log(k ^ 2)), SC: O(k^2)
    def merge_k_sorted_arrays(self, mat, k):
        rows = cols = k
        flatten_mat = []
        for i in range(rows):
            for j in range(cols):
                flatten_mat.append(mat[i][j])
        flatten_mat.sort()
        return flatten_mat

    # TC: O(k^2*Log(k)), SC: O(k)
    def merge_k_sorted_arrays_using_min_heap(self, mat, k):
        result = []
        min_heap = []
        heapq.heapify(min_heap)

        # Insert of all array's first element into heap
        for i in range(k):
            heapq.heappush(min_heap, (mat[i][0], i, 0))

        while min_heap:
            # Pop of root element (min element from all the arrays)
            val, row, col = heapq.heappop(min_heap)
            result.append(val)
            # Push the next element (Next in row of popped element) if exists
            if col + 1 < k:
                heapq.heappush(min_heap, (mat[row][col + 1], row, col + 1))

        return result


def main():
    k = int(input())
    mat = [list(map(int, input().strip().split()))[:k] for _ in range(k)]

    solution = Solution()
    print(solution.merge_k_sorted_arrays(mat, k))


if __name__ == "__main__":
    main()
