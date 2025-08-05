"""
Given two strings s1 and s2 .You have to check that s1 is a subsequence of s2 or not.
Note: A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements.

Examples:

Input: s1 = "AXY", s2 = "YADXCP"
Output: false
Explanation: s1 is not a subsequence of s2 as 'Y' appears before 'A'.

Input: s1 = "gksrek", s2 = "geeksforgeeks"
Output: true
Explanation: If we combine the bold character of "geeksforgeeks", it equals to s1. So s1 is a subsequence of s2.

Constraints:
1 ≤ |s1|,|s2| ≤10^6

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)
"""


class Solution:
    def check_for_subsequence(self, s1, s2):
        # Iterating the main string and checking the s2 with pointer
        j = 0
        for i in range(len(s2)):
            if s2[i] == s1[j]:
                j += 1
            if j == len(s1):
                return True
        return False


def main():
    s1 = input("Enter the s1: ")
    s2 = input("Enter the s2: ")
    solution = Solution()
    print(solution.check_for_subsequence(s1, s2))


if __name__ == "__main__":
    main()
