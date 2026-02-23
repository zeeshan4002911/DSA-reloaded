"""
Given an integer array arr[] of size n elements and a positive integer K, the task is to return the k largest element in the given array (not the K distinct element).

Examples:

    Input:  [1, 23, 12, 9, 30, 2, 50], K = 3
    Output: [23, 30, 50]

    Input:  [12, 3, 5, 7, 19], K = 2
    Output: [12, 19]
"""

import heapq


class Solution:
    def kth_largest(self, arr, k):
        if k > len(arr):
            print("Value of k is out of bound")
            return None

        # Python heapq converts list into min-heap by default
        min_heap = []

        for ele in arr:
            heapq.heappush(min_heap, ele)

            # Always maintain k largest element in heap
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        result = []
        # Collating the k largest element in non decreasing order by popping from min heap one by one
        for _ in range(k):
            result.append(heapq.heappop(min_heap))
        return result


def main():
    arr = input("Enter array: ").strip().split()
    arr = [int(val.split(",")[0]) for val in arr]
    k = int(input("Enter value of k: ").strip())
    soln = Solution()
    print(soln.kth_largest(arr, k))


if __name__ == "__main__":
    main()
