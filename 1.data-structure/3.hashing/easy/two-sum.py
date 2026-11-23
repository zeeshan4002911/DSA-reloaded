"""
You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9

Output: [0,1]

Explanation:

The sum of nums[0] and nums[1] is 2 + 7 = 9, which equals the target. Therefore, the indices [0, 1] are returned.

Example 2:

Input: nums = [3,2,4], target = 6

Output: [1,2]

Explanation:

The sum of nums[1] and nums[2] is 2 + 4 = 6, which equals the target. Therefore, the indices [1, 2] are returned.

Example 3:

Input: nums = [3,3], target = 6

Output: [0,1]

Explanation:

The sum of nums[0] and nums[1] is 3 + 3 = 6, which equals the target. Therefore, the indices [0, 1] are returned.



Constraints:

    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.


Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""


class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        hash_map = {}

        for i, ele in enumerate(nums):
            rem = target - ele

            # If complement already exists in the hash map
            if rem in hash_map:
                return [hash_map[rem], i]

            hash_map[ele] = i


def main():
    nums = input("Enter the nums: ").strip().replace(",", " ")
    nums = list(map(int, nums.split()))
    target = int(input("Enter the target: ").strip())

    sol = Solution()
    print(Solution().two_sum(nums, target))


if __name__ == "__main__":
    main()
