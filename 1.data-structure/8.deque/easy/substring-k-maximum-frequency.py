"""
Given a string str, the task is to find the substring of length K which occurs the maximum number of times. If more than one string occurs maximum number of times, then print the lexicographically smallest substring.

Examples:

    Input: str = "bbbbbaaaaabbabababa", K = 5
    Output: ababa
    Explanation:
    The substrings of length 5 from the above strings are {bbbbb, bbbba, bbbaa, bbaaa, baaaa, aaaaa, aaaab, aaabb, aabba, abbab, bbaba, babab, ababa, babab, ababa}.
    Among all of them, substrings {ababa, babab} occurs the maximum number of times(= 2).
    The lexicographically smallest string from {ababa, babab} is ababa.
    Therefore, "ababa" is the required answer.


    Input:  str = "heisagoodboy", K = 5
    Output: agood
    Explanation:
    The substrings of length 5 from the above string are {heisa, eisag, isago, sagoo, agood, goodb, oodbo, odboy}.
    All of them occur only once. But the lexicographically smallest string among them is "agood".
    Therefore, "agood" is the required answer.
"""

from collections import deque, defaultdict


class Solution:
    def substring_length_k_with_maximum_frequency(self, s, k):
        size = len(s)
        if k > size:
            return "k size overflow"

        window_size = k
        freq_count = defaultdict(int)
        # Deque for sliding window
        window_deque = deque()

        # Initial window with k size
        for i in range(window_size):
            window_deque.append(s[i])
        freq_count[self.convert_to_string(window_deque)] += 1

        # Sliding the window by adding next element into deque read and removing from front
        for i in range(window_size, size):
            window_deque.popleft()
            window_deque.append(s[i])
            freq_count[self.convert_to_string(window_deque)] += 1

        # Maximum frequency calculation
        max_freq = max(freq_count.values())
        result = None
        
        for substring, freq in freq_count.items():
            # Minimum value in lexicographical order
            if max_freq == freq:
                if result is None:
                    result = substring
                else:
                    result = min(result, substring)

        return result

    def convert_to_string(self, deq):
        s = ""
        for c in deq:
            s += c
        return s


def main():
    s = input("Enter string: ").strip()
    k = int(input("Enter substring size: ").strip())
    solution = Solution()
    print(solution.substring_length_k_with_maximum_frequency(s, k))


if __name__ == "__main__":
    main()
