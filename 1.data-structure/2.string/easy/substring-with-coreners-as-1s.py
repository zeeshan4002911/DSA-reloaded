"""
Given a binary string s. You have to count the number of substrings that start and end with 1.

Examples:

Input: s = "1111"
Output: 6
Explanation: There are 6 substrings from the given string. They are "11", "11", "11", "111", "111", "1111".

Input: s = "01101"
Output: 3
Explanation: There are 3 substrings from the given string. They are "11", "101", "1101".

Constraints:
1 ≤ |s| ≤ 10^4

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)
"""


class Solution:
    def binary_string(self, s):
        size = len(s)
        count_1s = 0
        result = 0
        # Counting the number of 1s from end and adding together for result
        for i in range(size - 1, -1, -1):
            if i == size - 1 and s[i] == "1":
                count_1s += 1
            elif s[i] == "1":
                result += count_1s
                count_1s += 1
        return result


def main():
    s = input("Enter the string: ")
    solution = Solution()
    print(solution.binary_string(s))


if __name__ == "__main__":
    main()
