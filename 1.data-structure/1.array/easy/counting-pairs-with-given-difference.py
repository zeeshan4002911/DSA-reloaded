"""
Given an array arr[] of positive integers. Find the number of pairs of integers whose absolute difference equals to a given number k.
Note: (a, b) and (b, a) are considered the same. Also, the same numbers at different indices are considered different.

The answer is guaranteed to fit in a 32-bit integer.

Examples:

Input: arr[] = [1, 4, 1, 4, 5], k = 3
Output: 4
Explanation: There are 4 pairs with absolute difference 3, the pairs are {1, 4}, {1, 4}, {4, 1} and {1, 4}.

Input: arr[] = [8, 16, 12, 16, 4, 0], k = 4
Output: 5
Explanation: There are 5 pairs with absolute difference 4, the pairs are {8, 12}, {8, 4}, {16, 12}, {12, 16}, {4, 0}.

Constraints:
1 <= arr.size() <= 2*10^5
1 <= k <= 2*10^5
0 <= arr[i] <= 10^5

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(n)
"""


class Solution:
    def counting_pairs_with_given_diff(self, arr, target):
        sum_counter = 0
        seen_map = dict()
        for ele in arr:
            pos_complement_num = ele + target
            neg_complement_num = ele - target
            # Due to absolute value, difference of pairs (target) can be positive or negative
            if pos_complement_num in seen_map:
                sum_counter += seen_map[pos_complement_num]

            if neg_complement_num in seen_map:
                sum_counter += seen_map[neg_complement_num]

            # Increasing the occurence count in seen dictionary
            seen_map[ele] = seen_map.get(ele, 0) + 1
        return sum_counter


def main():
    arr = [int(value) for value in input().strip().split()]
    target = int(input())
    solution = Solution()
    print(solution.counting_pairs_with_given_diff(arr, target))


if __name__ == "__main__":
    main()
