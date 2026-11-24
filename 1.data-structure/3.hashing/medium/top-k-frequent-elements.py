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
    # TC: O(nlogn) - due to heap operation, SC: O(n)
    def top_k_frequent(self, nums: list[int], k: int) -> list[int]:
        result = []
        freq_heap = []

        # Count for all the numbers frequency
        count_arr = Counter(nums)

        # max heap by adding -ve to freq
        for num, freq in count_arr.items():
            heapq.heappush(freq_heap, (-freq, num))

        for i in range(k):
            num = heapq.heappop(freq_heap)[1]
            result.append(num)

        return result


def main():
    nums = input("Enter the nums: ").strip().replace(",", " ").split()
    nums = map(int, nums)
    k = int(input("Enter k: "))
    print(Solution().top_k_frequent(nums, k))


if __name__ == "__main__":
    main()
