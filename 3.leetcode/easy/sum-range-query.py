"""
Given an integer array nums, handle multiple queries of the following type:

    Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.

Implement the NumArray class:

    NumArray(int[] nums) Initializes the object with the integer array nums.
    int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).



Example 1:

Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3



Constraints:

    1 <= nums.length <= 10^4
    -10^5 <= nums[i] <= 10^5
    0 <= left <= right < nums.length
    At most 10^4 calls will be made to sumRange.

"""

from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        result = 0
        last = len(self.nums) - 1

        if left > right or left > last or right > last:
            return result

        for i in range(left, right + 1):
            result += self.nums[i]

        return result


class UnSupportedQuery(Exception):
    """Unsupported query error message"""


class Solution:
    def sum_range_query(self, queries: List[str], values: List[List[int]]) -> List[int]:
        result = []
        for i in range(len(queries)):
            if queries[i] == "NumArray":
                nums = values[i][0]
                obj = NumArray(nums)
            elif queries[i] == "sumRange":
                res = obj.sumRange(values[i][0], values[i][1])
                result.append(res)
            else:
                raise UnSupportedQuery("Unsupported query")
        return result


def main():
    raw_queries = input("Enter queries: ").strip()
    raw_ranges = input("Enter ranges: ").strip()

    queries = list(
        map(
            str, raw_queries.replace(",", " ").replace("'", "").replace('"', "").split()
        )
    )
    stack = []
    current_list = []
    num_buffer = ""

    for char in raw_ranges:
        if char == "[":
            stack.append(current_list)
            current_list = []
        elif char in "0123456789-":
            num_buffer += char
        elif char in ",]":
            if num_buffer:
                current_list.append(int(num_buffer))
                num_buffer = ""

            # If the list is closing, pop back up to the parent container
            if char == "]" and stack:
                parent_list = stack.pop()
                parent_list.append(current_list)
                current_list = parent_list
    casted_ranges = current_list[0] if current_list else []

    soln = Solution()
    print(soln.sum_range_query(queries, casted_ranges))


if __name__ == "__main__":
    main()
