"""
Two strings are called k-anagrams if both of the below conditions are true.
1. Both have same number of characters.
2. Two strings can become anagram by changing at most k characters in a string.

Given two strings of lowercase alphabets and an integer value k, the task is to find if two strings are k-anagrams of each other or not.

Example:

Input: s1 = "fodr", s2 = "gork", k = 2
Output: true
Explanation: We can change 'f' -> 'g' and 'd' -> 'k' in s1.

Input: s1 = "geeks", s2 = "eggkf", k = 1
Output: false
Explanation: We can update or modify only 1 value but there is a need of modifying 2 characters i.e. 'g' and 'f' in s2.

Input: s1 = "adb", s2 = "fdab", k = 2
Output: false
Explanation: Both the strings have different numbers of characters.

Constraints:
1 ≤ s1.size(), s2.size() ≤ 10^5
1 ≤ k ≤ 105
Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)
"""


class Solution:
    def check_for_k_anagram(self, s1, s2, k):
        if len(s1) != len(s2):
            return False

        # Fixed size array for storing count of letters
        count_arr = [0] * 26

        # Storing the count of s1 based on ascii reference index into count array
        for ele in s1:
            if str(ele).isascii():
                ascii_diff = ord(ele) - ord("a")
                if 0 <= ascii_diff < 26:
                    count_arr[ascii_diff] += 1

        # Substract of s2 character if similar character is present in s1
        for ele in s2:
            if str(ele).isascii():
                ascii_diff = ord(ele) - ord("a")
                if 0 <= ascii_diff < 26 and count_arr[ascii_diff] > 0:
                    count_arr[ascii_diff] -= 1
        
        # Sum of unique character which is not present in s2
        count_sum = sum(count_arr)
        if count_sum <= k:
            return True

        return False


def main():
    s1 = input("Enter the first string: ")
    s2 = input("Enter the second string: ")
    k = int(input("Enter the value of k: "))
    solution = Solution()
    print(solution.check_for_k_anagram(s1, s2, k))


if __name__ == "__main__":
    main()
