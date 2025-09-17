"""
Given a non-decreasing array arr[] and an integer k,
find the minimum possible value of the maximum difference between adjacent elements after removing k elements from the array.
Note: k < n - 2.

Examples:

    Input: arr[] = [3, 7, 8, 10, 14], k = 2
                    [4, 1, 2, 4]
    Output: 2
    Explanation: After removing elements arr[0] and arr[4],
    the remaining array is [7, 8, 10]. The maximum difference between adjacent elements is 2 which is minimum.

    Input: arr[] = [12, 16, 22, 31, 31, 38], k = 3
                   [4, 6, 9, 0, 7]
    Output: 6
    Explanation: After removing elements arr[3], arr[4] and arr[5],
    the remaining array is [12, 16, 22]. The maximum difference between adjacent elements is 6 which is minimum.
"""

from collections import deque


class Solution:
    def minimize_the_maximum_difference(self, arr, k):
        size = len(arr)
        if k >= size - 2:
            return "k size overflow"

        window_size = size - k
        result_min = float("inf")
        window_deque = deque()

        for i in range(1, window_size):
            window_deque.append(arr[i] - arr[i - 1])

        result_min = min(result_min, max(window_deque))

        for i in range(window_size, size):
            window_deque.popleft()
            window_deque.append(arr[i] - arr[i - 1])
            result_min = min(result_min, max(window_deque))

        return result_min


def main():
    arr = [int(val) for val in input("Enter numbers: ").strip().split()]
    k = int(input("Enter k size: ").strip())
    solution = Solution()
    print(solution.minimize_the_maximum_difference(arr, k))


if __name__ == "__main__":
    main()
