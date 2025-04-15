"""
You are given an array arr of size n - 1 that contains distinct integers in the range from 1 to n (inclusive). This array represents a permutation of the integers from 1 to n with one element missing. Your task is to identify and return the missing element.

Examples:

Input: arr[] = [1, 2, 3, 5]
Output: 4
Explanation: All the numbers from 1 to 5 are present except 4.

Input: arr[] = [8, 2, 4, 5, 3, 7, 1]
Output: 6
Explanation: All the numbers from 1 to 8 are present except 6.

Input: arr[] = [1]
Output: 2
Explanation: Only 1 is present so the missing element is 2.

Constraints:
1 ≤ arr.size() ≤ 106
1 ≤ arr[i] ≤ arr.size() + 1
"""


class Solution:
    def missing_in_array(self, arr):
        """
        Based on the sum of first N natural number formula,
        Missing number will be present in sum of natural number but not included in actual sum of input
        """
        # Given length of arr = n - 1, therefore n = len(arr) + 1
        n = len(arr) + 1
        natural_number_sum = n * (n + 1) // 2
        actual_sum = sum(arr)
        return natural_number_sum - actual_sum


def main():
    arr = [int(value) for value in input().strip().split()]
    solution = Solution()
    print(solution.missing_in_array(arr))


if __name__ == "__main__":
    main()
