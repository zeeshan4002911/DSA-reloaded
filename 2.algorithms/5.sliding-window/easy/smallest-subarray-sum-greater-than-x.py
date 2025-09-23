"""
Given a number x and an array of integers arr, find the smallest subarray with sum greater than the given value. If such a subarray do not exist return 0 in that case.

Examples:

Input: x = 51, arr[] = [1, 4, 45, 6, 0, 19]
Output: 3
Explanation: Minimum length subarray is [4, 45, 6]

Input: x = 100, arr[] = [1, 10, 5, 2, 7]
Output: 0
Explanation: No subarray exist

Constraints:
1 ≤ arr.size, x ≤ 10^5
0 ≤ arr[] ≤ 10^4

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)
"""


class Solution:
    def smallest_subarray_sum_greater_than_x(self, arr, x):
        size = len(arr)
        left, right, sum = 0, 0, 0
        result = float("inf")

        # Sliding window using pointers
        while right < size:
            sum += arr[right]
            right += 1

            # Reducing the size of window from left till the condition is valid
            while sum > x:
                result = min(result, right - left)
                sum -= arr[left]
                left += 1

        if result == float("inf"):
            result = 0
        return result


def main():
    x = int(input("Enter value of x: "))
    arr = [int(value) for value in input().strip().split()]
    solution = Solution()
    print(solution.smallest_subarray_sum_greater_than_x(arr, x))


if __name__ == "__main__":
    main()
