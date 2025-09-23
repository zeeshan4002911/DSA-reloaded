"""
Given an array arr[] of integers and a number x, the task is to find the sum of subarray having a maximum sum less than or equal to the given value of x.

Examples:

Input: arr[] = [1, 2, 3, 4, 5], x = 11
Output: 10
Explanation: Subarray having maximum sum is [1, 2, 3, 4].

Input: arr[] = [2, 4, 6, 8, 10], x = 7
Output: 6
Explanation: Subarray having maximum sum is [2, 4] or [6].

Expected Time Complexity: O(n).
Expected Auxiliary Space: O(1).

Constraints:
1 ≤ arr.size() ≤ 10^6
1 ≤ arr[i] ≤ 10^6
1 ≤ x ≤ 10^12
"""


class Solution:
    # Sliding window approach
    def maximum_sum_of_subarray_of_size_less_than_target(self, arr, x):
        result = 0
        size = len(arr)
        local_sum, left, right = 0, 0, 0

        while right < size:
            local_sum += arr[right]
            right += 1

            # Reducing the size of window from left for optimum subarray
            while left <= right and local_sum > x:
                local_sum -= arr[left]
                left += 1
            
            if local_sum <= x:
                result = max(result, local_sum)

        return result


def main():
    arr = [int(val) for val in input().strip().split()]
    x = int(input("Enter the size of x: "))
    solution = Solution()
    print(solution.maximum_sum_of_subarray_of_size_less_than_target(arr, x))


if __name__ == "__main__":
    main()
