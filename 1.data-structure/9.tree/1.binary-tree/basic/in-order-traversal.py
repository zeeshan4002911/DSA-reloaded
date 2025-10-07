"""
Inorder traversal is a depth-first traversal method that follows this sequence:

    Left subtree is visited first.
    Root node is processed next.
    Right subtree is visited last.

"""

import sys, os

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), "..", ".."))
from tree_helper import BinaryTree


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

    traversal = Traversal()
    result = traversal.in_order_traversal(root, [])
    print(result)


if __name__ == "__main__":
    main()
