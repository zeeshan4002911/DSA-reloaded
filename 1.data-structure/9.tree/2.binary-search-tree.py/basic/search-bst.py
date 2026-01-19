"""
Given the root of a Binary Search Tree and a node value key, find if the node with value key is present in the BST or not.

Examples:

Input: root = [6, 2, 8, N, N, 7, 9], key = 8

Output: true
Explanation: 8 is present in the BST as right child of root.

Input: root = [16, 12, 18, 10, N, 17, 19], key = 14

Output: false
Explanation: 14 is not present in the BST

Constraints:
1 ≤ number of nodes ≤ 3*10^4
1 ≤ node->data, key ≤ 10^9

Expected Complexities
Time Complexity: O(h)
Auxiliary Space: O(1)
"""

import os, sys

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."))
from binary_search_tree_helper import BinarySearchTree, Node


class Solution:
    def search_ittr(self, root, key):
        # Condition for no tree root
        if root is None:
            return False

        curr = root
        while curr is not None:
            if curr.data < key:
                curr = curr.right
            elif curr.data > key:
                curr = curr.left
            else:
                # In case of found
                return True

        # Post search, false to mark not found
        return False

    def search_rec(self, root, key):
        if root is None:
            return False
        # Condition for checking
        if root.data == key:
            return True

        left_tree_res = self.search_rec(root.left, key)
        right_tree_res = self.search_rec(root.right, key)

        # Return True if search is able to find the key in left or right subtree
        return left_tree_res or right_tree_res


def main():
    arr = input("Enter the tree level order: ").strip().split()
    key = int(input("Enter the key to search: ").strip())
    arr = [int(val) if isinstance(val, int) else val for val in arr]
    bst = BinarySearchTree()
    root = bst.build_bst(arr)
    # bst.print_tree()

    soln = Solution()
    result = soln.search_ittr(root, key)
    print(result)


if __name__ == "__main__":
    main()
