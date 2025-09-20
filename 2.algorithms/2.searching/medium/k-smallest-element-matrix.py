"""
Given a matrix mat[][] of size n*n, where each row and column is sorted in non-decreasing order. Find the kth smallest element in the matrix.
Examples:

Input: n = 4, mat[][] = [[16, 28, 60, 64], [22, 41, 63, 91], [27, 50, 87, 93], [36, 78, 87, 94]], k = 3
Output: 27
Explanation: 27 is the 3rd smallest element.

Input: n = 4, mat[][] = [[10, 20, 30, 40], [15, 25, 35, 45], [24, 29, 37, 48], [32, 33, 39, 50]], k = 7
Output: 30
Explanation: 30 is the 7th smallest element.

Constraints:
1 <= n <= 500
1 <= mat[i][j] <= 10000
1 <= k <= n*n

Time Complexity: O(n * log (mat[i][j] ))
Auxiliary Space: O(1)
"""

import heapq


class Solution:
    def k_smallest_element(self, n, mat, k):
        max_heap = []
        heapq.heapify(max_heap)
        
        for i in range(n):
            for j in range(n):
                current_element = mat[i][j]
                # For max heap as heapify by default will be min heap
                heapq.heappush(max_heap, -1 * current_element)
                
                if len(max_heap) > k:
                    heapq.heappop(max_heap)
        
        result = -max_heap[0]
        return result


def main():
    n = int(input())
    mat = [list(map(int, input().strip().split()))[:n] for _ in range(n)]
    print("Enter the value of K: ", end="")
    k = int(input())
    solution = Solution()
    print(solution.k_smallest_element(n, mat, k))


if __name__ == "__main__":
    main()
