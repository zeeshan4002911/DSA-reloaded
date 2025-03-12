"""
    Input: arr[] = [10, 20, 4]
    Output: 20
    Explanation: Among 10, 20 and 4, 20 is the largest. 

    Input: arr[] = [20, 10, 20, 4, 100]
    Output: 100

"""
import math

class Solution:
    def getMax(self, arr):
        maxValue = -math.inf
        for ele in arr:
            if ele > maxValue: maxValue = ele
        return maxValue

def main():
    t = int(input())
    while (t > 0):
        arr = [int(value) for value in input().strip().split()]
        solution = Solution()
        print(solution.getMax(arr))
        t -= 1


if __name__ == "__main__":
    main()
