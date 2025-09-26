"""
Given a positive integer n, determine whether it is odd or even. Return true if the number is even and false if the number is odd.

Examples:

Input: n = 15
Output: false
Explanation: The number is not divisible by 2, Odd number.

Input: n = 44
Output: true
Explanation: The number is divisible by 2, Even number.

Constraints:
1 ≤ n ≤ 10^4

Expected Complexities
Time Complexity: O(1)
Auxiliary Space: O(1)
"""


class Solution:
    def check_even_odd(self, num):
        return num % 2 == 0

def main():
    num = int(input("Enter the number: ").strip())
    solution = Solution()
    print(solution.check_even_odd(num))


if __name__ == "__main__":
    main()
