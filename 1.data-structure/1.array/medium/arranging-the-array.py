"""
Arranging the array

You are given an array of size N. Rearrange the given array in-place such that all the negative numbers occur before all non-negative numbers.
(Maintain the order of all -ve and non-negative numbers as given in the original array).

Example 1:

Input:
N = 4
Arr[] = {-3, 3, -2, 2}
Output:
-3 -2 3 2
Explanation:
In the given array, negative numbers
are -3, -2 and non-negative numbers are 3, 2.

Example 2:

Input:
N = 4
Arr[] = {-3, 1, 0, -2}
Output:
-3 -2 1 0
Explanation:
In the given array, negative numbers
are -3, -2 and non-negative numbers are 1, 0.

Your Task:
You don't need to read input or print anything. Your task is to complete the function Rearrange() which takes the array Arr[] and its size N as inputs and returns the array after rearranging with spaces between the elements of the array.

Expected Time Complexity: O(Nlog(N))
Expected Auxiliary Space: O(log(N))

Constraints:
1 ≤ N ≤ 10^5
-10^9 ≤ Elements of array ≤ 10^9
"""

from typing import List


class Solution:
    def arranging_the_array(self, n: int, arr: List[int]) -> None:
        """
        reverse the positive part of the left array ie, Lp and reverse the negative part of the Right part i.e, Rn.
        """
        self.arranging_the_array_helper(arr, 0, n - 1)
        return arr

    def arranging_the_array_helper(self, arr, left, right):
        if left >= right:
            return
        mid = left + (right - left) // 2
        self.arranging_the_array_helper(arr, left, mid)
        self.arranging_the_array_helper(arr, mid + 1, right)
        self.merge(arr, left, mid, right)

    def merge(self, arr, left, mid, right):
        i = left
        j = mid + 1

        # Move i to the first non-negative in left half
        while i <= mid and arr[i] < 0:
            i += 1

        # Move j to the first non-negative in right half
        while j <= right and arr[j] < 0:
            j += 1
        # Go back to the last negative element in right half
        j -= 1

        # reverse Lp, for left sub-array
        self.reverse(arr, i, mid)
        # reverse Rn, for right sub-array
        self.reverse(arr, mid + 1, j)
        self.reverse(arr, i, j)

    def reverse(self, arr, i, j):
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1


def main():
    arr = [int(value) for value in input().strip().split()]
    solution = Solution()
    print(solution.arranging_the_array(len(arr), arr))


if __name__ == "__main__":
    main()
