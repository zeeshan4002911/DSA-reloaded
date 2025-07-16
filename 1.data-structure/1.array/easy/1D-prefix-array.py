"""
Given an array arr[], the goal is to compute its prefix sum array. The prefix sum array, prefixSum[], should be of the same length as arr[], where each element prefixSum[i] represents the sum of all elements from the start of the array up to index i, i.e., prefixSum[i] = arr[0] + arr[1] + .... + arr[i].

Examples:

Input: arr[] = [10, 20, 10, 5, 15]
Output: [10, 30, 40, 45, 60]
Explanation: For each index i, add all the elements from 0 to i:
prefixSum[0] = 10, 
prefixSum[1] = 10 + 20 = 30, 
prefixSum[2] = 10 + 20 + 10 = 40 and so on.

Input: arr[] = [30, 10, 10, 5, 50]
Output: [30, 40, 50, 55, 105]
Explanation: For each index i, add all the elements from 0 to i:
prefixSum[0] = 30, 
prefixSum[1] = 30 + 10 = 40, 

prefixSum[2] = 30 + 10 + 10 = 50 and so on.

Constraints:
1 ≤ arr.size() ≤ 10^5
1 ≤ arr[i] ≤ 10^4

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(n)
"""

class Solution:
    def prefix_sum_generator(self, arr):
        size = len(arr)
        result = [None] * size
        result[0] = arr[0]
        for i in range(1, len(arr)):
            # Prefix Element: Sum of current element and previous prefix array element
            result[i] = result[i - 1] + arr[i]
        return result

def main():
    arr = [int(val) for val in input().strip().split()]
    solution = Solution()
    print(solution.prefix_sum_generator(arr))


if __name__ == "__main__":
    main()