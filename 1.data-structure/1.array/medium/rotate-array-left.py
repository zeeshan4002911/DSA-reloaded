"""
Given an array arr[]. Rotate the array to the left (counter-clockwise direction) by d steps, where d is a positive integer. Do the mentioned change in the array in place.

Note: Consider the array as circular.

Examples:

    Input: arr[] = [1, 2, 3, 4, 5], d = 2
    Output: [3, 4, 5, 1, 2]
    Explanation: when rotated by 2 elements, it becomes 3 4 5 1 2.

    Input: arr[] = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], d = 3
    Output: [8, 10, 12, 14, 16, 18, 20, 2, 4, 6]
    Explanation: when rotated by 3 elements, it becomes 8 10 12 14 16 18 20 2 4 6.

    Input: arr[] = [7, 3, 9, 1], d = 9
    Output: [3, 9, 1, 7]
    Explanation: when we rotate 9 times, we'll get 3 9 1 7 as resultant array.

Constraints:
    1 <= arr.size(), d <= 105
    0 <= arr[i] <= 105
"""

from math import gcd


class Solution:
    # Juggling Algorithm
    def rotate_counter_clockwise_juggling(self, arr, d):
        n = len(arr)
        d %= n
        cycles = gcd(d, n)

        for i in range(cycles):
            j = i
            currEle = arr[j]
            while True:
                k = (j - d) % n
                nextEle = arr[k]
                arr[k] = currEle
                currEle = nextEle
                j = k
                if j == i:
                    break
        return arr

    # By rotation
    def rotate_counter_clockwise_reverse(self, arr, d):
        n = len(arr)
        d %= n
        arr.reverse()

        arr[n - d : n] = reversed(arr[n - d : n])
        arr[: n - d] = reversed(arr[: n - d])
        return arr


def main():
    solution = Solution()
    arr = [int(value) for value in input().strip().split()]
    print("Enter left rotation position value:", end=" ")
    d = int(input())
    print(solution.rotate_counter_clockwise_juggling(arr, d))


if __name__ == "__main__":
    main()
