"""
Given an array arr consisting of only 0's and 1's in random order. Modify the array in-place to segregate 0s onto the left side and 1s onto the right side of the array.

Examples :

Input: arr[] = [0, 0, 1, 1, 0]
Output: [0, 0, 0, 1, 1]
Explanation:  After segregation, all the 0's are on the left and 1's are on the right. Modified array will be [0, 0, 0, 1, 1].

Input: arr[] = [1, 1, 1, 1]
Output: [1, 1, 1, 1]
Explanation: There are no 0s in the given array, so the modified array is [1, 1, 1, 1]

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ arr.size() ≤ 106
0 ≤ arr[i] ≤ 1
"""


class Solution:
    def segregate_0s_and_1s(self, arr):
        size = len(arr)
        i = 0
        j = size - 1
        while i < j:
            while arr[i] == 0 and i < size - 1:
                i += 1

            while arr[j] == 1 and j > 0:
                j -= 1

            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

        return arr


def main():
    arr = [int(value) for value in input().strip().split()]
    solution = Solution()
    print(solution.segregate_0s_and_1s(arr))


if __name__ == "__main__":
    main()
