"""
Kadane's Algorithm
Given an integer array arr[]. You need to find the maximum sum of a subarray.

Examples:

Input: arr[] = [2, 3, -8, 7, -1, 2, 3]
Output: 11
Explanation: The subarray {7, -1, 2, 3} has the largest sum 11.

Input: arr[] = [-2, -4]
Output: -2
Explanation: The subarray {-2} has the largest sum -2.

Input: arr[] = [5, 4, 1, 7, 8]
Output: 25
Explanation: The subarray {5, 4, 1, 7, 8} has the largest sum 25.

Constraints:
1 ≤ arr.size() ≤ 10^5
-109 ≤ arr[i] ≤ 10^4

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)
"""


class Solution:
    def maximum_subarray_sum(self, arr):
        """
        At each index i, Kadane’s algorithm decides whether to:
        1. Extend the previous subarray (current_sum + arr[i])
        2. Or start a new subarray from the current element (arr[i])
        Note: This is basically solving the problem for index i using the solution to index i - 1,
                which is a key feature of dynamic programming though implementation feels greedy.
        """
        max_current = arr[0]
        max_global = arr[0]
        for i in range(1, len(arr)):
            max_current = max(max_current + arr[i], arr[i])
            max_global = max(max_global, max_current)
        return max_global


def main():
    arr = [int(value) for value in input().strip().split()]
    solution = Solution()
    print(solution.maximum_subarray_sum(arr))


if __name__ == "__main__":
    main()
