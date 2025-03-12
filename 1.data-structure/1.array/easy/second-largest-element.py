"""
Given an array of positive integers arr[] of size n, the task is to find second largest distinct element in the array.

Note: If the second largest element does not exist, return -1.

Examples:

    Input: arr[] = [12, 35, 1, 10, 34, 1]
    Output: 34
    Explanation: The largest element of the array is 35 and the second largest element is 34.

    Input: arr[] = [10, 5, 10]
    Output: 5
    Explanation: The largest element of the array is 10 and the second largest element is 5.

    Input: arr[] = [10, 10, 10]
    Output: -1
    Explanation: The largest element of the array is 10 there is no second largest element.

"""


class Solution:
    def getSecondLargestElement(self, arr):
        firstMaxValue = -1
        secondMaxValue = -1
        for ele in arr:
            if ele > firstMaxValue:
                secondMaxValue = firstMaxValue
                firstMaxValue = ele
            elif ele > secondMaxValue and ele < firstMaxValue:
                secondMaxValue = ele
        return secondMaxValue


def main():
    t = int(input())
    while t > 0:
        arr = [int(value) for value in input().strip().split()]
        solution = Solution()
        print(solution.getSecondLargestElement(arr))
        t -= 1


if __name__ == "__main__":
    main()
