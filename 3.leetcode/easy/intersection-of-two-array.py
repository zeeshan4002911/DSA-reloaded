"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.



Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.



Constraints:

    1 <= nums1.length, nums2.length <= 1000
    0 <= nums1[i], nums2[i] <= 1000

"""

from typing import List
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = len(nums1)
        s2 = len(nums2)
        result = []

        if s1 < s2:
            small_num = nums1
            large_num_map = Counter(nums2)
        else:
            small_num = nums2
            large_num_map = Counter(nums1)

        for num in small_num:
            if num in large_num_map and large_num_map[num] > 0:
                result.append(num)
                large_num_map[num] -= 1

        return result


def main():
    nums1 = input("Enter nums1: ").strip()
    nums2 = input("Enter nums2: ").strip()

    nums1 = nums1.replace(",", " ").split()
    nums1 = list(map(int, nums1))
    nums2 = nums2.replace(",", " ").split()
    nums2 = list(map(int, nums2))

    soln = Solution()
    print(soln.intersect(nums1, nums2))


if __name__ == "__main__":
    main()
