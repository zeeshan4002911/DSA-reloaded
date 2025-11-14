"""
You are given two numbers n and p. You need to find np.

Examples:

Input: n = 9, p = 9
Output: 387420489
Explanation: 387420489 is the value obtained when 9 is raised to the power of 9.

Input: n = 2, p = 9
Output: 512
Explanation: 512 is the value obtained when 2 is raised to the power of 9.

Constraints:
1 ≤ n ≤ 10
0 ≤  p ≤ 9

Expected Complexities
Time Complexity: O(p)
Auxiliary Space: O(p)
"""


class Solution:
    def power_using_recursion(self, n, p,  res=1):
        if p <= 0:
            return 1
        if p <= 1:
            # To include the p = 1, in result
            res = res * n
            return res
        
        return self.power_using_recursion(n, p - 1, res * n)


def main():
    n = int(input("Enter the number: "))
    p = int(input("Enter the power: "))

    soln = Solution()
    print(soln.power_using_recursion(n, p))


if __name__ == "__main__":
    main()
