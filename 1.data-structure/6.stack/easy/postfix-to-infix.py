"""
You are given a string that represents the postfix form of a valid mathematical expression. Convert it to its infix form.

Example:

Input:
ab*c+
Output:
((a*b)+c)
Explanation:
The above output is its valid infix form.

Your Task:

Complete the function string postToInfix(string post_exp), which takes a postfix string as input and returns its infix form.



Expected Time Complexity: O(N).

Expected Auxiliary Space: O(N).

Constraints:

3<=post_exp.length()<=10^4

"""


class Solution:
    def postfix_to_infix(self, pos_exp):
        size = len(pos_exp)
        st = []

        for i in range(size):
            # Adding operand into the stack without any change
            if str(pos_exp[i]).isalnum():
                st.append(pos_exp[i])
            # For operator, generating the infix form using last two operand of stack
            else:
                operand1 = st.pop()
                operand2 = st.pop()
                ele = "(" + str(operand2) + pos_exp[i] + str(operand1) + ")"
                # Adding the infix expression back to stack for chain equation
                st.append(ele)

        # Single element will remain on stack for valid postfix expression input
        return st.pop()


def main():
    s = input("Enter postfix expression: ").strip()
    solution = Solution()
    print(solution.postfix_to_infix(s))


if __name__ == "__main__":
    main()
