"""
Given an array arr[], the task is to find the top three largest distinct integers present in the array.

Note: If there are less than three distinct elements in the array, then return the available distinct numbers in descending order.

Examples :

    Input: arr[] = [10, 4, 3, 50, 23, 90]
    Output: [90, 50, 23]

    Input: arr[] = [10, 9, 9]
    Output: [10, 9]
    There are only two distinct elements

    Input: arr[] = [10, 10, 10]
    Output: [10]
    There is only one distinct element
"""


class Solution:
    def getSecondLargestElement(self, arr):
        firstMaxValue = -1
        secondMaxValue = -1
        thirdMaxValue = -1
        for ele in arr:
            if ele > firstMaxValue:
                thirdMaxValue = secondMaxValue
                secondMaxValue = firstMaxValue
                firstMaxValue = ele
            elif ele > secondMaxValue and ele < firstMaxValue:
                thirdMaxValue = secondMaxValue
                secondMaxValue = ele
            elif ele > thirdMaxValue and ele < secondMaxValue:
                thirdMaxValue = ele
        result = []
        if firstMaxValue != -1: result.append(firstMaxValue)
        if secondMaxValue != -1: result.append(secondMaxValue)
        if thirdMaxValue != -1: result.append(thirdMaxValue)
        return result


def main():
    t = int(input())
    while t > 0:
        arr = [int(value) for value in input().strip().split()]
        solution = Solution()
        print(solution.getSecondLargestElement(arr))
        t -= 1


if __name__ == "__main__":
    main()
