"""
Given a single string s, the task is to check if it is a palindrome sentence or not. A palindrome sentence is a sequence of characters, such as word, phrase, or series of symbols that reads the same backward as forward after converting all uppercase letters to lowercase and removing all non-alphanumeric characters (including spaces and punctuation).

Examples:

Input: s = "Too hot to hoot"
Output: true
Explanation: If we remove all non-alphanumeric characters and convert all uppercase letters to lowercase, string s will become "toohottohoot" which is a palindrome.

Input: s = "Abc 012..## 10cbA"
Output: true
Explanation: If we remove all non-alphanumeric characters and convert all uppercase letters to lowercase, string s will become "abc01210cba" which is a palindrome.

Input: s = "ABC $. def01ASDF"
Output: false
Explanation: The processed string becomes "abcdef01asdf", which is not a palindrome.

Constraints:
1 ≤ s.length() ≤ 10^6

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)
"""


class Solution:
    def check_palindrome_sentence(self, s):
        s_arr = list(s)
        left, right = 0, len(s_arr) - 1
        # 2-pointers method
        while left < right:
            if not str(s_arr[left]).isalnum():
                left += 1
            elif not str(s_arr[right]).isalnum():
                right -= 1
            elif str(s_arr[left]).lower() == str(s_arr[right]).lower():
                left += 1
                right -= 1
            else:
                return False
        return True


def main():
    s = input()
    solution = Solution()
    print(solution.check_palindrome_sentence(s))


if __name__ == "__main__":
    main()
