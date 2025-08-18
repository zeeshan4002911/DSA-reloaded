"""
Given a string s, the task is to check if it is a palindrome or not.

Examples:

    Input: s = "abba"
    Output: Yes
    Explanation: s is a palindrome

    Input: s = "abc"
    Output: No
    Explanation: s is not a palindrome
"""


class Solution:
    def palindrome_check(self, s):
        return self.two_pointers_rec_helper(s, 0, len(s) - 1)

    def two_pointers_rec_helper(self, s, left, right):
        if left >= right:
            return True
        # Check of left and right character equality
        elif s[left] != s[right]:
            return False
        # Tail recursion for moving pointers
        return self.two_pointers_rec_helper(s, left + 1, right - 1)

def main():
    s = input("Enter string: ").strip()
    solution = Solution()
    print(solution.palindrome_check(s))


if __name__ == "__main__":
    main()
