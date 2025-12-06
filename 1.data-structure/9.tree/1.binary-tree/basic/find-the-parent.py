"""
Given a Binary Tree and a node, the task is to find the parent of the given node in the tree.
Return -1 if the given node is the root node.
Note: In a binary tree, a parent node of a given node is the node that is directly connected above the given node.

Input: root = [1, 7, 3, 4, 5, 6], target = 3
         1
       /   \
      7     3
    /   \    \
   4     5    6
Output: 1

Input: root = [1, 7, 3, 4, 5, 6], target = 1
         1
       /   \
      7     3
    /   \    \
   4     5    6
Output: -1

"""

import sys, os

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."))
from binary_tree_helper import BinaryTree


class Solution:
    def find_the_parent(self, root, target):
        if root is None:
            return -1

        if (root.left is not None and root.left.data == target) or (
            root.right is not None and root.right.data == target
        ):
            return root.data

        res_l = self.find_the_parent(root.left, target)
        res_r = self.find_the_parent(root.right, target)

        if res_l != -1:
            return res_l
        elif res_r != -1:
            return res_r
        else:
            return -1


def main():
    arr = input("Enter tree in form of level order list: ").strip().split()
    target = input("Enter target: ").strip()
    arr = [None if val == "N" else val for val in arr]
    bt = BinaryTree()
    root = bt.build_tree(arr)

    soln = Solution()
    result = soln.find_the_parent(root, target)
    print(result)


if __name__ == "__main__":
    main()
