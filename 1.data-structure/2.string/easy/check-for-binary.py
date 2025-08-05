"""
Given a non-empty sequence of characters s, return true if sequence is Binary, else return false.

Examples:

Input: s = "101"
Output: true
Explanation: Since string contains only '0' and '1', output is true.

Input: s = "75"
Output: false
Explanation: Since string contains digits other than '0' and '1', output is false.

Constraints:
1 <= s.size() <= 10^5

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)
"""


class Solution:
    def check_for_binary(self, s):
        for ele in s:
            if ele == '0' or ele == '1':
                continue
            return False
        return True


def main():
    s = input("Enter the string: ")
    solution = Solution()
    print(solution.check_for_binary(s))


if __name__ == "__main__":
    main()
