"""
Given an array of integers arr[], the task is to find the minimum and maximum elements in the array using recursion only.

Examples:

    Input: arr[] = [1, 4, 3, -5, -4, 8, 6]
    Output: min = -5, max = 8

    Input: arr[] = [1, 4, 45, 6, 10, -8]
    Output: min = -8, max = 45

    Input: arr[] = [12, 3, 15, 7, 9]
    Output: min = 3, max = 15
"""


class Solution:
    def min_and_max_element_of_array(self, arr):
        local_min = float("inf")
        local_max = -float("inf")
        n = len(arr)
        return self.search_rec_helper(arr, n, 0, local_min, local_max)

    def search_rec_helper(self, arr, n, i, local_min, local_max):
        if n == i:
            return (local_min, local_max)

        local_min = min(local_min, arr[i])
        local_max = max(local_max, arr[i])
        return self.search_rec_helper(arr, n, i + 1, local_min, local_max)


def main():
    arr = [int(val) for val in input("Enter array: ").strip().split()]
    solution = Solution()
    print(solution.min_and_max_element_of_array(arr))


if __name__ == "__main__":
    main()
