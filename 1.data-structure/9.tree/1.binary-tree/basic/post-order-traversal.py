"""
Given the root of a Binary Tree, your task is to return its Postorder Traversal.

Note: A postorder traversal first visits the left child (including its entire subtree), then visits the right child (including its entire subtree), and finally visits the node itself.

Examples:

Input: root = [19, 10, 8, 11, 13]
     19
    /  \
   10   8
  / \
11   13

Output: [11, 13, 10, 8, 19]
Explanation: The postorder traversal of the given binary tree is [11, 13, 10, 8, 19].

Input: root = [11, 15, N, 7]

     11
    /  \
   15   N
  /
7

Output: [7, 15, 11]
Explanation: The postorder traversal of the given binary tree is [7, 15, 11].

Constraints:
1 ≤ number of nodes ≤ 3*10^4
0 ≤ node->data ≤ 10^5

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)
"""

import sys, os
from queue import LifoQueue

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."))
from binary_tree_helper import BinaryTree


class Traversal:
    def post_order_traversal_rec(self, root):
        return self._helper(root, [])

    def _helper(self, root, res):
        if root is None:
            return res

        self._helper(root.left, res)
        self._helper(root.right, res)
        res.append(root.data)

        return res

    def post_order_traversal_ittr(self, root):
        if root is None:
            return []

        result = []
        stack = LifoQueue()
        stack.put(root)

        # Modified pre-order traversal [root->right->left] + reverse
        while not stack.empty():
            curr = stack.get()
            result.append(curr.data)

            if curr.left is not None:
                stack.put(curr.left)

            if curr.right is not None:
                stack.put(curr.right)

        return result[::-1]


def main():
    arr = input("Enter tree in form of level order list: ").strip().split()
    arr = [None if val == "N" else val for val in arr]
    bt = BinaryTree()
    root = bt.build_tree(arr)
    # bt.print_tree()

    traversal = Traversal()
    # result = traversal.post_order_traversal_rec(root)
    result = traversal.post_order_traversal_ittr(root)
    print(result)


if __name__ == "__main__":
    main()
