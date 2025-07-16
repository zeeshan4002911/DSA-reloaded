"""
You are given a prefix sum array presum[] of an array arr[]. The task is to find the original array arr[] whose prefix sum is presum[].

Examples:

    Input:  presum[] = {5, 7, 10, 11, 18}
    Output: [5, 2, 3, 1, 7]
    Explanation: Original array {5, 2, 3, 1, 7}
    Prefix sum array = {5, 5+2, 5+2+3, 5+2+3+1, 5+2+3+1+7} = {5, 7, 10, 11, 18}
    Each element of original array is replaced by the sum of the prefix of current index.

    Input: presum[] = {45, 57, 63, 78, 89, 97}
    Output: [45, 12, 6, 15, 11, 8]
"""

class Solution:
    def prefix_sum_reducer(self, arr):
        size = len(arr)
        result = [None] * size
        result[0] = arr[0]
        for i in range(1, len(arr)):
            # Element: Difference of Prefix Element and previous prefix array element
            result[i] = arr[i] - arr[i - 1]
        return result

def main():
    arr = [int(val) for val in input().strip().split()]
    solution = Solution()
    print(solution.prefix_sum_reducer(arr))


if __name__ == "__main__":
    main()
