"""
Count 1’s in a sorted binary array
Last Updated : 07 Mar, 2025

Given a binary array arr[] of size n, which is sorted in non-increasing order, count the number of 1’s in it.

Examples:

    Input: arr[] = [1, 1, 0, 0, 0, 0, 0]
    Output: 2
    Explanation: Count of the 1’s in the given array is 2.

    Input: arr[] = [1, 1, 1, 1, 1, 1, 1]
    Output: 7

    Input: arr[] = [0, 0, 0, 0, 0, 0, 0]
    Output: 0

"""


class Solution:
    def count_1s_linear_search(self, arr):
        size = len(arr)
        for i in range(size):
            if arr[i] == 0:
                # return of index as length on 0s discovery
                return i
        # For all 1s case
        return size

    def count_1s_binary_search(self, arr):
        size = len(arr)
        return self.binary_search_handler(arr, 0, size - 1)

    def binary_search_handler(self, arr, low, high):
        if low > high:
            return 0
        mid = low + (high - low) // 2
        if arr[mid] == 0:
            result = self.binary_search_handler(arr, low, mid - 1)
        elif mid == len(arr) - 1 or arr[mid + 1] == 0:
            # index + 1 as length on 1s -> 0s discovery
            result = mid + 1
        else:
            result = self.binary_search_handler(arr, mid + 1, high)
        return result


def main():
    arr = [int(value) for value in input().strip().split()]
    solution = Solution()
    print(solution.count_1s_binary_search(arr))


if __name__ == "__main__":
    main()
