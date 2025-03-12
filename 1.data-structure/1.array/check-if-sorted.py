"""
Given an array of size n, the task is to check if it is sorted in ascending order or not. Equal values are allowed in an array and two consecutive equal values are considered sorted.

Examples:

    Input: arr[] = [20, 21, 45, 89, 89, 90]
    Output: Yes

    Input: arr[] = [20, 20, 45, 89, 89, 90]
    Output: Yes

    Input: arr[] = [20, 20, 78, 98, 99, 97]
    Output: No
"""


class Solution:
    def checkSort(self, arr) -> bool:
        n = len(arr)
        if n == 1 or n == 0:
            return True

        for i in range(1, n):
            if arr[i] < arr[i - 1]: return False
        return True
    
def main():
    solution = Solution()
    arr = [int(value) for value in input().strip().split()]
    result = solution.checkSort(arr)
    print(result)

if __name__ == "__main__":
    main()