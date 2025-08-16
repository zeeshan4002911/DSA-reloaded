"""
Given a string s, replace all the spaces in the string with '%20'.

Examples:

Input: s = "Mr Benedict Cumberbatch"i love programming
Output: "Mr%20Benedict%20Cumberbatch"
Explanation: The 2 spaces are replaced by '%20'

Input: s = "i love programming"
Output: "i%20love%20programming"
Explanation: The 2 spaces are replaced by '%20'

Constraints:
1 <= n <= 10
"""

import urllib.parse

class Solution:
    def URLify(self, s):
        return s.replace(" ", "%20")
    
    def URLify_builtin(self, s):
        return urllib.parse.quote(s)


def main():
    s = input("Enter the string: ").strip()
    solution = Solution()
    print(solution.URLify_builtin(s))


if __name__ == "__main__":
    main()
