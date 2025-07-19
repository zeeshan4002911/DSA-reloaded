"""
You are given a string s. You need to find the length of the string and return it.

Examples:

Input: s = Geeks
Output: 5

Input: s = Hello1234
Output: 9

Constraints:
1 <= | s |  <= 100000

Expected Complexities
Time Complexity: O(1)
Auxiliary Space: O(1)
"""


class Solution:
    def length_of_string(self, s):
        return len(s)

    def calculate_length_of_string(self, s):
        length = 0
        for _ in s:
            length += 1
        return length


def main():
    s = input("Enter the String: ")
    op = Solution()
    print(op.length_of_string(s))


if __name__ == "__main__":
    main()
