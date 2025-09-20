"""
Given two arrays a[] and b[], check if they are disjoint, i.e., there is no element common between both the arrays. Return true if if they are disjoint, otherwise, false.

Examples:

Input: a[] = [2, 34, 11, 9, 3], b[] = [2, 1, 3, 5]
Output: false
Explanation: 3 is common in both the arrays.

Input: a[] = [12, 34, 11, 9, 3], b[] = [7, 2, 1, 5]
Output: true
Explanation: There is no common element in both the sets.

Input: a[] = [1, 2, 3, 4], b[] = [4, 3, 2, 1]
Output: false
Explanation: All the elements are common in both the arrays.

Constraints:
1 <= arr.size() <= 10^6
1 <= arr[i] <= 10^6

Expected Complexities
Time Complexity: O(n + m)
Auxiliary Space: O(n)
"""


class Solution:
    def check_array_disjoint(self, arr_main, arr_sub):
        hash_set = set()
        for ele in arr_main:
            # Storing the element of main array as seen in set
            hash_set.add(ele)

        for ele in arr_sub:
            if ele in hash_set:
                return False
        return True


def main():
    arr_main = input().strip().split()
    arr_sub = input().strip().split()
    solution = Solution()
    print(solution.check_array_disjoint(arr_main, arr_sub))


if __name__ == "__main__":
    main()
