"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a binary search tree.



Example 1:

Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:

Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.



Constraints:

    1 <= nums.length <= 10^4
    -10^4 <= nums[i] <= 10^4
    nums is sorted in a strictly increasing order.

"""

from typing import List, Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sorted_array_to_BST(self, nums: List[int]) -> Optional[TreeNode]:
        size = len(nums)
        low, high = 0, size - 1
        root = self.sorted_array_to_BST_helper(nums, low, high)
        return root

    def sorted_array_to_BST_helper(self, nums, low, high):
        if low > high:
            return None

        mid = low + (high - low) // 2

        node = TreeNode(nums[mid])
        node.left = self.sorted_array_to_BST_helper(nums, low, mid - 1)
        node.right = self.sorted_array_to_BST_helper(nums, mid + 1, high)
        return node


class HelperClass:

    @staticmethod
    def level_order_bst_traversal(root):
        level_order = []
        if root is None:
            return level_order

        q = deque()
        q.appendleft(root)

        while q:
            curr = q.pop()
            level_order.append(curr.val)

            if curr.left is not None:
                q.appendleft(curr.left)

            if curr.right is not None:
                q.appendleft(curr.right)

        return level_order


def main():
    arr = input("Enter array: ").strip()
    arr = arr.replace(",", " ").split()
    arr = list(map(int, arr))

    soln = Solution()
    root = soln.sorted_array_to_BST(arr)
    # import pdb; pdb.set_trace()
    print(HelperClass.level_order_bst_traversal(root))


if __name__ == "__main__":
    main()
