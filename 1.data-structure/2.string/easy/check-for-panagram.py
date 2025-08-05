"""
Given a string s, check if it is a "Panagram" or not. Return true if the string is a Panagram, else return false.
A "Panagram" is a sentence containing every letter in the English Alphabet either in lowercase or Uppercase.

Examples:

Input: s = "Bawds jog, flick quartz, vex nymph"
Output: true
Explanation: In the given string, there are all the letters of the English alphabet. Hence, the output is true.

Input: s = "sdfs"
Output: false
Explanation: In the given string, there aren't all the letters present in the English alphabet. Hence, the output is false.

Constraints:
1 ≤ |s| ≤ 10^4
s consists only  lowercase and uppercase letters

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)
"""


class Solution:
    def check_panagram(self, s):
        # Count array for storing number of uppercase letters 
        count_arr = [0] * 26
        for ch in s:
            ascii_case_insensitive = ord(ch.upper()) - 65
            if 0 <= ascii_case_insensitive < 26:
                count_arr[ascii_case_insensitive] += 1
        
        # Checking for missing letters in input
        for count in count_arr:
            if count == 0:
                return False
        return True


def main():
    s = input("Enter the string: ").strip()
    solution = Solution()
    print(solution.check_panagram(s))


if __name__ == "__main__":
    main()
