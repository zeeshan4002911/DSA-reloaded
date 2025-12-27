"""
Given the root of a binary tree, convert the binary tree to its Mirror tree.

Note: Mirror of a Binary Tree T is another Binary Tree M(T) with left and right children of all non-leaf nodes interchanged.

Examples:

Input: root = [1, 2, 3, N, N, 4]
Output: [1, 3, 2, N, 4]
Explanation:

In the inverted tree, every non-leaf node has its left and right child interchanged.

Input: root = [1, 2, 3, 4, 5]
Output: [1, 3, 2, N, N, 5, 4]
Explanation:

In the inverted tree, every non-leaf node has its left and right child interchanged.

Constraints:
1 ≤ number of nodes ≤ 10^4
1 ≤ node->data ≤ 10^5

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(n)
"""

import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from binary_tree_helper import BinaryTree

from queue import LifoQueue


class Solution:
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

    def convert_to_mirror_tree_ittr(self, root):
        if root is None:
            return root

        st = LifoQueue()
        st.put(root)

        while not st.empty():
            curr = st.get()
            # Swapping the left and right node
            temp = curr.left
            curr.left = curr.right
            curr.right = temp

            if curr.right:
                st.put(curr.right)
            if curr.left:
                st.put(curr.left)

        return root


def main():
    arr = input("Enter tree in form of level order list: ").strip().split()
    bt = BinaryTree()
    root = bt.build_tree(arr)

    soln = Solution()
    res_root = soln.convert_to_mirror_tree_rec(root)
    bt.print_tree(res_root)


if __name__ == "__main__":
    main()
