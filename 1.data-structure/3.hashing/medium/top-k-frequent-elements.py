"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.



Example 1:

Input: nums = [1,1,1,2,2,3], k = 2

Output: [1,2]

Example 2:

Input: nums = [1], k = 1

Output: [1]

Example 3:

Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

Output: [1,2]



Constraints:

    1 <= nums.length <= 10^5
    -10^4 <= nums[i] <= 10^4
    k is in the range [1, the number of unique elements in the array].
    It is guaranteed that the answer is unique.



Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

import heapq
from collections import Counter


class Solution:
    # TC: O(n), SC: O(n)
    def top_k_frequent(self, nums: list[int], k: int) -> list[int]:
        result = []
        count_hashmap = {}

        for num in nums:
            count_hashmap[num] = count_hashmap.get(num, 0) + 1

        # Maximum any number can be present in all the place of nums, index store frequency and value store number
        freq_arr = [[] for _ in range(len(nums) + 1)]
        for key, value in count_hashmap.items():
            freq_arr[value].append(key)

        item = 0
        for i in range(len(freq_arr) - 1, -1, -1):
            for ele in freq_arr[i]:
                result.append(ele)
                item += 1
                if item == k:
                    return result

        return result

    # TC: O(nlogn) - due to heap operation, SC: O(n)
    def top_k_frequent_heap(self, nums: list[int], k: int) -> list[int]:
        result = []
        freq_heap = []

        # Count for all the numbers frequency
        count_arr = Counter(nums)

        # Min heap with k elements instead max heap with all nums
        for num, freq in count_arr.items():
            heapq.heappush(freq_heap, (freq, num))
            if len(freq_heap) > k:
                heapq.heappushpop(freq_heap)

        for i in range(k):
            num = heapq.heappop(freq_heap)[1]
            result.append(num)

        return result


def main():
    nums = input("Enter the nums: ").strip().replace(",", " ").split()
    nums = list(map(int, nums))
    k = int(input("Enter k: "))
    print(Solution().top_k_frequent(nums, k))


if __name__ == "__main__":
    main()
