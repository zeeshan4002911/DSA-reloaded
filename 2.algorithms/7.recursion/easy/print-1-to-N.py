"""
Given an positive integer n, print numbers from 1 to n without using loops.

Implement the function printTillN() to print the numbers from 1 to n as space-separated integers.

Examples

Input: n = 5
Output: 1 2 3 4 5
Explanation: We have to print numbers from 1 to 5.

Input: n = 10
Output: 1 2 3 4 5 6 7 8 9 10
Explanation: We have to print numbers from 1 to 10.

Constraints:
1 ≤ n ≤ 1000

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(n)
"""


class Solution:
    def print_1_to_N(self, n):
        self.print_1_to_N_helper(n, 1)

    def print_1_to_N_helper(self, n, i):
        if i > n:
            return

        print(i, end=" ")
        return self.print_1_to_N_helper(n, i + 1)


def main():
    while True:
        n = input("Enter a number: ").strip()
        try:
            n = int(n)
            break
        except ValueError:
            print("Invalid input. Please enter a valid", int.__name__)

    solution = Solution()
    solution.print_1_to_N(n)


if __name__ == "__main__":
    main()
