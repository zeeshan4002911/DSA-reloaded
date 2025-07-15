"""
You are given a string s, consisting of lowercase alphabets. Your task is to remove consecutive duplicate characters from the string.

Example:

Input: s = "aabb"
Output:  "ab"
Explanation:
The character 'a' at index 2 is the same as 'a' at index 1, so it is removed.
Similarly, the character 'b' at index 4 is the same as 'b' at index 3, so it is removed.
The final string is "ab".

Input:s = "aabaa"
Output: "aba"
Explanation:
The character 'a' at index 2 is the same as 'a' at index 1, so it is removed.
The character 'a' at index 5 is the same as 'a' at index 4, so it is removed.
The final string is "aba".

Input: s = "abcddcba"
Output: "abcdcba"
Explanation:
The character 'd' at index 5 is the same as 'd' at index 4, so it is removed.
No other consecutive duplicates exist.
The final string is "abcdcba".

Constraints:
1 ≤ n ≤ 10^6
All characters in the string are lowercase English alphabets.

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(n)
"""


class Solution:
    def remove_consecutive_characters(self, s):
        size = len(s)
        result = ""
        
        # For string with one or no character
        if size <= 1:
            return s

        # First character
        result = s[0]
        
        # Adding the current character based on different previous character
        for i in range(1, size):
            if s[i] == s[i - 1]:
                continue
            result += s[i]

        return result


def main():
    s = input()
    solution = Solution()
    print(solution.remove_consecutive_characters(s))


if __name__ == "__main__":
    main()
