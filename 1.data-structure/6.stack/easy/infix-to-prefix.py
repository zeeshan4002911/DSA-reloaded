"""
You are given an infix expression in the form of a string s, consisting of:

    Lowercase alphabetical operands (a to z).
    Standard arithmetic operators: +, -, *, /, ^.
    Optional parentheses for grouping.

Your task is to convert this infix expression into its equivalent prefix expression and return it as a string.

Examples:

Input: s = "a*b+c/d"
Output: +*ab/cd
Explaination: In prefix notation, operators come before their operands a*b → *ab, c/d → /cd
Since * and / have higher precedence than +, we evaluate them first, then apply +, So the final prefix expression is: +*ab/cd

Input: s = "(a-b/c)*(a/k-l)"
Output: *-a/bc-/akl
Explaination: Convert inner divisions first : b/c → /bc , a/k → /ak
Handle subtractions next: a-b/c → -a/bc, a/k-l → -/akl
Finally, apply multiplication:
(a-b/c) * (a/k-l) → *-a/bc-/akl

Constraints:
1 ≤ s.size() ≤ 10^5

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(n)
"""


class Solution:
    def infix_to_prefix_expression(self, s):
        result = ""
        size = len(s)
        st = []

        ### Algorithm steps ###
        # 0. Reverse the input infix expression
        s = s[::-1]

        for i in range(size):
            # 1. Adding all the operand into the result
            if str(s[i]).isalnum():
                result += s[i]

            # 2. Processing for bracket element, considering the reverse effect [ i.e., ')' to '(' ]
            elif s[i] == ")":
                st.append("(")
            elif s[i] == "(":
                while st and st[-1] != "(":
                    result += st.pop()
                # Removing the opening bracket from the stack
                st.pop()

            # 3. For operator
            else:
                if s[i] == "^":
                    while st and self.precedence_check(s[i]) <= self.precedence_check(
                        st[-1]
                    ):
                        result += st.pop()
                else:
                    while st and self.precedence_check(s[i]) < self.precedence_check(
                        st[-1]
                    ):
                        result += st.pop()
                st.append(s[i])

        # 4. Adding remaining element of stack
        while st:
            result += st.pop()

        # 5. Reverse of result
        result = result[::-1]
        return result

    def precedence_check(self, char):
        if char == "^":
            return 3
        elif char in ["*", "/"]:
            return 2
        elif char in ["+", "-"]:
            return 1
        return -1


def main():
    s = input("Enter infix expression: ").strip()
    solution = Solution()
    print(solution.infix_to_prefix_expression(s))


if __name__ == "__main__":
    main()
