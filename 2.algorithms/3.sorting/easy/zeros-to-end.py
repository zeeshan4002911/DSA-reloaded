"""
You are given an array arr[] of non-negative integers.
Your task is to move all the zeros in the array to the right end while maintaining the relative order of the non-zero elements.
The operation must be performed in place, meaning you should not use extra space for another array.

Examples:
    Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
    Output: [1, 2, 4, 3, 5, 0, 0, 0]
    Explanation: There are three 0s that are moved to the end.

    Input: arr[] = [10, 20, 30]
    Output: [10, 20, 30]
    Explanation: No change in array as there are no 0s.

    Input: arr[] = [0, 0]
    Output: [0, 0]
    Explanation: No change in array as there are all 0s.

Constraints:
    1 ≤ arr.size() ≤ 105
    0 ≤ arr[i] ≤ 105
"""


class Solution:
    def zeros_to_end(self, arr):
        n = len(arr)
        curr = 0
        for i in range(n):
            if arr[i] != 0:
                arr[curr] = arr[i]
                curr += 1
        while curr < n:
            arr[curr] = 0
            curr += 1
        return arr
    
    # Uses swap to push zeros to right
    def zeros_to_end_swap(self, arr):
        n = len(arr)
        curr = 0
        for i in range(n):
            if arr[i] != 0:
                arr[i], arr[curr] = arr[curr], arr[i]
                curr += 1
        return arr

def main():
    arr = [int(value) for value in input().strip().split()]
    solution = Solution()
    print(solution.zeros_to_end(arr))

if __name__ == "__main__":
    main()
