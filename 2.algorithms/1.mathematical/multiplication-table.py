"""
Create the multiplication table from 1 to 10 for a given number n and return the table as an array.

Examples:

Input: n = 9
Output: 9 18 27 36 45 54 63 72 81 90

Input: n = 2
Output: 2 4 6 8 10 12 14 16 18 20

Constraints:
1 <= N <= 10^6

Expected Complexities
Time Complexity: O(1)
Auxiliary Space: O(1)
"""


class Solution:
    def print_multiplication_table(self, num):
        result = []
        for factor in range(1, 11):
            result.append(factor * num)
        return result

    def pretty_print(self, num):
        for factor in range(1, 11):
            print(f"{num} x {factor} = {factor * num}")


def main():
    num = int(input("Enter the table number: ").strip())
    solution = Solution()
    print(solution.print_multiplication_table(num))
    solution.pretty_print(num)


if __name__ == "__main__":
    main()
