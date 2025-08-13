"""
Given a string s, your task is to determine the length of the longest substring that lies between two identical characters in the string. The substring should exclude the characters at the two ends. If no such pair of identical characters exists, return -1.

Examples:

    Input: s = "accabbacc"
    Output: 6
    Explanation: The matching characters are 'c' at positions 1 and 8. Substring between them is "cabbac", of length 6.

    Input: s = "aa"
    Output: 0
    Explanation: Matching characters 'a' are at positions 0 and 1. No characters in between, so length is 0.

    Input: s = "abcd"
    Output: -1
    Explanation: No repeated characters exist, hence no valid substring between same characters.

"""

from collections import defaultdict


class Solution:
    def longest_substring_between_equals(self, s):
        index_ref = defaultdict(lambda: [None, None])

        # Storing the first and last occurence index for each character
        for i, ele in enumerate(s):
            if index_ref[ele][0] is None:
                index_ref[ele][0] = i
            else:
                index_ref[ele][1] = i

        result = -1
        for value in index_ref.values():
            if value[0] is not None and value[1] is not None:
                # Substract by 1 to exclude the end element, 0 based index exclude the first element
                substring_len = value[1] - value[0] - 1
                result = max(result, substring_len)

        return result


def main():
    s = input("Enter the string: ").strip()
    solution = Solution()
    print(solution.longest_substring_between_equals(s))


if __name__ == "__main__":
    main()
