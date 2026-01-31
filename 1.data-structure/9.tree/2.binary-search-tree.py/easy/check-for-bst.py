"""
Given the root of a binary tree. Check whether it is a BST or not.

A BST is defined as follows:

    The left subtree of a node contains only nodes with data less than the node's data.
    The right subtree of a node contains only nodes with data greater than the node's data.
    Both the left and right subtrees must also be binary search trees.

Note: We are considering that BSTs can not contain duplicate Nodes.

Examples:

Input: root = [2, 1, 3, N, N, N, 5]


Output: true
Explanation: The left subtree of every node contains smaller data and right subtree of every node contains greater data. Hence, the tree is a BST.

Input: root = [2, N, 7, N, 6, N, 9]



Output: false
Explanation: Since the node to the right of node with data 7 has lesser value 6, hence it is not a valid BST.

Input: root = [10, 5, 20, N, N, 9, 25]


Output: false
Explanation: The node with data 9 present in the right subtree has lesser key value than root node 10.

Constraints:
1 ≤ number of nodes ≤ 10^5
1 ≤ node->data ≤ 10^9

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(h)
"""

import os, sys

# Importing binary tree helper to build tree instead of bst builder
sys.path.append(
    os.path.join(
        os.path.abspath(os.path.dirname(__file__)), "..", "..", "1.binary-tree"
    )
)
from binary_tree_helper import BinaryTree


class Solution:
    def check_for_bst_rec(self, root):
        return self.check_for_bst_rec_helper(root, [0])

    # BST check based on bst rule of inorder sorted result
    def check_for_bst_rec_helper(self, root, prev):
        if root is None:
            return True

        res_left_subtree = self.check_for_bst_rec_helper(root.left, prev)
        if res_left_subtree is False:
            return False

        # Checking the current inorder value, as inorder gives non-decreasing order of values for bst
        if prev[0] > root.data:
            return False

        prev[0] = root.data

        res_left_subtree = self.check_for_bst_rec_helper(root.right, prev)
        if res_left_subtree is False:
            return False

        return True

    # BST check using node value range similar to bst construction
    def check_for_bst_using_range(
        self, root, min_val=-float("inf"), max_val=float("inf")
    ):
        if root is None:
            return True

        # If current node is not in valid range
        if root.data <= min_val or root.data >= max_val:
            return False

        res_left_subtree = self.check_for_bst_using_range(root.left, min_val, root.data)
        res_right_subtree = self.check_for_bst_using_range(root.right, root.data, max_val)
        return res_left_subtree and res_right_subtree


def main():
    arr = input("Enter the tree level order: ").strip().split()
    arr = [x.replace(",", "").strip() for x in arr]
    arr = [int(x) if x != "N" else x for x in arr]
    bt = BinaryTree()
    root = bt.build_tree(arr)
    bt.print_tree()

    soln = Solution()
    result = soln.check_for_bst_rec(root)
    print(result)


if __name__ == "__main__":
    main()
