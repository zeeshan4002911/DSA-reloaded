"""
Given an array arr[]. The task is to find the largest element and return it.

Examples:

Input: arr[] = [1, 8, 7, 56, 90]
Output: 90
Explanation: The largest element of the given array is 90.

Input: arr[] = [5, 5, 5, 5]
Output: 5
Explanation: The largest element of the given array is 5.

Input: arr[] = [10]
Output: 10
Explanation: There is only one element which is the largest.

Constraints:
1 <= arr.size()<= 10^6
0 <= arr[i] <= 10^6

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)
"""

import math


class Solution:
    def getMax(self, arr):
        maxValue = -math.inf
        for ele in arr:
            if ele > maxValue:
                maxValue = ele
        return maxValue


def main():
    t = int(input())
    while t > 0:
        arr = [int(value) for value in input().strip().split()]
        solution = Solution()
        print(solution.getMax(arr))
        t -= 1


if __name__ == "__main__":
    main()
