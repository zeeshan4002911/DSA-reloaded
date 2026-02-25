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
    def heap_sort_inplace(self, arr):
        n = len(arr)
        # Converting parameter arr to max heap
        for i in range(n // 2 - 1, -1, -1):
            self.sift_down(i, arr, n)

        while n > 0:
            # Swapping the root with the last element
            arr[0], arr[n - 1] = arr[n - 1], arr[0]
            
            # Excluding the last element, to act as a storage for sorted portion
            n -= 1
            
            # Bubbling down the root to place it at it's rigth position in heap
            self.sift_down(0, arr, n)

        return arr

    # Same as heapify method of heap_helper.py
    def sift_down(self, i, arr, n):
        curr_node = i
        left_child = 2 * i + 1
        right_child = 2 * i + 2

        if left_child < n and arr[curr_node] < arr[left_child]:
            curr_node = left_child
        if right_child < n and arr[curr_node] < arr[right_child]:
            curr_node = right_child

        if i != curr_node:
            arr[i], arr[curr_node] = arr[curr_node], arr[i]
            self.sift_down(curr_node, arr, n)

    def heap_sort(self, arr):
        # Python heapq converts list into min-heap by default
        heapq.heapify(arr)

        result = []
        while arr:
            result.append(heapq.heappop(arr))

        arr[:] = result


def main():
    arr = input("Enter array: ").strip().replace(',', ' ').split()
    arr = [int(val) for val in arr]

    soln = Solution()
    soln.heap_sort_inplace(arr)
    print(arr)


if __name__ == "__main__":
    main()
