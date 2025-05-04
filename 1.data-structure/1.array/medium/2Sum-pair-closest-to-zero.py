"""
Given an integer array of N elements. You need to find the maximum sum of two elements such that sum is closest to zero.

Example 1:

Input:
N = 3
arr[] = {-8 -66 -60}
Output: -68
Explanation: Sum of two elements closest to
zero is -68 using numbers -60 and -8.

Example 2:

Input:
N = 6
arr[] = {-21 -67 -37 -18 4 -65}
Output: -14
Explanation: Sum of two elements closest to
zero is -14 using numbers -18 and 4.

Note : In Case if we have two of more ways to form sum of two elements closest to zero return the maximum sum.


Your Task:
You don't need to read input or print anything. You just need to complete the function closestToZero() which takes an array arr[] and its size n as inputs and returns the maximum sum closest to zero that can be formed by summing any two elements in the array.


Expected Time Complexity: O(N*logN).
Expected Auxiliary Space: O(1).


Constraints:
2 ≤ N ≤ 5 * 10^5
-106 ≤ arr[i] ≤ 10^6
"""


class Solution:
    def closestToZero(self, arr, n):
        # Sorting of Array due to required time and space complexity
        arr.sort()

        i = 0
        j = n - 1
        closest_sum = float("inf")
        result = float("inf")
        while i < j:
            s = arr[i] + arr[j]
            if abs(s) < abs(closest_sum):
                closest_sum = s
                result = s
            # Condition to handle special case of having same closest sum, result would be maximum of both
            elif abs(s) == abs(closest_sum):
                result = max(result, s)
            if s < 0:
                i += 1
            elif s > 0:
                j -= 1
            else:
                return 0

        return result


def main():
    arr = [int(value) for value in input().strip().split()]
    solution = Solution()
    print(solution.closestToZero(arr, len(arr)))


if __name__ == "__main__":
    main()
