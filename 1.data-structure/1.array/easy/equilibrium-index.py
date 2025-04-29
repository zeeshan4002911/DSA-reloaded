"""
Given an array of integers arr[], the task is to find the first equilibrium point in the array.

The equilibrium point in an array is an index (0-based indexing) such that the sum of all elements before that index is the same as the sum of elements after it. Return -1 if no such point exists.

Examples:

Input: arr[] = [1, 2, 0, 3]
Output: 2
Explanation: The sum of left of index 2 is 1 + 2 = 3 and sum on right of index 2 is 3.

Input: arr[] = [1, 1, 1, 1]
Output: -1
Explanation: There is no equilibrium index in the array.

Input: arr[] = [-7, 1, 5, 2, -4, 3, 0]
Output: 3
Explanation: The sum of left of index 3 is -7 + 1 + 5 = -1 and sum on right of index 3 is -4 + 3 + 0 = -1.

Constraints:
3 <= arr.size() <= 10^5
-10^4 <= arr[i] <= 10^4

"""


class Solution:
    def equilibrium_point(self, arr):
        left_sum = arr[0]
        right_sum = sum(arr)
        for i in range(1, len(arr)):
            left_sum += arr[i - 1]
            right_sum -= arr[i]
            if left_sum == right_sum:
                return i
        return -1


def main():
    arr = [int(value) for value in input().strip().split()]
    solution = Solution()
    print(solution.equilibrium_point(arr))


if __name__ == "__main__":
    main()
