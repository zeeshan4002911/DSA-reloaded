"""
Given the root of a binary tree, check whether it is symmetric, i.e., whether the tree is a mirror image of itself.

Note: A binary tree is symmetric if the left subtree is a mirror reflection of the right subtree.

Examples:

Input: root = [10, 5, 5, 2, N, N, 2]

Output: True
Explanation: As the left and right half of the above tree is mirror image, the tree is symmetric.

Input: root = [8, 4, 4, N, 6, N, 6]

Output: False
Explanation:  As the left and right half of the above tree is not the mirror image, the tree is not symmetric.

Constraints:
0 ≤ number of nodes ≤ 2000
1 ≤ node->data ≤ 100

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(h)
"""

import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from binary_tree_helper import BinaryTree


class Solution:
    def check_symmetric_tree_rec(self, root):
        if root is None:
            return True

        # For single node, symmetric tree as left and right child does not exists
        if root and root.left is None and root.right is None:
            return True

        # For signle node with one child, not symmetric tree
        if root.left is None or root.right is None:
            return False

        # Convert the left sub tree to mirror tree
        root_left_mirror = self.convert_to_mirror_tree_rec(root.left)

        # Check the left mirror sub tree and right sub tree
        res = self.check_if_identical_rec(root_left_mirror, root.right)

        return res

    def convert_to_mirror_tree_rec(self, root):
        if root is None:
            return

        # Swapping the left and right node
        temp = root.left
        root.left = root.right
        root.right = temp

        self.convert_to_mirror_tree_rec(root.left)
        self.convert_to_mirror_tree_rec(root.right)

        return root

    def check_if_identical_rec(self, r1, r2):
        # Condition for the base case of leaf node
        if r1 is None and r2 is None:
            return True
        # Condition to check if any one of tree is missing similar branch
        if r1 is None or r2 is None:
            return False
        # Condition to check if the data is different
        if r1.data != r2.data:
            return False

        l_result = self.check_if_identical_rec(r1.left, r2.left)
        r_result = self.check_if_identical_rec(r1.right, r2.right)

        # Not identical if either left or right sub tree is not identical
        return l_result and r_result


def main():
    arr = input("Enter tree in form of level order list: ").strip().split()
    bt = BinaryTree()
    root = bt.build_tree(arr)

    soln = Solution()
    res = soln.check_symmetric_tree_rec(root)
    print(res)


if __name__ == "__main__":
    main()
