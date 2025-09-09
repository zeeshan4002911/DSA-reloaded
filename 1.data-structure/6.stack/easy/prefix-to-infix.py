"""
You are given a string S of size N that represents the prefix form of a valid mathematical expression. The string S contains only lowercase and uppercase alphabets as operands and the operators are +, -, *, /, %, and ^.Convert it to its infix form.

Example 1:

Input:
*-A/BC-/AKL
Output:
((A-(B/C))*((A/K)-L))
Explanation:
The above output is its valid infix form.

Your Task:

Your task is to complete the function string preToInfix(string pre_exp), which takes a prefix string as input and return its infix form.

Expected Time Complexity: O(N).

Expected Auxiliary Space: O(N).

Constraints:

3<=|S|<=10^4
"""


class Solution:
    def prefix_to_infix(self, pre_exp):
        size = len(pre_exp)
        st = []

        for i in range(size - 1, -1, -1):
            # Adding operand into the stack without any change
            if str(pre_exp[i]).isalnum():
                st.append(pre_exp[i])
            # For operator, generating the infix form using last two operand of stack
            else:
                operand1 = st.pop()
                operand2 = st.pop()
                ele = "(" + str(operand1) + pre_exp[i] + str(operand2) + ")"
                # Adding the infix expression back to stack for chain equation
                st.append(ele)
        
        # Single element will remain on stack for valid prefix to infix expression
        return st.pop()


def main():
    s = input("Enter prefix expression: ").strip()
    solution = Solution()
    print(solution.prefix_to_infix(s))


if __name__ == "__main__":
    main()
