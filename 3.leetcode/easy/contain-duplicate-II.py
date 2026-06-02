"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.



Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false



Constraints:

    1 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9
    0 <= k <= 10^5

"""

from typing import List
from collections import Counter


class Solution:
    def contains_nearby_duplicate(self, nums: List[int], k: int) -> bool:
        """
        Sliding Window: If window size is <= k then any then any two i and j can be equal
        if we count the number of occurence within the window
        """
        count_map = Counter()
        size = len(nums)

        # Edge case to handle window size greater or equals to input size
        if k >= size:
            count_map = Counter(nums)
            # This only runs once, so most_common(1) here is acceptable
            if count_map and count_map.most_common(1)[0][1] >= 2:
                return True
            return False

        # First (K + 1) window processing
        for i in range(k + 1):
            count_map[nums[i]] += 1
            # O(1) Check immediately during insertion
            if count_map[nums[i]] >= 2:
                return True

        # Sliding window by adding next and removing window starting element
        for i in range(k + 1, size):
            window_start = i - (k + 1)
            count_map[nums[window_start]] -= 1
            count_map[nums[i]] += 1

            # O(1) Check only the newly added element
            if count_map[nums[i]] >= 2:
                return True

        return False

    def contains_nearby_duplicate_2(self, nums: List[int], k: int) -> bool:
        # Use a hash set to store the elements of the current window
        window_set = set()

        for i, num in enumerate(nums):
            # If the element is already in the set, we found a duplicate within k distance
            if num in window_set:
                return True

            # Add the current element to the set
            window_set.add(num)

            # Maintain the window size: if the window exceeds size k,
            # remove the oldest element (which is at index i - k)
            if len(window_set) > k:
                window_set.remove(nums[i - k])

        return False


def main():
    arr = input("Enter array: ").strip()
    k = int(input("Enter the value of k: ").strip())
    arr = arr.replace(",", " ").split()
    arr = list(map(int, arr))
    soln = Solution()
    print(soln.contains_nearby_duplicate_2(arr, k))


if __name__ == "__main__":
    main()
