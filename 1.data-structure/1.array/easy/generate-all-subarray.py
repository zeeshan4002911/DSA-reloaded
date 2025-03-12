"""
Given an array arr[], the task is to generate all the possible subarrays of the given array.

Examples:

    Input: arr[] = [1, 2, 3]
    Output: [ [1], [1, 2], [2], [1, 2, 3], [2, 3], [3] ]

    Input: arr[] = [1, 2]
    Output: [ [1], [1, 2], [2] ]

Constraints:
1 <= arr.size() <= 103
1 <= arr[i] <= 106
"""


class Solution:
    def generateSubArr(self, arr):
        n = len(arr)
        result = []
        for i in range(n):
            for j in range(i, n):
                result.append(arr[i : (j + 1)])
        return result


def main():
    solution = Solution()
    arr = [int(value) for value in input().strip().split()]
    print(solution.generateSubArr(arr))


if __name__ == "__main__":
    main()
