"""
Given an array arr[] of integers, count the number of subarrays in arr[] which are strictly increasing with size greater or equal to 2. A subarray is a contiguous part of array. A subarray is strictly increasing if each element is greater then it's previous element if it exists.

Examples:

Input: arr[] = [1, 3, 3, 2, 3, 5]
Output: 4
Explanation: Increasing Subarrays are : arr[0,1], arr[3,4], arr[3,5], arr[4,5].

Input: arr[] = [1, 5]
Output: 1
Explanation:The only Increasing Subarray is arr[0,1].

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1 <= arr.size() <= 10^6
1 <= arri <= 10^7

"""


class Solution:
    # Sliding window approach
    def count_increasing_substring(self, arr):
        size = len(arr)
        result = 0
        window_size = 1
        
        for i in range(1, size):
            # Expansion of window in case the sequence in stricly increasing
            if arr[i] > arr[i - 1]:
                window_size += 1
            else:
                # Possible subarray addition and resent of window length
                result += ((window_size * (window_size - 1)) / 2)
                window_size = 1
        
        # Add the subarray for the end window in result count
        result += ((window_size * (window_size - 1)) / 2)
        
        return int(result)


def main():
    arr = [int(val) for val in input().strip().split()]
    solution = Solution()
    print(solution.count_increasing_substring(arr))


if __name__ == "__main__":
    main()
