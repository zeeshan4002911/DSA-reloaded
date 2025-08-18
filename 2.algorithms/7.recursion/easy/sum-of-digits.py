"""
Given a number, we need to find sum of its digits using recursion.

Examples: 

    Input: 12345
    Output: 15
    Explanation: Sum of digits → 1 + 2 + 3 + 4 + 5 = 15

    Input: 45632
    Output: 20
"""


class Solution:
    def sum_of_digits(self, n):
        return self.sum_rec_helper(n, 0)

    def sum_rec_helper(self, n, result):
        if n == 0:
            return result

        result += (n % 10)
        n //= 10
        return self.sum_rec_helper(n, result)


def main():
    while True:
        n = input("Enter a number: ").strip()
        try:
            n = int(n)
            break
        except ValueError:
            print("Invalid input. Please enter a valid", int.__name__)

    solution = Solution()
    print(solution.sum_of_digits(n))


if __name__ == "__main__":
    main()
