"""
Given a string s, containing lowercase alphabetical characters. The task is to print all non-empty substrings of the given string.

Examples :

    Input :  s = "abc"
    Output :  "a", "ab", "abc", "b", "bc", "c"

    Input :  s = "ab"
    Output :  "a",  "ab",  "b"

    Input :  s = "a"
    Output :  "a"
"""


class Solution:
    def generate_all_substring(self, s):
        size = len(s)
        result = []
        for i in range(size):
            sub_str = ""
            for j in range(i, size):
                sub_str += s[j]
                result.append(sub_str)

        return result

    def generate_all_substring_recurive(self, s):
        def rec_helper(s, i, size, sub_str, result):
            if i == size:
                return

            sub_str += s[i]
            result.append(sub_str)
            rec_helper(s, i + 1, size, sub_str, result)
            
            # Removing the added element of call stack
            sub_str = sub_str[:-1]
            if sub_str == "":
                # Increasing the starting index to get substrings for next element
                rec_helper(s, i + 1, size, sub_str, result)

        size = len(s)
        result = []
        rec_helper(s, 0, size, "", result)
        return result


def main():
    s = input("Enter the string: ")
    solution = Solution()
    print(solution.generate_all_substring(s))


if __name__ == "__main__":
    main()
