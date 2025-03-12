"""
Given a sorted array arr[] of size n, the goal is to rearrange the array so that all distinct elements appear at the beginning in sorted order. Additionally, return the length of this distinct sorted subarray.

Note: The elements after the distinct ones can be in any order and hold any value, as they don’t affect the result.

Examples:

    Input: arr[] = [2, 2, 2, 2, 2]
    Output: [2]
    Explanation: All the elements are 2, So only keep one instance of 2.

    Input: arr[] = [1, 2, 2, 3, 4, 4, 4, 5, 5]
    Output: [1, 2, 3, 4, 5]

    Input: arr[] = [1, 2, 3]
    Output: [1, 2, 3]
    Explanation : No change as all elements are distinct.

"""


class Solution:
    def removeDuplicate(self, sortedArr):
        n = len(sortedArr)
        if n == 1:
            return sortedArr

        ref = 0
        for i in range(1, n):
            if sortedArr[i] > sortedArr[i - 1]:
                ref += 1
                sortedArr[ref] = sortedArr[i]

        return sortedArr[: ref + 1]
    
def main():
    solution = Solution()
    sortedArr = [int(value) for value in input().strip().split()]
    print(solution.removeDuplicate(sortedArr))

if __name__ == "__main__":
    main()