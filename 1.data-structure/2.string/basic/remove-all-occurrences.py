"""
Given a string s and a character c. The task is to remove all the occurrences of the character in the string.

Examples:

Input: s = "geeksforgeeks", c = 'e'
Output: s = "gksforgks"

Input: s = "geeksforgeeks", c = 'g'
Output: s = "eeksforeeks"

Constraints:
1 <= |s| <= 10^5

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)
"""

class Solution:
    def remove_all_occurences(self, s, ch):
        return str(s).replace(ch, '')

    def computed_remove_all_occurences(self, s, ch):
        result = ""
        for c in s:
            if c == ch:
                continue
            result += c
        return result


def main():
    s = input("Enter the string: ")
    pos = input("Enter the character to remove: ")
    solution = Solution()
    print(solution.remove_all_occurences(s, pos))


if __name__ == "__main__":
    main()
