"""
You are given a string that represents the prefix form of a valid mathematical expression. Convert it to its postfix form.

Example:

Input:
*-A/BC-/AKL
Output:
ABC/-AK/L-*
Explanation:
The above output is its valid postfix form.

Your Task:

Complete the function preToPost(string pre_exp), which takes a prefix string as input and returns its postfix form.



Expected Time Complexity: O(N).

Expected Auxiliary Space: O(N).

Constraints:

3<=pre_exp.length()<=100
"""


class Solution:
    def prefix_to_postfix(self, pre_exp):
        size = len(pre_exp)
        st = []

        for i in range(size - 1, -1, -1):
            # Adding operand into the stack without any change
            if str(pre_exp[i]).isalnum():
                st.append(pre_exp[i])
            # For operator, generating the postfix form using last two operand of stack
            else:
                operand1 = st.pop()
                operand2 = st.pop()
                ele = str(operand1) + str(operand2) + pre_exp[i]
                # Adding the postfix expression back to stack for chain equation
                st.append(ele)
        
        # Single element will remain on stack for valid prefix to postfix expression
        return st.pop()


def main():
    s = input("Enter prefix expression: ").strip()
    solution = Solution()
    print(solution.prefix_to_postfix(s))


if __name__ == "__main__":
    main()
