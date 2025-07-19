"""
Given two strings, determine if they are exactly the same, considering case sensitivity.

Examples:

Input: s1 = "abc" , s1 = "abc"
Output: YES

Input: s1 = " " , s2 = " "
Output: YES

Input: s1 = "geeks", s2 = "Geeks"
Output: NO

Constraints:
1 ≤ |s1|, |s2| ≤ 10^5

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)
"""


class Solution:
    def check_for_same(self, s1, s2):
        return s1 == s2

    def calculate_check_for_same(self, s1, s2):
        s1_size = len(s1)
        s2_size = len(s2)
        if s1_size != s2_size:
            return False

        for i in range(s1_size):
            if s1[i] != s2[i]:
                return False

        return True


def main():
    s1 = input("Enter the first String: ")
    s2 = input("Enter the second String: ")
    op = Solution()
    print(op.check_for_same(s1, s2))


if __name__ == "__main__":
    main()
