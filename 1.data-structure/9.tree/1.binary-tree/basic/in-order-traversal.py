"""
Given a root of a Binary Tree, your task is to return its Inorder Traversal.

Note: An inorder traversal first visits the left child (including its entire subtree), then visits the node, and finally visits the right child (including its entire subtree).

Examples:

Input: root = [1, 2, 3, 4, 5]

Output: [4, 2, 5, 1, 3]
Explanation: The inorder traversal of the given binary tree is [4, 2, 5, 1, 3].

Input: root = [8, 1, 5, N, 7, 10, 6, N, 10, 6]

Output: [1, 7, 10, 8, 6, 10, 5, 6]
Explanation: The inorder traversal of the given binary tree is [1, 7, 10, 8, 6, 10, 5, 6].

Constraints:
1 ≤ number of nodes ≤ 3*10^4
0 ≤ node->data ≤ 10^5

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)
"""

"""
Inorder traversal is a depth-first traversal method that follows this sequence:

    Left subtree is visited first.
    Root node is processed next.
    Right subtree is visited last.

"""

import sys, os

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."))
from binary_tree_helper import BinaryTree


class Traversal:
    def in_order_traversal(self, root, res):
        if root is None:
            return

        self.in_order_traversal(root.left, res)
        res.append(root.data)
        self.in_order_traversal(root.right, res)

        return res


def main():
    arr = input("Enter tree in form of level order list: ").strip().split()
    arr = [None if val == "N" else val for val in arr]
    bt = BinaryTree()
    root = bt.build_tree(arr)
    # bt.print_tree()

    traversal = Traversal()
    result = traversal.in_order_traversal(root, [])
    print(result)


if __name__ == "__main__":
    main()
