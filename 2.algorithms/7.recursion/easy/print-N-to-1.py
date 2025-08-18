"""
Print numbers from N to 1 (space separated) without the help of loops.

Example 1:

Input:
N = 10
Output: 10 9 8 7 6 5 4 3 2 1

Your Task:
This is a function problem. You only need to complete the function printNos() that takes N as parameter and prints number from N to 1 recursively. Don't print newline, it will be added by the driver code.


Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N) (Recursive).

Constraint
1<=n<=1000
"""


class Solution:
    def print_N_to_1(self, n):
        self.print_N_to_1_helper(n, n)

    def print_N_to_1_helper(self, n, i):
        if i < 1:
            return

        print(i, end=" ")
        return self.print_N_to_1_helper(n, i - 1)


def main():
    while True:
        n = input("Enter a number: ").strip()
        try:
            n = int(n)
            break
        except ValueError:
            print("Invalid input. Please enter a valid", int.__name__)

    solution = Solution()
    solution.print_N_to_1(n)


if __name__ == "__main__":
    main()
