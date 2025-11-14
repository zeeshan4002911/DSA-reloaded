"""
Siddhant made a special series and named it as G.F Series. The series follows this trend  Tn=(Tn-2)2-(Tn-1)  in which the first and the second term are 0 and 1 respectively. Help Siddhant to find the first n terms of the series.

Note: Print a white space (" ") after every integer and a newline character after every testcase.

Examples

Input: n = 3
Output: 0 1 -1
Explanation: First-term is given as 0 and the second term is 1. So the T3 = (T_3-2)^2 - (T_3-1) = T12 - T2 = 02 - 1 = -1

Input: n = 6
Output: 0 1 -1 2 -1 5
Explanation:
T1 : 0
T2 : 1
T3 : -1
T4 = (1)2 - (-1) = 2
T5 = (-1)2 - (2) = 1 - 2 = -1
T6 = (2)2 - (-1) = 4 + 1 = 5

Your Task:
You don't need to read input. Your task is to complete the function gfSeries() which takes an integer n as an input parameter and print first n term of the series.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)

Constraints:
2 <= n <= 15
"""


class Solution:
    def df_series(self, n):
        print("0 1", end=" ")
        
        # Starting with 2 characters as 0 and 1 is already printed
        self.df_series_helper(n, 2, 0, 1)
        print()
    
    def df_series_helper(self, n, i, t1, t2):
        if i >= n:
            return
        
        t3 = (t1) ** 2 - t2
        print(t3, end=" ")
        
        # Moving the pointers for next level calculation
        self.df_series_helper(n, i + 1, t2, t3)


def main():
    n = int(input("Enter a number: "))
    soln = Solution()
    soln.df_series(n)


if __name__ == "__main__":
    main()
