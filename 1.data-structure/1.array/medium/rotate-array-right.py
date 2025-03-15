"""
Given an array of integers arr[] of size n, the task is to rotate the array elements to the left by d positions.

Examples:

    Input: arr[] = {1, 2, 3, 4, 5, 6}, d = 2
    Output: {5, 6, 1, 2, 3, 4}
    Explanation: After first left rotation, arr[] becomes {2, 3, 4, 5, 6, 1} and after the second rotation, arr[] becomes {3, 4, 5, 6, 1, 2}

    Input: arr[] = {1, 2, 3}, d = 4
    Output: {3, 1, 2}
"""

from math import gcd


class Solution:
    # Juggling Algorithm
    def rotate_clockwise_juggling(self, arr, d):
        n = len(arr)
        d %= n
        cycles = gcd(d, n)

        for i in range(cycles):
            j = i
            currEle = arr[j]
            while True:
                k = (j + d) % n
                nextEle = arr[k]
                arr[k] = currEle
                currEle = nextEle
                j = k
                if j == i:
                    break
        return arr

    # By rotation
    def rotate_clockwise_reverse(self, arr, d):
        n = len(arr)
        d %= n
        arr.reverse()

        arr[0:d] = reversed(arr[:d])
        arr[d:n] = reversed(arr[d:])
        return arr


def main():
    solution = Solution()
    arr = [int(value) for value in input().strip().split()]
    print("Enter right rotation position value:", end=" ")
    d = int(input())
    print(solution.rotate_clockwise_juggling(arr, d))


if __name__ == "__main__":
    main()
