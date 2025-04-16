"""
Given an array, arr[], of size n, filled with numbers from 1 to n-1 in random order. The array has only one repetitive element. Your task is to find the repetitive element.

Note: It is guaranteed that there is a repeating element present in the array.

Examples:

Input: arr[] = [1, 3, 2, 3, 4]
Output: 3
Explanation: The number 3 is the only repeating element.

Input: arr[] = [1, 5, 1, 2, 3, 4]
Output: 1
Explanation: The number 1 is the only repeating element.

Input: arr[] = [1, 1]
Output: 1
Explanation: The array is of size 2 with both elements being 1, making 1 the repeating element.

Constraints:
2 <= arr.size() <= 105
1 <= arr[i] <= n-1
"""


class Solution:
    def repetitive_in_array(self, arr):
        """
        Based on the sum of first N natural number formula,
        Repetitive number will be present in actual sum of input but not included in natural numbers sum
        """
        # Given length of n = (size of array - 1), therefore n = len(arr) - 1
        n = len(arr) - 1
        natural_sum = n * (n + 1) // 2
        actual_sum = sum(arr)
        return actual_sum - natural_sum


def main():
    arr = [int(value) for value in input().strip().split()]
    solution = Solution()
    print(solution.repetitive_in_array(arr))


if __name__ == "__main__":
    main()
