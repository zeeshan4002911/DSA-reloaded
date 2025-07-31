"""
You are given a string s, and your task is to reverse the string.

Examples:

Input: s = "Geeks"
Output: "skeeG"

Input: s = "for"
Output: "rof"

Input: s = "a"
Output: "a"

Constraints:
1 <= s.size() <= 10^6
s contains only alphabetic characters (both uppercase and lowercase).

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)
"""

class Solution:
    def reverse_a_string(self, s):
        return s[::-1]

    def compute_reverse_a_string(self, s):
        result = ""
        for i in range(len(s) - 1, -1, -1):
            result += s[i]
        return result


def main():
    s = input("Enter the string: ")
    solution = Solution()
    print(solution.reverse_a_string(s))


if __name__ == "__main__":
    main()
