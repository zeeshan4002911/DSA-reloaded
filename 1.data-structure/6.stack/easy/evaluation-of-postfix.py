"""
You are given an array of strings arr[] that represents a valid arithmetic expression written in Reverse Polish Notation (Postfix Notation). Your task is to evaluate the expression and return an integer representing its value.

Key Details:

    The valid operators are '+', '-', '*', and '/'.
    Each operand is guaranteed to be a valid integer or another expression.
    The division operation between two integers always rounds the result towards zero, discarding any fractional part.
    No division by zero will occur in the input.
    The input is a valid arithmetic expression in Reverse Polish Notation.
    The result of the expression and all intermediate calculations will fit in a 32-bit signed integer.

Examples:

Input: arr[] = ["2", "3", "1", "*", "+", "9", "-"]
Output: -4
Explanation: If the expression is converted into an infix expression, it will be 2 + (3 * 1) – 9 = 5 – 9 = -4.

Input: arr[] = ["100", "200", "+", "2", "/", "5", "*", "7", "+"]
Output: 757
Explanation: If the expression is converted into an infix expression, it will be ((100 + 200) / 2) * 5 + 7  = 150 * 5 + 7 = 757.

Constraints:
1 ≤ arr.size() ≤ 10^5
arr[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-10^4, 10^4]

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(n)
"""

import math


class Solution:
    def evaluate(self, arr):
        # Postfix to Infix Conversion Algortihm
        size = len(arr)
        st = []

        # Iterating from the left side as operand is before operator from left to right
        for i in range(size):
            # Adding to stack for each integers
            if str(arr[i]).lstrip("-").isdigit():
                st.append(arr[i])
            
            # For Operator, popping out last two operand and evaluating the result using operator
            elif arr[i] in ["+", "-", "*", "/"]:
                operand1 = st.pop()
                operand2 = st.pop()
                operand1, operand2 = int(operand1), int(operand2)

                if arr[i] == "+":
                    eval_exp = operand2 + operand1
                elif arr[i] == "-":
                    eval_exp = operand2 - operand1
                elif arr[i] == "*":
                    eval_exp = operand2 * operand1
                else:
                    # Truncating to get near to zero as divison result, math.floor near to negative infinity
                    eval_exp = math.trunc(operand2 / operand1)

                # Pushing the evaluated result back to stack
                st.append(eval_exp)

        # Stack will have one element post evaluation
        return st.pop()


def main():
    arr = input("Enter space separated expression: ").strip().split()
    solution = Solution()
    print(solution.evaluate(arr))


if __name__ == "__main__":
    main()
