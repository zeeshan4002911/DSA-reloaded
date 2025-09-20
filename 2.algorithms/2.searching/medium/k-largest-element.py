"""
Given an array arr[] of positive integers and an integer k, Your task is to return k largest elements in decreasing order.

Examples:

Input: arr[] = [12, 5, 787, 1, 23], k = 2
Output: [787, 23]
Explanation: 1st largest element in the array is 787 and second largest is 23.

Input: arr[] = [1, 23, 12, 9, 30, 2, 50], k = 3
Output: [50, 30, 23]
Explanation: Three Largest elements in the array are 50, 30 and 23.

Input: arr[] = [12, 23], k = 1
Output: [23]
Explanation: 1st Largest element in the array is 23.

Constraints:
1 ≤ k ≤ arr.size() ≤ 10^6
1 ≤ arr[i] ≤ 10^6

Expected Complexities
Time Complexity: k+(n-k)*logk
Auxiliary Space: k+(n-k)*logk
"""

import heapq

class Solution:
    def k_largest_element(self, arr, k):
        size = len(arr)
        min_heap = arr[:k]
        heapq.heapify(min_heap)
        
        for i in range(k, size):
            if arr[i] > min_heap[0]:
                heapq.heapreplace(min_heap, arr[i])
    
        result = []
        while min_heap:
            result.append(heapq.heappop(min_heap))
        
        # For decreasing order
        result.reverse()
        return result


def main():
    arr = [int(value) for value in input().strip().split()]
    k = int(input())
    solution = Solution()
    print(solution.k_largest_element(arr, k))


if __name__ == "__main__":
    main()
