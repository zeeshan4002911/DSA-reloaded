"""
Given a string s, you need to print all possible strings that can be made by placing spaces (zero or one) in between them. The output should be printed in sorted increasing order of strings.

Example 1:

Input:
s = "ABC"
Output: (A B C)(A BC)(AB C)(ABC)
Explanation:
ABC
AB C
A BC
A B C
These are the possible combination of "ABC".

Example 2:

Input:
s = "BBR"
Output: (B B R)(B BR)(BB R)(BBR)


Your Task:
You don't need to read input or print anything. Your task is to complete the function permutation() which takes the string s as input parameters and returns the sorted array of the string denoting the different permutations (DON'T ADD '(' and ')' it will be handled by the driver code only).

Expected Time Complexity: O(2 ^ s)
Expected Auxiliary Space: O(1)



CONSTRAINTS:
1 <= |s| < 10
s only contains lowercase and Uppercase English letters.
"""


class Solution:
    def permutation_with_spaces(self, s):
        result = []
        n = len(s)
        self.string_generator_helper(s, 0, n, result, "")
        return result

    def string_generator_helper(self, s, i, n, result, gen_s):
        if i >= n:
            result.append(gen_s)
            return
        
        if gen_s == "":
            # Only for the first call stack when generated string is empty
            self.string_generator_helper(s, i + 1, n, result, gen_s + s[i])
        else:
            self.string_generator_helper(s, i + 1, n, result, gen_s + " " + s[i])
            # Backtracking to add zero space in-between character
            self.string_generator_helper(s, i + 1, n, result, gen_s + s[i])


def main():
    s = input("Enter the string: ").strip()
    solution = Solution()
    print(solution.permutation_with_spaces(s))


if __name__ == "__main__":
    main()
