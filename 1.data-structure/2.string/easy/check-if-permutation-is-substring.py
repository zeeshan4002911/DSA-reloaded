"""
Given two strings txt and pat having lowercase letters, the task is to check if any permutation of pat is a substring of txt.

Examples:

Input: txt = "geeks", pat = "eke"
Output: true
Explanation: "eek" is a permutation of "eke" which exists in "geeks".

Input: txt = "programming", pat = "rain"
Output: false
Explanation: No permutation of "rain" exists as a substring in "programming".

Constraints:
1 ≤ txt.size() ≤ 10^5
1 ≤ pat.size() ≤ txt.size()
Both the strings consist of lowercase English alphabets.

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)
"""

from collections import Counter


class Solution:
    # Sliding window approach
    def check_if_permutation_is_substring(self, txt, pat):
        txt_size = len(txt)
        pat_size = len(pat)
        txt_count_map = {}
        pat_count_map = {}

        # Condition to prevent window size larger than input
        if pat_size > txt_size:
            return False

        # Calcualtion for pattern charachters count using Counter
        pat_count_map = Counter(pat)
        txt_count_map = Counter(txt[:pat_size])

        if txt_count_map == pat_count_map:
            return True

        # Window slide by adding next window element count and decreasing/removing initial window element
        for i in range(pat_size, txt_size):
            start_char = txt[i - pat_size]
            end_char = txt[i]

            # Counter will fill 0 instead of keyError, but code is there for logic
            if end_char not in txt_count_map:
                txt_count_map[end_char] = 0

            txt_count_map[end_char] += 1
            txt_count_map[start_char] -= 1

            # Cleaning the local count dictionary
            if txt_count_map[start_char] == 0:
                del txt_count_map[start_char]

            if txt_count_map == pat_count_map:
                return True

        return False


def main():
    txt = input("Enter txt: ")
    pattern = input("Enter pat: ")
    solution = Solution()
    print(solution.check_if_permutation_is_substring(txt, pattern))


if __name__ == "__main__":
    main()
