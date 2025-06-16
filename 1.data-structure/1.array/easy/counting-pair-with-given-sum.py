"""
Given an array arr[] and an integer target. You have to find numbers of pairs in array arr[] which sums up to given target.

Examples:

Input: arr[] = [1, 5, 7, -1, 5], target = 6
Output: 3
Explanation: Pairs with sum 6 are (1, 5), (7, -1) and (1, 5).

Input: arr[] = [1, 1, 1, 1], target = 2
Output: 6
Explanation: Pairs with sum 2 are (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1).

Input: arr[] = [10, 12, 10, 15, -1], target = 125
Output: 0

Constraints:
1 <= arr.size() <= 10^5
-10^4 <= arr[i] <= 10^4
1 <= target <= 10^4

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(n)
"""


class Solution:
    def counting_pair_with_given_sum(self, arr, target):
        sum_counter = 0
        seen_map = dict()
        for ele in arr:
            complement_num = target - ele
            if complement_num in seen_map:
                sum_counter += seen_map[complement_num]
            
            # Increasing the occurence count in seen dictionary
            seen_map[ele] = seen_map.get(ele, 0) + 1
        return sum_counter


def main():
    arr = [int(value) for value in input().strip().split()]
    target = int(input())
    solution = Solution()
    print(solution.counting_pair_with_given_sum(arr, target))


if __name__ == "__main__":
    main()
