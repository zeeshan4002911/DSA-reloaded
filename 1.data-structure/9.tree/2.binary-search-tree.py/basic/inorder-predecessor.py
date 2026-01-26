"""
Given a Binary Search Tree, the task is to find the In-Order predecessor of a given target key.

In a Binary Search Tree (BST), the Inorder predecessor of a node is the previous node in the Inorder traversal of the BST. The Inorder predecessor is NULL for the first node in the Inorder traversal.

Examples:

    In the below diagram, inorder predecessor of 8 is 4, inorder predecessor of 10 is 8 and inorder predecessor of 14 is 12.

        20
      /    \
     8      22
    / \
   4   12
      /  \
     10   14
"""

import os, sys

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."))
from binary_search_tree_helper import BinarySearchTree, Node


class Solution:
    def get_inorder_predecessor_ittr(self, root, x):
        if root is None:
            return -1

        prec_node = None
        curr = root
        while curr:
            if curr.data < x.data:
                # Step 2: Post finding the value it go to right side always
                # as x will be smaller in it's subtree after step 1
                prec_node = curr
                curr = curr.right
            elif curr.data < x.data:
                curr = curr.left
            else:
                # Step 1: Case where node value is found
                curr = curr.left

        return -1 if prec_node is None else prec_node.data


def main():
    arr = input("Enter the tree level order: ").strip().split()
    x = int(input("Enter the value of x: ").strip())
    x_node = Node(x)
    arr = [x.replace(",", "").strip() for x in arr]
    bst = BinarySearchTree()
    root = bst.build_bst(arr)
    bst.print_tree()

    soln = Solution()
    result = soln.get_inorder_predecessor_ittr(root, x_node)
    print(result)


if __name__ == "__main__":
    main()
