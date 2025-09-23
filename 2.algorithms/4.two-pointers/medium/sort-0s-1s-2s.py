"""
Given an array arr[] containing only 0s, 1s, and 2s. Sort the array in ascending order.

You need to solve this problem without utilizing the built-in sort function.

Examples:

Input: arr[] = [0, 1, 2, 0, 1, 2]
Output: [0, 0, 1, 1, 2, 2]
Explanation: 0s 1s and 2s are segregated into ascending order.

Input: arr[] = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
Output: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]
Explanation: 0s 1s and 2s are segregated into ascending order.

Follow up: Could you come up with a one-pass algorithm using only constant extra space?

Constraints:
1 <= arr.size() <= 10^6
0 <= arr[i] <= 2
Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)
"""


class Solution:
    def sort012(self, arr):
        # Three pointers sort cum partition, on itterate of middle pointer
        ptr_0s, ptr_1s, ptr_2s = 0, 0, len(arr) - 1
        # Dutch National Flag Algorithm
        while ptr_1s <= ptr_2s:
            if arr[ptr_1s] == 0:
                arr[ptr_0s], arr[ptr_1s] = arr[ptr_1s], arr[ptr_0s]
                ptr_0s += 1
                ptr_1s += 1
            elif arr[ptr_1s] == 2:
                arr[ptr_2s], arr[ptr_1s] = arr[ptr_1s], arr[ptr_2s]
                ptr_2s -= 1
            elif arr[ptr_1s] == 1:
                ptr_1s += 1
        return arr


def main():
    arr = list(map(int, input().strip().split()))
    solution = Solution()
    print(solution.sort012(arr))


if __name__ == "__main__":
    main()
