"""
Given two arrays a[] and b[], your task is to determine whether b[] is a subset of a[].

Examples:

Input: a[] = [11, 7, 1, 13, 21, 3, 7, 3], b[] = [11, 3, 7, 1, 7]
Output: true
Explanation: b[] is a subset of a[]

Input: a[] = [1, 2, 3, 4, 4, 5, 6], b[] = [1, 2, 4]
Output: true
Explanation: b[] is a subset of a[]

Input: a[] = [10, 5, 2, 23, 19], b[] = [19, 5, 3]
Output: false
Explanation: b[] is not a subset of a[]

Constraints:
1 <= a.size(), b.size() <= 10^5
1 <= a[i], b[j] <= 10^6

Expected Complexities
Time Complexity: O(n + m)
Auxiliary Space: O(n)
"""


class Solution:
    def check_subset(self, arr_main, arr_sub):
        hash_map = {}
        for ele in arr_main:
            # Storing the count of element of main array using dict getter with default value 0
            hash_map[ele] = hash_map.get(ele, 0) + 1

        for ele in arr_sub:
            if ele not in hash_map or (ele in hash_map and hash_map[ele] == 0):
                return False
            else:
                hash_map[ele] = hash_map[ele] - 1
        return True


def main():
    arr_main = input().strip().split()
    arr_sub = input().strip().split()
    solution = Solution()
    print(solution.check_subset(arr_main, arr_sub))


if __name__ == "__main__":
    main()
