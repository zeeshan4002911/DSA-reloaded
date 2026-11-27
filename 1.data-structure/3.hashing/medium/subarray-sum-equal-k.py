"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.



Example 1:

Input: nums = [2,-1,1,2], k = 2
Output: 4
Explanation: [2], [2,-1,1], [-1,1,2], [2] are the subarrays whose sum is equals to k.

Example 2:

Input: nums = [1,1,1], k = 2
Output: 2

Example 3:

Input: nums = [1,2,3], k = 3
Output: 2


Constraints:

    1 <= nums.length <= 2 * 10^4
    -1000 <= nums[i] <= 1000
    -10^7 <= k <= 10^7

"""

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = curr_sum = 0
        prefixSum_hashmap = {0: 1}

        # key insight: if prefixSum[j] - prefixSum[i] = k, then subarray from index i+1 to j has sum k
        for num in nums:
            curr_sum += num
            diff = curr_sum - k

            result += prefixSum_hashmap.get(diff, 0)
            # Store the count of number of subarray including current one (Even with zero it' sum up to k)
            prefixSum_hashmap[curr_sum] = prefixSum_hashmap.get(curr_sum, 0) + 1

        return result


def main():
    nums = input("Enter the nums: ").strip().replace(",", " ").split()
    nums = list(map(int, nums))
    k = int(input("Enter k: "))
    print(Solution().top_k_frequent(nums, k))


if __name__ == "__main__":
    main()
