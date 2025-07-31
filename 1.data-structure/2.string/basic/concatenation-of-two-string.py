"""
String concatenation is the process of joining two strings end-to-end to form a single string.

Examples

    Input: s1 = “Hello”, s2 = “World”
    Output: “HelloWorld”
    Explanation: Joining “Hello” and “World” results in “HelloWorld”.

    Input: s1 = “Good”, s2 = “Morning”
    Output: “GoodMorning”
    Explanation: Joining “Good” and “Morning” results in “GoodMorning”
    
Time Complexity : O(m + n) where m and n are lengths of the two 
"""

class Solution:
    def concatenation_of_string(self, s1, s2):
        return s1 + s2

    def computed_concatenation_of_string(self, s1, s2):
        result = ""
        for i in range(len(s1)):
            result += s1[i]
        for i in range(len(s2)):
            result += s2[i]
        return result


def main():
    s1 = input("Enter the first string: ")
    s2 = input("Enter the second string: ")
    solution = Solution()
    print(solution.concatenation_of_string(s1, s2))


if __name__ == "__main__":
    main()
