"""
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

    "a->b" if a != b
    "a" if a == b



Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"



Constraints:

    0 <= nums.length <= 20
    -2^31 <= nums[i] <= 2^31 - 1
    All the values of nums are unique.
    nums is sorted in ascending order.

Additional Explanation:
It is asking for you to summarize continuous numbers into a range. For example, 0, 1 should be converted to 0->1.
A more useful application would be 2,3,4,5,6,7,8,9,10 can be summarized to 2->10.
However, if you have 0,2, there is a gap in the range, so you should return "0", "2".
Example: 0, 2, 3, 4, 5, 6, 7, 8, 10, 20, 25, 26, 27
Turns to: 0, 2->8, 10, 20, 25->27
You can think of it in terms of how pages are referenced in bibliographies.
Example: Python for Dummies. Pages: 1-4, 10 means pages 1 to 4 and page 10.
"""

from typing import List


class Solution:
    def summary_ranges(self, nums: List[int]) -> List[str]:
        result = []
        i = 0
        size = len(nums)

        if size == 0:
            return result

        start_range = nums[0]

        while i < size:
            # Formation of range on each non-continous number
            if i > 0 and nums[i - 1] != nums[i] - 1:
                if start_range == nums[i - 1]:
                    result.append(str(start_range))
                else:
                    range = f"{start_range}->{nums[i - 1]}"
                    result.append(range)

                start_range = nums[i]

            i += 1

        # Processing of last element
        if start_range == nums[size - 1]:
            result.append(str(start_range))
        else:
            range = f"{start_range}->{nums[size - 1]}"
            result.append(range)

        return result


def main():
    nums = input("Enter nums: ").strip()

    nums = nums.replace(",", " ").split()
    nums = list(map(int, nums))

    soln = Solution()
    print(soln.summary_ranges(nums))


if __name__ == "__main__":
    main()
