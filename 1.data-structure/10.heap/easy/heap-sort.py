"""
Given an array arr[]. The task is to sort the array elements by Heap Sort.

Examples:

Input: arr[] = [4, 1, 3, 9, 7]
Output: [1, 3, 4, 7, 9]
Explanation: After sorting elements using heap sort, elements will be in order as 1, 3, 4, 7, 9.

Input: arr[] = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Explanation: After sorting elements using heap sort, elements will be in order as 1, 2, 3, 4, 5, 6, 7, 8, 9, 10.

Input: arr[] = [2, 1, 5]
Output: [1, 2, 5]
Explanation: After sorting elements using heap sort, elements will be in order as 1, 2, 5.

Constraints:
1 ≤ arr.size() ≤ 10^6
1 ≤ arr[i] ≤ 10^6

Expected Complexities
Time Complexity: O(n log n)
Auxiliary Space: O(1)
"""

import heapq


class Solution:
    def heap_sort(self, arr):
        # Python heapq converts list into min-heap by default
        heapq.heapify(arr)

        while arr:
            print(heapq.heappop(arr), end=" ")


def main():
    arr = input("Enter array: ").strip().split()
    arr = [int(val.split(",")[0]) for val in arr]

    soln = Solution()
    soln.heap_sort(arr)


if __name__ == "__main__":
    main()
