"""
Given a string s, composed of different combinations of '(' , ')', '{', '}', '[', ']'. Determine whether the Expression is balanced or not.
An expression is balanced if:

    Each opening bracket has a corresponding closing bracket of the same type.
    Opening brackets must be closed in the correct order.

Examples :

Input: s = "[{()}]"
Output: true
Explanation: All the brackets are well-formed.

Input: s = "[()()]{}"
Output: true
Explanation: All the brackets are well-formed.

Input: s = "([]"
Output: false
Explanation: The expression is not balanced as there is a missing ')' at the end.

Input: s = "([{]})"
Output: false
Explanation: The expression is not balanced as there is a closing ']' before the closing '}'.

Constraints:
1 ≤ s.size() ≤ 10^6
s[i] ∈ {'{', '}', '(', ')', '[', ']'}

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(n)
"""


class Solution:
    def check_balanced_parenthesis(self, s):
        st = []

        for char in s:
            # Adding all the opening braces into the stack
            if char == "(" or char == "{" or char == "[":
                st.append(char)
            # For each closing brace peeking opening and popping it out
            elif (
                (char == ")" and st and st[-1] == "(")
                or (char == "}" and st and st[-1] == "{")
                or (char == "]" and st and st[-1] == "[")
            ):
                st.pop()
            # In case of not popping out the top charachter
            else:
                return False

        # For a valid stack all the opening will get popped out because of closeing brace
        if st:
            return False
        
        # Return of True when stack is empty at the end, and all the braces are balanced
        return True


def main():
    s = input("Enter parethesis expression: ").strip()
    solution = Solution()
    print(solution.check_balanced_parenthesis(s))


if __name__ == "__main__":
    main()
