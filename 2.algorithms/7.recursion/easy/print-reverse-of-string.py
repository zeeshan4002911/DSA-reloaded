"""
Given a string, the task is to print the given string in reverse order using recursion.

Examples:

    Input: s = "Geeks for Geeks"
    Output: "skeeG rof skeeG"
    Explanation: After reversing the input string we get "skeeG rof skeeG".

    Input: s = "Reverse a string Using Recursion"
    Output: "noisruceR gnisU gnirts a esreveR"
    Explanation: After reversing the input string we get "noisruceR gnisU gnirts a esreveR".
"""


class Solution:
    def reverse_of_string(self, s):
        return self.reverse_rec_helper(s, len(s) - 1, "")

    def reverse_rec_helper(self, s, i, result):
        if i < 0:
            return result

        result += s[i]
        return self.reverse_rec_helper(s, i - 1, result)


def main():
    s = input("Enter the string: ").strip()
    solution = Solution()
    print(solution.reverse_of_string(s))


if __name__ == "__main__":
    main()
