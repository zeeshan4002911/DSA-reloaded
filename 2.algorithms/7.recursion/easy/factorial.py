"""
Given a positive integer, n. Find the factorial of n.

Examples :

Input: n = 5
Output: 120
Explanation: 1 x 2 x 3 x 4 x 5 = 120

Input: n = 4
Output: 24
Explanation: 1 x 2 x 3 x 4 = 24

Constraints:
0 ≤ n ≤ 12

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)
"""


class Solution:
    def factorial(self, n):
        if n == 1 or n == 0:
            return 1

        return n * self.factorial(n - 1)

    # Tail recursion for better recursive stack management - TCO (Tail call optimization)
    # Not supported in python
    def factorial_tail_recursion(self, n):
        return self.factorial_rec_helper(n, 1)

    def factorial_rec_helper(self, n, result):
        if n == 1 or n == 0:
            return result
        
        result *= n
        return self.factorial_rec_helper(n - 1, result)


def main():
    while True:
        n = input("Enter a number: ").strip()
        try:
            n = int(n)
            break
        except ValueError:
            print("Invalid input. Please enter a valid", int.__name__)

    solution = Solution()
    print(solution.factorial_tail_recursion(n))


if __name__ == "__main__":
    main()
