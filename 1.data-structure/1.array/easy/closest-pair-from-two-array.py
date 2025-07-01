"""
Given two sorted arrays arr and brr and a number x, find the pair whose sum is closest to x and the pair has an element from each array. In the case of multiple closest pairs return any one of them.
Note: Can return the two numbers in any manner. The driver code takes care of the printing of the closest difference.

Example 1:

Input : N = 4, M = 4
arr[ ] = {1, 4, 5, 7}
brr[ ] = {10, 20, 30, 40}
X = 32
Output :
1, 30
Explanation:
The closest pair whose sum is closest
to 32 is {1, 30} = 31.

Example 2:

Input : N = 4, M = 4
arr[ ] = {1, 4, 5, 7}
brr[ ] = {10, 20, 30, 40}
X = 50
Output :
7, 40
Explanation:
The closest pair whose sum is closest
to 50 is {7, 40} = 47.

Your Task:
You only need to complete the function printClosest() that takes an array (arr), another array (brr), size of array arr (N), size of array brr (M), and return the array of two integers whose sum is closest to X. The driver code takes care of the printing of the closest difference.

Expected Time Complexity: O(N+M).
Expected Auxiliary Space: O(1).

Constraints:
1 ≤ N, M ≤ 10^5
1 ≤ A[i], B[i] ≤ 10^9
"""


class Solution:
    def two_sum_pair_with_closest_sum_from_two_array(self, arr, brr, n, m, target):
        left, right = 0, m - 1
        closeness = float("inf")
        result = []

        while left < n and right >= 0:
            local_sum = arr[left] + brr[right]

            # Closeness check and update base on condition
            local_closeness = abs(local_sum - target)
            if local_closeness < closeness:
                closeness = local_closeness
                result = [arr[left], brr[right]]
            
            # Normal two pointers approach
            elif local_sum < target:
                left += 1
            elif local_sum > target:
                right -= 1
            else:
                return [arr[left], brr[right]]

        return result


def main():
    arr = [int(value) for value in input("Enter first array: ").strip().split()]
    brr = [int(value) for value in input("Enter second array: ").strip().split()]
    target = int(input("Enter the value of target: "))
    solution = Solution()
    print(
        solution.two_sum_pair_with_closest_sum_from_two_array(
            arr, brr, len(arr), len(brr), target
        )
    )


if __name__ == "__main__":
    main()
