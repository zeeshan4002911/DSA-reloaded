"""
Given the root of a binary tree, determine if it is height-balanced or not.

Note: A binary tree is considered height-balanced if the absolute difference in heights of the left and right subtrees is at most 1 for every node in the tree.

Examples:

Input: root = [10, 20, 30, 40, 60]

Output: true
Explanation: The height difference between the left and right subtrees at all nodes is at most 1. Hence, the tree is balanced.

Input: root = [1, 2, 3, 4, N, N, N, 5]

Output: false
Explanation: The height difference between the left and right subtrees at node 2 is 2, which exceeds 1. Hence, the tree is not balanced.

Constraints:
1 ≤ number of nodes ≤ 1000
1 ≤ node->data ≤ 10^4

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(h)
"""

import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from binary_tree_helper import BinaryTree

from queue import LifoQueue


class Solution:
    # TC: O(N), SC: O(h), on skewed tree O(N)
    def balanced_tree_check_rec(self, root):
        result, height = self.balanced_tree_check_op(root)
        return result

    def balanced_tree_check_op(self, root):
        if root is None:
            return (True, 0)

        l_res, l_height = self.balanced_tree_check_op(root.left)
        r_res, r_height = self.balanced_tree_check_op(root.right)

        res = l_res and r_res and abs(l_height - r_height) <= 1
        height = max(l_height, r_height) + 1

        return (res, height)

    # TC: O(N^2), SC: O(h), on skewed tree O(N)
    def balanced_tree_check(self, root):
        if root is None:
            return True

        l_res = self.balanced_tree_check(root.left)
        r_res = self.balanced_tree_check(root.right)

        if l_res is False or r_res is False:
            return False

        l_sub_tree_height = self.get_height(root.left)
        r_sub_tree_height = self.get_height(root.right)

        res = abs(l_sub_tree_height - r_sub_tree_height) <= 1

        return res

    def get_height(self, root, height=0):
        if root is None:
            return height

        return max(
            self.get_height(root.left, height + 1),
            self.get_height(root.right, height + 1),
        )


def main():
    arr = input("Enter tree in form of level order list: ").strip().split()
    bt = BinaryTree()
    root = bt.build_tree(arr)

    soln = Solution()
    res = soln.balanced_tree_check_rec(root)
    print(res)


if __name__ == "__main__":
    main()
