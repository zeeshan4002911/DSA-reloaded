"""
Given an infix expression in the form of string s. Convert this infix expression to a postfix expression.

    Infix expression: The expression of the form a op b. When an operator is in between every pair of operands.
    Postfix expression: The expression of the form a b op. When an operator is followed for every pair of operands.

Note: The order of precedence is: ^ greater than * equals to / greater than + equals to -. Ignore the right associativity of ^.

Examples :

Input: s = "a+b*(c^d-e)^(f+g*h)-i"
Output: abcd^e-fgh*+^*+i-
Explanation: After converting the infix expression into postfix expression, the resultant expression will be abcd^e-fgh*+^*+i-

Input: s = "A*(B+C)/D"
Output: ABC+*D/
Explanation: After converting the infix expression into postfix expression, the resultant expression will be ABC+*D/

Input: s = "(a+b)*(c+d)"
Output: ab+cd+*

Constraints:
1 ≤ s.length ≤ 30

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(n)
"""

from collections import deque


class Solution:
    def infix_to_postfix_expression(self, s):
        result = ""
        size = len(s)
        st = deque()

        ### Algorithm steps ###
        for i in range(size):
            # 1. Adding all the operand into the result
            if str(s[i]).isalnum():
                result += s[i]

            # 2. Processing for bracket element
            elif s[i] == "(":
                st.append(s[i])
            elif s[i] == ")":
                # On closing bracket popping all the element from stack till the opening bracket and adding to result
                while st and st[-1] != "(":
                    result += st.pop()
                # Removing the opening bracket from the stack
                st.pop()

            # 3. For operator
            else:
                while st and self.precedence_check(s[i]) <= self.precedence_check(st[-1]):
                    result += st.pop()
                st.append(s[i])

        # 4. Adding remaining element of stack
        while st:
            result += st.pop()

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
    print(solution.infix_to_postfix_expression(s))


if __name__ == "__main__":
    main()
