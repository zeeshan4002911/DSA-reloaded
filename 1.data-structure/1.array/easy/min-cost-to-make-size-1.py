"""
Given an array, arr[]. You need to reduce size of array to one. You are allowed to select a pair of integers and remove the larger one of these two. This decreases the array size by 1. Cost of this operation is equal to value of smaller one. Find out minimum sum of costs of operations needed to convert the array into a single element.

Examples:

Input: arr[] = [4, 3, 2]
Output: 4
Explanation: Choose (4, 2) so 4 is removed, new array = {2, 3}. Now choose (2, 3) so 3 is removed. So total cost = 2 + 2 = 4

Input: arr[] = [3, 4]
Output: 3
Explanation: Choose 3, 4, so cost is 3.

Input: arr[] = [1]
Output: 0
Explanation: The array is already of size one, so no operations are needed.

Constraints:
1 <= arr.size() <= 105
1 <= arr[i] <= 104
"""


class Solution:
    def cost_of_operation(self, arr):
        """
        Greedy Approach: Always choose the minimum and current maximum pair to remove,
        operation cost will be minimum in each choice
        """
        min_element = min(arr)
        return (len(arr) - 1) * min_element


def main():
    arr = [int(value) for value in input().strip().split()]
    print(Solution().cost_of_operation(arr))


if __name__ == "__main__":
    main()
