"""
Given two strings s1 and s2, the task is to check if the given strings can be made equal by inserting at most one string to one of the strings at any index.

Examples:

    Input : s1 = "geeksforgeeks", s2 = "geeksgeeks"
    Output : Yes
    Explanation: Add string "for" after 4th index to s2.

    Input: s1 = "geekforgeeks", s2 = "geeksgeeks"
    Output: No
    Explanation: string s1 has extra "for" and s2 has an extra "s".
"""


class Solution:
    def check_if_string_can_be_equal(self, s1, s2):
        if len(s1) == len(s2):
            return s1 == s2
        if len(s1) < len(s2):
            smaller_s = s1
            larger_s = s2
        else:
            smaller_s = s2
            larger_s = s1

        smaller_size = len(smaller_s)
        larger_size = len(larger_s)

        prefix_s = ""
        for i in range(smaller_size):
            if smaller_s[i] != larger_s[i]:
                break
            prefix_s += smaller_s[i]

        suffix_s = ""
        for j in range(smaller_size):
            if smaller_s[smaller_size - 1 - j] != larger_s[larger_size - 1 - j]:
                break
            suffix_s += smaller_s[j]

        if prefix_s + suffix_s == smaller_s:
            return True
        return False


def main():
    s1 = input("Enter the first text: ").strip()
    s2 = input("Enter the first text: ").strip()
    solution = Solution()
    print(solution.check_if_string_can_be_equal(s1, s2))


if __name__ == "__main__":
    main()
