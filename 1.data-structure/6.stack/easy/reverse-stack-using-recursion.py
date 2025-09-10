"""
You are given a stack St. You have to reverse the stack using recursion.

Example 1:

Input: St = [3,2,1,7,6]
Output: [6,7,1,2,3]
Explanation: Input stack after reversing will look like the stack in the output.

Example 2:

Input: St = [4,3,9,6]
Output: [6,9,3,4]
Explanation: Input stack after reversing will look like the stack in the output.

Constraints:
1 ≤ stack.size ≤ 10^4
0 ≤ stack.element ≤ 10^3

Expected Complexities
Time Complexity: O(n^2)
Auxiliary Space: O(n)
"""


class Solution:
    def reverse_stack(self, st):
        return self.reverse_stack_rec(st, [])

    def reverse_stack_rec(self, st, result):
        if not st:
            return result

        top = st.pop()
        result.append(top)
        return self.reverse_stack_rec(st, result)


def main():
    st = input("Enter the stack: ").strip().split()
    solution = Solution()
    print(solution.reverse_stack(st))


if __name__ == "__main__":
    main()
