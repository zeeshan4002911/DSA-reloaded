"""

Given a string s, a character c and an integer position pos, the task is to insert the character c into the string s at the specified position pos.

Examples:

    Input: s = "Geeks", c = 'A', pos = 3
    Output: GeeAks

    Input: s = "HelloWorld", c = '!', pos = 5
    Output: Hello!World
"""


class Solution:
    def insert_a_character(self, s, char, pos):
        return s[:pos] + char + s[pos:]

    def calculated_insert_a_character(self, s, char, pos):
        result = ""
        for i, ch in enumerate(s):
            if i == pos:
                result += char
            result += ch

        if pos >= len(s):
            result += char

        return result


def main():
    s = input("Enter String: ")
    char = input("Enter character to insert: ")
    pos = int(input("Enter position to insert: "))
    solution = Solution()
    print(solution.calculated_insert_a_character(s, char, pos))


if __name__ == "__main__":
    main()
