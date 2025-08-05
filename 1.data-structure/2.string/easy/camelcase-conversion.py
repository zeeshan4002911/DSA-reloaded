"""
Given a sentence s, your task is to remove all spaces and convert it to Camel Case. In Camel Case, words are joined without spaces, the first word keeps its original case, and each subsequent word starts with an uppercase letter.

Note: It is guaranteed that the sample test cases don't contain leading spaces.

Examples:

Input: s = "i got intern at geeksforgeeks"
Output: "iGotInternAtGeeksforgeeks"
Explanation: All spaces are removed and each word starts with a capital letter, except the first word which retains its original capitalization.

Input: s = "here comes the garden"
Output: "hereComesTheGarden"
Explanation: Spaces are removed and each word after the first is capitalized.

Input: s = "coding is fun"
Output: "codingIsFun"
Explanation: Spaces are removed, the first word retains its original case, and each subsequent word starts with a capital letter.

Constraints:
1 <= s.size() <= 10^6

The string s contains only lowercase english alphabets and spaces.
Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)
"""

class Solution:
    def camecase_conversion(self, s):
        result = ""
        encounter_space_flag = False
        for ele in s:
            if ele == ' ':
                encounter_space_flag = True
                continue
            if encounter_space_flag:
                result += str(ele).upper()
                encounter_space_flag = False
            else:
                result += ele
            
        return result


def main():
    s = input("Enter the string: ").strip()
    solution = Solution()
    print(solution.camecase_conversion(s))


if __name__ == "__main__":
    main()