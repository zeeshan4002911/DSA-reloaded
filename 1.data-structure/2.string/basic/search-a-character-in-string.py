"""
Write a program to search for a given character in a string. If the character is found, print the index/position where it first appears in the string. If the character is not found, print -1.

Examples:

Input: s = "geeksforgeeks" , ch = 'k'
Output: 3
Explanation: The character 'k' is present at index 3 and 11 in "geeksforgeeks" , so the first index is 3.

Input: s = "geeksforgeeks" , ch = 'z'
Output: -1
Explanation: The character 'z' is not present in "geeksforgeeks".

Constraints:
1 ≤ |s| ≤ 10^5


Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)
"""


class Solution:
    def search_a_charachter_in_string(self, s1, char):
        return str(s1).find(char[0])

    def calculate_search_a_charachter_in_string(self, s1, char):
        for i, ch in enumerate(s1):
            if ch == char:
                return i

        return -1


def main():
    s1 = input("Enter the String: ")
    char = input("Enter the character: ")
    op = Solution()
    print(op.search_a_charachter_in_string(s1, char))


if __name__ == "__main__":
    main()
