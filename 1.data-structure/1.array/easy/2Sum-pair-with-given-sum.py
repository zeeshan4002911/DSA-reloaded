"""
Given an array arr[] of positive integers and another integer target. Determine if there exist two distinct indices such that the sum of their elements is equal to the target.

Examples:

Input: arr[] = [1, 4, 45, 6, 10, 8], target = 16
Output: true
Explanation: arr[3] + arr[4] = 6 + 10 = 16.

Input: arr[] = [1, 2, 4, 3, 6], target = 11
Output: false
Explanation: None of the pair makes a sum of 11.

Input: arr[] = [11], target = 11
Output: false
Explanation: No pair is possible as only one element is present in arr[].

Constraints:
1 ≤ arr.size ≤ 10^5
1 ≤ arr[i] ≤ 10^5
1 ≤ target ≤ 2*10^5

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(n)
"""


class Solution:
    def two_sum_pair_with_given_sum(self, arr, target):
        """
        For Sorted Array: Two-pointers approach [TC: O(n), SC: O(1)]
        For unsorted Array: Hash set [TC: O(n), SC: O(n)]
        """
        hash_set = set()
        for ele in arr:
            complement_num = target - ele
            if complement_num in hash_set:
                return True
            hash_set.add(ele)
        return False


def main():
    arr = [int(value) for value in input().strip().split()]
    print("Enter the value of target:", end=" ")
    target = int(input())
    solution = Solution()
    print(solution.two_sum_pair_with_given_sum(arr, target))


if __name__ == "__main__":
    main()
