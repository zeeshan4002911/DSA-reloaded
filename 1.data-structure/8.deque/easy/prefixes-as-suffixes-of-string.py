"""
Given a string S consisting of N characters, the task is to find the length of all prefixes of the given string S that are also suffixes of the same string S.

Examples:

    Input: S = "ababababab"
    Output: 2 4 6 8
    Explanation:
    The prefixes of S that are also its suffixes are:


        "ab" of length = 2
        "abab" of length = 4
        "ababab" of length = 6
        "abababab" of length = 8



    Input: S = "geeksforgeeks"
    Output: 5

"""

import collections


class Solution:
    def length_of_prefixes_as_suffixes(self, s):
        result = []
        size = len(s)
        sliding_window_1 = ""
        sliding_window_2 = collections.deque()

        for i in range(size - 1):
            sliding_window_1 += s[i]
            sliding_window_2.appendleft(s[size - 1 - i])
            if sliding_window_1 == "".join(list(sliding_window_2)):
                result.append(i + 1)
        return result


def main():
    s = input("Enter the string: ").strip()
    solution = Solution()
    print(solution.length_of_prefixes_as_suffixes(s))


if __name__ == "__main__":
    main()
