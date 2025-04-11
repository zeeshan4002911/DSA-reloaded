"""
Given an array arr, rearrange the array according to the following relations :

    arr[i] >= arr[i-1], if i is even.
    arr[i] <= arr[i-1], if i is odd.
    [Considering 1-base indexed array]

Return the rearranged array.

Note: The driver code will print "true" if your output array satisfies the conditions; otherwise, it will print "false".

Example:

Input: arr[] = [1, 2, 2, 1]
Output: [1, 2, 1, 2]
Explanation: Both 2s are at even positions and 1s at odd positions, satisfying the given conditions.

Input: arr[] = [1, 3, 2]
Output: [1, 3, 2]
Explanation: The array is already arranged according to the conditions.

Constraints:
1 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 104

Time Complexity: O(n log n)
Auxiliary Space: O(1)
"""


class Solution:
    def rearrange_even_greater_odd(self, arr: list) -> list:
        size = len(arr)
        for i in range(1, size):
            if (i + 1) % 2 == 0:
                if arr[i] < arr[i - 1]:
                    self.swap(arr, i, i - 1)
            else:
                if arr[i] > arr[i - 1]:
                    self.swap(arr, i, i - 1)
        return arr

    def swap(self, arr, a, b):
        arr[a], arr[b] = arr[b], arr[a]


def main():
    arr = [int(value) for value in input().strip().split()]
    solution = Solution()
    print(solution.rearrange_even_greater_odd(arr))


if __name__ == "__main__":
    main()
