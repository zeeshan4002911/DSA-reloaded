"""
Given a binary tree, we need to print all leaf nodes of the given binary tree from left to right.
That is, the nodes should be printed in the order they appear from left to right in the given tree.

Input root[]: [1, 2, 3, 4, N, 5, 8, N, N, 6, 7, 9, 10]
        1
      /   \
     2     3
    /     /  \
   4    5      8
       / \    / \
      6   7  9   10

Output: [4, 6, 7, 9, 10]
"""

import sys, os
from queue import LifoQueue

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."))
from binary_tree_helper import BinaryTree, BinaryTreeNode


class Solution:
    def get_leaf_node_values(self, root):
        if root is None:
            return []

        result = []
        stack = LifoQueue()
        stack.put(root)

        while not stack.empty():
            curr = stack.get()
            # Condition to check leaf node
            if curr.left is None and curr.right is None:
                result.append(curr.data)

            if curr.right:
                stack.put(curr.right)
            if curr.left:
                stack.put(curr.left)

        return result


def main():
    arr = input("Enter tree in form of level order list: ").strip().split()
    bt = BinaryTree()
    root = bt.build_tree(arr)

    soln = Solution()
    result = soln.get_leaf_node_values(root)
    print(result)


if __name__ == "__main__":
    main()
