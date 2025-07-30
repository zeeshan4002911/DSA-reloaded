"""
Given a string and a position (0 based), remove a character from the given position.

Examples:

Input: s = "abcde", pos = 1
Output: s = "acde"

Input: s = "a", pos = 0
Output: s = ""

Constraints:
1 ≤ |s| ≤ 2*10^5

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)

"""


class Solution:
    def remove_a_character_from_given_position(self, s, pos):
        if 0 > pos or pos >= len(s):
            return "Position is out of range"
        return s[:pos] + s[pos + 1 :]

    def computed_remove_a_character(self, s, pos):
        if 0 > pos or pos >= len(s):
            return "Position is out of range"

        result = ""
        for i in range(len(s)):
            if i == pos:
                continue
            result += s[i]
        return result


def main():
    s = input("Enter the string: ")
    pos = int(input("Enter the position to remove: "))
    solution = Solution()
    print(solution.computed_remove_a_character(s, pos))


if __name__ == "__main__":
    main()
