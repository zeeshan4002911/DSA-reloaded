"""
Given an array arr[] that contains positive and negative integers (may contain 0 as well). Find the maximum product that we can get in a subarray of arr[].

Note: It is guaranteed that the output fits in a 32-bit integer.

Examples

Input: arr[] = [-2, 6, -3, -10, 0, 2]
Output: 180
Explanation: The subarray with maximum product is {6, -3, -10} with product = 6 * (-3) * (-10) = 180.

Input: arr[] = [-1, -3, -10, 0, 6]
Output: 30
Explanation: The subarray with maximum product is {-3, -10} with product = (-3) * (-10) = 30.

Input: arr[] = [2, 3, 4]
Output: 24
Explanation: For an array with all positive elements, the result is product of all elements.

Constraints:
1 ≤ arr.size() ≤ 10^6
-10  ≤  arr[i]  ≤  10

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)
"""


class Solution:
    def maximum_subarray_product(self, arr):
        """
        At every index i, we keep track of two values:
        max_current: The maximum product that ends at index i.
        min_current: The minimum product that ends at index i (important because a negative * negative = positive).
            Note: If we have a negative number, multiplying it by the current max could become very small (or negative).
            But multiplying it by the current min (if it's negative) could yield a large positive number!
        """
        max_current = arr[0]
        min_current = arr[0]
        max_global = arr[0]
        size = len(arr)
        for i in range(1, size):
            if arr[i] < 0:
                min_current, max_current = max_current, min_current

            max_current = max(max_current * arr[i], arr[i])
            min_current = min(min_current * arr[i], arr[i])
            max_global = max(max_global, max_current)
        return max_global


def main():
    arr = [int(value) for value in input().strip().split()]
    solution = Solution()
    print(solution.maximum_subarray_product(arr))


if __name__ == "__main__":
    main()
