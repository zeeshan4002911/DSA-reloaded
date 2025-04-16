"""
Given an unsorted array arr of positive integers of size n. One number a from the set [1, 2,....,n] is missing and one number b occurs twice in the array. Find numbers a and b.

Note: The test cases are generated such that there always exists one missing and one repeating number within the range [1,n].

Examples:

Input: arr[] = [2, 2]
Output: [2, 1]
Explanation: Repeating number is 2 and smallest positive missing number is 1.

Input: arr[] = [1, 3, 3]
Output: [3, 2]
Explanation: Repeating number is 3 and smallest positive missing number is 2.

Input: arr[] = [4, 3, 6, 2, 1, 1]
Output: [1, 5]
Explanation: Repeating number is 1 and the missing number is 5.

Constraints:
2 ≤ arr.size() ≤ 106
1 ≤ arr[i] ≤ arr.size()
"""


class Solution:
    def missing_and_repeating(self, arr):
        actual_sum = sum(arr)
        actual_square_sum = sum([(val**2) for val in arr])

        n = len(arr)
        natural_sum = (n * (n + 1)) // 2
        natural_square_sum = (n * (n + 1) * (2 * n + 1)) // 6
        
        """
        # Solving for value of missing and repeating number by forming two mathematical equation
        x = repeating_num, y = missing_num
        x - y = actual_sum - natural_sum #---------(1)
        x ** 2 - y ** 2 = actual_square_sum - natural_square_sum
        (x + y)(x - y) = actual_square_sum - natural_square_sum #---------(2)
        
        # Division of equation 2 by 1
        x + y = (actual_square_sum - natural_square_sum) // (actual_sum - natural_sum)
        
        # Substitution of x value in equation 2
        (actual_sum - natural_sum + y) + y = (actual_square_sum - natural_square_sum) // (actual_sum - natural_sum)
        y = (((actual_square_sum - natural_square_sum) // (actual_sum - natural_sum)) + natural_sum - actual_sum) // 2
        
        # Replacing y value in equation 1 or 2 to get x value
        x = (actual_sum - natural_sum) + (((actual_square_sum - natural_square_sum) // (actual_sum - natural_sum)) + natural_sum - actual_sum) // 2
        """
        repeating_num = (actual_sum - natural_sum) + (
            ((actual_square_sum - natural_square_sum) // (actual_sum - natural_sum))
            + natural_sum
            - actual_sum
        ) // 2
        missing_num = (
            ((actual_square_sum - natural_square_sum) // (actual_sum - natural_sum))
            + natural_sum
            - actual_sum
        ) // 2
        return [repeating_num, missing_num]


def main():
    arr = [int(value) for value in input().strip().split()]
    solution = Solution()
    print(solution.missing_and_repeating(arr))


if __name__ == "__main__":
    main()
