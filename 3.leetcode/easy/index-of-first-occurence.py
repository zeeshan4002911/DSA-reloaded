"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.



Constraints:

    1 <= haystack.length, needle.length <= 10^4
    haystack and needle consist of only lowercase English characters.

"""

from collections import deque


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        window_size = len(needle)
        size = len(haystack)
        if window_size > size:
            return -1

        queue = deque()
        # Sliding window for searching for needle in haystack
        for i in range(window_size):
            queue.append(haystack[i])

        # Conversion of queue to string to match with needle
        if "".join(list(queue)) == needle:
            return 0

        for i in range(window_size, size):
            queue.popleft()
            queue.append(haystack[i])

            if "".join(list(queue)) == needle:
                return i - (window_size - 1)

        return -1


def main():
    needle = input("Enter needle: ").strip()
    haystack = input("Enter haystack: ").strip()

    soln = Solution()
    print(soln.strStr(haystack, needle))


if __name__ == "__main__":
    main()
