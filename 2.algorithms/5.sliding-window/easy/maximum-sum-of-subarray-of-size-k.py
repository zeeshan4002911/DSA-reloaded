"""
Given an array of integers arr[]  and a number k. Return the maximum sum of a subarray of size k.

Note: A subarray is a contiguous part of any given array.

Examples:

Input: arr[] = [100, 200, 300, 400] , k = 2
Output: 700
Explanation: arr3  + arr4 = 700, which is maximum.

Input: arr[] = [100, 200, 300, 400] , k = 4
Output: 1000
Explanation: arr1 + arr2 + arr3 + arr4 = 1000, which is maximum.

Input: arr[] = [100, 200, 300, 400] , k = 1
Output: 400
Explanation: arr4 = 400, which is maximum.

Constraints:
1 <= arr.size() <= 10^6
1 <= arr[i]<= 10^6
1 <= k<= arr.size()

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)
"""


class Solution:
    # Sliding window approach
    def maximum_sum_of_subarray_of_size_k(self, arr, k):
        result = 0
        size = len(arr)
        local_sum = 0

        # Condition to prevent window size greater than array
        if k > size:
            return 0

        # Sum of first k elements
        for i in range(0, k):
            local_sum += arr[i]

        result = max(result, local_sum)

        # Slide of k size window by adding next element and removing of inital element
        for i in range(k, size):
            local_sum = local_sum + arr[i] - arr[i - k]
            result = max(result, local_sum)

        return result


def main():
    arr = [int(val) for val in input().strip().split()]
    k = int(input("Enter the size of k: "))
    solution = Solution()
    print(solution.maximum_sum_of_subarray_of_size_k(arr, k))


if __name__ == "__main__":
    main()
