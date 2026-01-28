"""
Given a root of a Binary Search Tree, modify and return the given BST such that it is balanced and has minimum possible height. If there is more than one answer, return any of them.

Note: The height of balanced BST returned by you will be compared with the expected height of the balanced tree.

Examples:

Input: root[] = [30, 20, N, 10, N]

Output: 2

Explanation: The above unbalanced BST is converted to balanced with the minimum possible height i.e. 2.

Input: root[] = [4, 3, 5, 2, N, N, 6, 1, N, N, 7]

Output: 3

Explanation: The above unbalanced BST is converted to balanced with the minimum possible height i.e. 3.

Constraints:
1 <= Number of Nodes <= 10^5
1 <= Node -> data <= 10^9
"""

import os, sys

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."))
from binary_search_tree_helper import BinarySearchTree, Node


class Solution:
    def unbalanced_bst_to_balanced_bst(self, root):
        # Getting inorder of unbalanced bst as it will be sorted
        inorder_res = self.inorder_traversal_rec(root, [])
        
        # Constructing the balanced tree using inorder traversal
        balanced_bst_root = self.construct_bst_from_inorder(
            inorder_res, 0, len(inorder_res) - 1
        )
        return balanced_bst_root

    def inorder_traversal_rec(self, root, result):
        if root is None:
            return

        self.inorder_traversal_rec(root.left, result)
        result.append(root.data)
        self.inorder_traversal_rec(root.right, result)
        return result

    def construct_bst_from_inorder(self, inorder_traversal, low, high):
        if low > high:
            return None

        mid = (high + low) // 2
        root = Node(inorder_traversal[mid])

        root.left = self.construct_bst_from_inorder(inorder_traversal, low, mid - 1)
        root.right = self.construct_bst_from_inorder(inorder_traversal, mid + 1, high)
        return root


def main():
    arr = input("Enter the tree level order: ").strip().split()
    arr = [x.replace(",", "").strip() for x in arr]
    bst = BinarySearchTree()
    root = bst.build_bst(arr)
    bst.print_tree()

    soln = Solution()
    result = soln.unbalanced_bst_to_balanced_bst(root)
    bst.print_tree(result)


if __name__ == "__main__":
    main()
