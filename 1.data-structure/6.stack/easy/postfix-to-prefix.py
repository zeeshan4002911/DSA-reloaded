"""
You are given a string that represents the postfix form of a valid mathematical expression. Convert it to its prefix form.

Example 1:

Input:
ABC/-AK/L-*
Output:
*-A/BC-/AKL
Explanation:
The above output is its valid prefix form.

Example 2:

Input:
ab+
Output:
+ab
Explanation:
The above output is its valid prefix form.

Your Task:

Complete the function string postToPre(string post_exp), which takes a postfix string as input and returns its prefix form.

Expected Time Complexity: O(post_exp.length()).

Expected Auxiliary Space: O(post_exp.length()).

Constraints:

3<=post_exp.length()<=16000
"""


class Solution:
    def postfix_to_prefix(self, post_exp):
        size = len(post_exp)
        st = []

        for i in range(size):
            # Adding operand into the stack without any change
            if str(post_exp[i]).isalnum():
                st.append(post_exp[i])
            # For operator, generating the prefix form using last two operand of stack
            else:
                operand1 = st.pop()
                operand2 = st.pop()
                ele = post_exp[i] + str(operand2) + str(operand1)
                # Adding the postfix expression back to stack for chain equation
                st.append(ele)

        # Single element will remain on stack for valid postfix expression input
        return st.pop()


def main():
    s = input("Enter postfix expression: ").strip()
    solution = Solution()
    print(solution.postfix_to_prefix(s))


if __name__ == "__main__":
    main()
