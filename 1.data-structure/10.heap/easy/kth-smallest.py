"""
Given an integer array arr[] and an integer k, your task is to find and return the kth smallest element in the given array.

Note: The kth smallest element is determined based on the sorted order of the array.

Examples :

Input: arr[] = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10], k = 4
Output: 5
Explanation: 4th smallest element in the given array is 5.

Input: arr[] = [7, 10, 4, 3, 20, 15], k = 3
Output: 7
Explanation: 3rd smallest element in the given array is 7.

Constraints:
1 ≤ arr.size() ≤ 10^5
1 ≤ arr[i] ≤ 10^5
1 ≤ k ≤  arr.size()

Expected Complexities
Time Complexity: O(n log k)
Auxiliary Space: O(k)
"""

import heapq

class Solution:
    def kth_smallest(self, arr, k):
        if k > len(arr):
            print("Value of k is out of bound")
            return None
        
        # Python heapq converts list into min-heap by default
        heapq.heapify(arr)

        i = 0
        result = None
        while i < k:
            result = heapq.heappop(arr)
            i += 1

        return result


def main():
    arr = input("Enter array: ").strip().split()
    arr = [int(val.split(",")[0]) for val in arr]
    k = int(input("Enter value of k: ").strip())
    soln = Solution()
    print(soln.kth_smallest(arr, k))


if __name__ == "__main__":
    main()
