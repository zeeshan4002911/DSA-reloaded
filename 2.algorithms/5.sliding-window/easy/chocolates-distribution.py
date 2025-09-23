"""
Given an array arr[] of positive integers, where each value represents the number of chocolates in a packet. Each packet can have a variable number of chocolates. There are m students, the task is to distribute chocolate packets among m students such that -
      i. Each student gets exactly one packet.
     ii. The difference between maximum number of chocolates given to a student and minimum number of chocolates given to a student is minimum and return that minimum possible difference.

Examples:

Input: arr = [3, 4, 1, 9, 56, 7, 9, 12], m = 5
Output: 6
Explanation: The minimum difference between maximum chocolates and minimum chocolates is 9 - 3 = 6 by choosing following m packets :[3, 4, 9, 7, 9].

Input: arr = [7, 3, 2, 4, 9, 12, 56], m = 3
Output: 2
Explanation: The minimum difference between maximum chocolates and minimum chocolates is 4 - 2 = 2 by choosing following m packets :[3, 2, 4].

Input: arr = [3, 4, 1, 9, 56], m = 5
Output: 55
Explanation: With 5 packets for 5 students, each student will receive one packet, so the difference is 56 - 1 = 55.

Constraints:
1 ≤ m <= arr.size ≤ 10^5
1 ≤ arr[i] ≤ 10^9

Expected Complexities
Time Complexity: O(n log n)
Auxiliary Space: O(1)
"""

from typing import List


class Solution:
    def chocolates_distribution(self, arr: List, m: int) -> int:
        # Sort to get minimum difference between packets
        arr.sort()
        size = len(arr)
        result = -1
        if 0 < m <= size:
            result = arr[m - 1] - arr[0]
        # Sliding window of m size and calculating difference in chocolates distribution by max - min
        for i in range(m, size):
            diff = arr[i] - arr[i - (m - 1)]
            result = min(result, diff)
        return result


def main():
    arr = [int(value) for value in input().strip().split()]
    print("Enter number of Students (m):", end=" ")
    m = int(input())
    solution = Solution()
    print(solution.chocolates_distribution(arr, m))


if __name__ == "__main__":
    main()
