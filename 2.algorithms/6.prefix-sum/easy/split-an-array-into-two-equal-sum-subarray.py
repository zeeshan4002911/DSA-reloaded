"""
Given an array of integers arr, return true if it is possible to split it in two subarrays (without reordering the elements), such that the sum of the two subarrays are equal. If it is not possible then return false.

Examples:

Input: arr = [1, 2, 3, 4, 5, 5]
Output: true
Explanation: In the above example, we can divide the array into two subarrays with equal sum. The two subarrays are: [1, 2, 3, 4] and [5, 5]. The sum of both the subarrays are 10. Hence, the answer is true.

Input: arr = [4, 3, 2, 1]
Output: false
Explanation: In the above example, we cannot divide the array into two subarrays with equal sum. Hence, the answer is false.

Expected Time Complexity: O(n)
Expected Space Complexity: O(1)

Constraints:
1<=arr.size()<=10^5
1<=arr[i]<=10^6
"""


class Solution:
    def split_an_array_into_two_equal_sum_subarray(self, arr):
        # Prefix Sum Approach
        prefix_sum = 0
        suffix_sum = sum(arr)
        for ele in arr:
            prefix_sum += ele
            suffix_sum -= ele
            if prefix_sum == suffix_sum:
                return True
        return False


def main():
    arr = [int(val) for val in input().strip().split()]
    solution = Solution()
    print(solution.split_an_array_into_two_equal_sum_subarray(arr))


if __name__ == "__main__":
    main()
