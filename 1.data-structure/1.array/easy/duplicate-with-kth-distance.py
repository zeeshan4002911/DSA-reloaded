"""
Given an unsorted array arr and a number k which is smaller than the size of the array. Return true if the array contains any duplicate within k distance throughout the array else false.

Examples:

Input: arr[] = [1, 2, 3, 4, 1, 2, 3, 4], k = 3
Output: false
Explanation: All duplicates are more than k distance away.

Input: arr[] = [1, 2, 3, 1, 4, 5], k = 3
Output: true
Explanation: 1 is repeated at distance 3.

Input: arr[] = [6, 8, 4, 1, 8, 5, 7], k = 3
Output: true
Explanation: 8 is repeated at distance 3.

Constraints:
1 ≤ arr.size() ≤ 106
1 ≤ k < arr.size()
1 ≤ arr[i] ≤ 105
"""


class Solution:
    def duplicate_with_kth_distance(self, arr, k):
        size = len(arr)
        seen = set()
        # Sliding Window having window length k + 1
        for i in range(k + 1):
            if arr[i] in seen:
                return True
            seen.add(arr[i])
        for i in range(k + 1, size):
            seen.remove(arr[i - (k + 1)])
            if arr[i] in seen:
                return True
            seen.add(arr[i])
        return False


def main():
    arr = [int(value) for value in input().strip().split()]
    print("Enter value of k:", end=" ")
    k = int(input())
    solution = Solution()
    print(solution.duplicate_with_kth_distance(arr, k))


if __name__ == "__main__":
    main()
