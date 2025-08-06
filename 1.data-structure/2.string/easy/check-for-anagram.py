"""
Given two non-empty strings s1 and s2, consisting only of lowercase English letters, determine whether they are anagrams of each other or not.
Two strings are considered anagrams if they contain the same characters with exactly the same frequencies, regardless of their order.

Examples:

Input: s1 = "geeks" s2 = "kseeg"
Output: true 
Explanation: Both the string have same characters with same frequency. So, they are anagrams.

Input: s1 = "allergy", s2 = "allergyy" 
Output: false 
Explanation: Although the characters are mostly the same, s2 contains an extra 'y' character. Since the frequency of characters differs, the strings are not anagrams. 

Input: s1 = "listen", s2 = "lists" 
Output: false 
Explanation: The characters in the two strings are not the same — some are missing or extra. So, they are not anagrams.

Constraints:
1 ≤ s1.size(), s2.size() ≤ 10^5
s1, s2 consists of lowercase English letters.

Expected Complexities
Time Complexity: O(n + m)
Auxiliary Space: O(1)
"""


class Solution:
    def check_for_anagram(self, s1, s2):
        # Fixed size array for storing count of letters
        s1_count_arr = [0] * 26
        s2_count_arr = [0] * 26
        
        # Storing the count of s1 based on ascii reference index into count array
        for ele in s1:
            if str(ele).isascii():
                ascii_diff = ord(ele) - ord("a")
                if 0 <= ascii_diff < 26:
                    s1_count_arr[ascii_diff] += 1
        
        # Storing the count of s2 based on ascii reference index into count array
        for ele in s2:
            if str(ele).isascii():
                ascii_diff = ord(ele) - ord("a")
                if 0 <= ascii_diff < 26:
                    s2_count_arr[ascii_diff] += 1
        
        # Checking the equality of both count arrays
        for i in range(26):
            if s1_count_arr[i] != s2_count_arr[i]:
                return False
        return True


def main():
    s1 = input("Enter the s1: ")
    s2 = input("Enter the s2: ")
    solution = Solution()
    print(solution.check_for_anagram(s1, s2))


if __name__ == "__main__":
    main()