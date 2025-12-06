"""
Given a binary tree, find its preorder traversal.

Examples:

Input:
         1
        /
      4
    /    \
  4       2
Output: [1, 4, 4, 2]

Input:
       6
     /   \
    3     2
     \   / 
      1 2
Output: [6, 3, 1, 2, 2] 

Input:
         8
       / \
      3   10
     / \    \
    1   6   14
       / \   /
      4   7 13
Output: [8, 3, 1, 6, 4, 7, 10, 14, 13]

Constraints:
1 ≤ number of nodes ≤ 10^5
0 ≤ node->data ≤ 10^6

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(n)
"""

import sys, os
from queue import LifoQueue

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."))
from binary_tree_helper import BinaryTree


class Traversal:
    def pre_order_traversal_rec(self, root):
        return self._helper(root, [])

    def _helper(self, root, res):
        if root is None:
            return res

        res.append(root.data)
        self._helper(root.left, res)
        self._helper(root.right, res)

        return res

    def pre_order_traversal_ittr(self, root):
        if root is None:
            return []

        result = []
        stack = LifoQueue()
        stack.put(root)

        # DFS - Depth first search using stack for backtracking
        while not stack.empty():
            curr = stack.get()
            result.append(curr.data)

            if curr.right is not None:
                stack.put(curr.right)

            """ Adding left last so that on next pop it will get processed,
            and traverse from left to right """

            if curr.left is not None:
                stack.put(curr.left)

        return result


def main():
    arr = input("Enter tree in form of level order list: ").strip().split()
    arr = [None if val == "N" else val for val in arr]
    bt = BinaryTree()
    root = bt.build_tree(arr)
    # bt.print_tree()

    traversal = Traversal()
    # result = traversal.pre_order_traversal_rec(root)
    result = traversal.pre_order_traversal_ittr(root)
    print(result)


if __name__ == "__main__":
    main()
