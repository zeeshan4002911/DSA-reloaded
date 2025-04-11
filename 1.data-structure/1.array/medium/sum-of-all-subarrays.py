"""
Given an array arr. Find the sum of all subarrays of the array since the sum could be very large print the sum modulo (109+7).

Examples:

Input: arr[] = [1, 2, 3]
Output: 20
Explanation: All subarray sums are: [1] = 1, [2] = 2, [3] = 3, [1,2] = 3, [2,3] = 5, [1,2,3] = 6. Thus total sum is 1+2+3+3+5+6 = 20.

Input: arr[] = [1, 3]
Output: 8
Explanation: All subarray sums are: [1] = 1 [3] = 3 [1,3] = 4. Thus total sum is 1+3+4 = 8.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints :
1 ≤ arr.size() ≤ 106
1 ≤ arr[i] ≤ 109
"""


class Solution:
    def sum_of_subarrays(self, arr) -> int:
        n = len(arr)
        total = 0

        """
        Starting points: from index 0 to i -> i + 1 choices
        Ending points: from index i to n-1 -> n - i choices
        So it appears in (i + 1) * (n - i) subarrays
        """
        for i, ele in enumerate(arr):
            total += ele * (i + 1) * (n - i)

        return total % (10 ** 9 + 7)


def main():
    arr = [int(value) for value in input().strip().split()]
    solution = Solution()
    print(solution.sum_of_subarrays(arr))


if __name__ == "__main__":
    main()
