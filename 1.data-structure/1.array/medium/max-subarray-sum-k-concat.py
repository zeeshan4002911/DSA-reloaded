"""
Given an array and a number k, find the largest sum of contiguous array in the modified array which is formed by repeating the given array k times.

Examples :

    Input  : arr[] = {-1, 10, 20}, k = 2
    Output : 59
    After concatenating array twice, we get {-1, 10, 20, -1, 10, 20} which has maximum subarray sum as 59.

    Input  : arr[] = {-1, -2, -3}, k = 3
    Output : -1

"""


class Solution:
    def maximum_subarray_sum(self, arr, k):
        """
        Iterate on same array k times and use modular arithmetic to move back beginning after end of array.
        TC: O(n*k)
        SC: O(1)
        """
        max_current = arr[0]
        max_global = arr[0]
        size = len(arr)
        size_of_k_arr = size * k
        for i in range(1, size_of_k_arr):
            current_ele = arr[i % size]
            max_current = max(max_current + current_ele, current_ele)
            max_global = max(max_global, max_current)
        return max_global


def main():
    arr = [int(value) for value in input().strip().split()]
    print("Enter value of k:", end=" ")
    k = int(input())
    solution = Solution()
    print(solution.maximum_subarray_sum(arr, k))


if __name__ == "__main__":
    main()
