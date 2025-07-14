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
                result += (window_size * (window_size - 1)) / 2
                window_size = 1

        # Add the subarray for the end window in result count
        result += (window_size * (window_size - 1)) / 2

        return int(result)


def main():
    arr = [int(val) for val in input().strip().split()]
    solution = Solution()
    print(solution.count_increasing_substring(arr))


if __name__ == "__main__":
    main()

## Formula Derivation
"""
    *** Total Number of Subarrays ***
    For a sequence of length n:
    - Subarrays of length 1: There are n such subarrays (each individual element).
    - Subarrays of length 2: There are n-1 such subarrays (each consecutive pair).
    - Subarrays of length 3: There are n-2 such subarrays (each consecutive triplet), and so on, until:
    - Subarrays of length n: There is exactly 1 subarray (the whole array itself).

    For a strictly increasing sequence of length n, the total number of subarrays of all lengths (from 1 to n) is given by:
    
    Total subarrays = 1+2+3+⋯+n = n(n+1)/2

    This counts all possible subarrays, including those of length 1.
    
    *** Subarrays of Length Greater Than 1 ***
    To count only the subarrays of length greater than 1, we need to exclude the single-element subarrays (subarrays of length 1).
        - The number of subarrays of length 1 is simply n (one for each element).
        - The number of subarrays of length greater than 1 can be found by subtracting the single-element subarrays (length 1) from the total count.

    So, the formula for counting subarrays of length greater than 1 is:
    Subarrays of length > 1 = n(n+1)/2 - n
    simplified version = n(n-1)/2
    
    same way total Subarray of length > 2 (more than 2 element in subarray) 
    = n(n+1)/2 - n - (n - 1) = n(n-3)/2
"""
