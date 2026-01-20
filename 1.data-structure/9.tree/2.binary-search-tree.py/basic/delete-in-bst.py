"""
Given the root of a binary search tree and a node value x. Delete the node with the given value x from the tree. If no node with value x exists, then do not make any change. Return the root of the tree after deleting the node with value x.

Note: You may return any valid BST after deleting the specified node. The driver code will print true if the resulting tree is a valid BST after deletion, and false otherwise.

Examples :

Input: root = [2, 1, 3], x = 12

Output: true
Explanation: In the given input there is no node with value 12, so the tree will remain same.

Input: root = [1, N, 2, N, 8, 5, 11, 4, 7, 9, 12], x = 11

Output: true
Explanation: In the given input, one of the possible tree after deleting 11 will be

Input: root = [2, 1, 3], x = 3

Output: [2, 1]
Explanation: In the given input, only possible tree after deleting 3 will be

Constraints:
1 ≤ number of nodes ≤ 10^5
1 ≤ node->data, x ≤ 10^5

Expected Complexities
Time Complexity: O(Height of the BST)
Auxiliary Space: O(Height of the BST)
"""

import os, sys

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."))
from binary_search_tree_helper import BinarySearchTree, Node


class Solution:
    def deletion_rec(self, root, x):
        # Base case for leaf nodes
        if root is None:
            return root

        if root.data < x:
            root.right = self.deletion_rec(root.right, x)
        elif root.data > x:
            root.left = self.deletion_rec(root.left, x)
        else:
            # Case 1: Leaf node deletion
            if root.left is None and root.right is None:
                return None

            # Case 2: If any one child is not present then replacing the parent with other child
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

            # Case 3a: If both left and right child are present (replacement with inorder successor)
            succ = self.get_inorder_successor(root)
            root.data = succ.data
            root.right = self.deletion_rec(root.right, succ.data)

            """
            # Case 3b: Or replacement with inorder predecessor
            pred = self.get_inorder_predecessor(root)
            root.data = pred.data
            root.left = self.deletion_rec(root.left, pred.data)
            """

        return root

    def get_inorder_successor(self, root):
        # In order successor is next node after root in in-order traversal so it's present in right subtree
        curr = root.right

        # Going to left most node as it will be having the smallest value in this right subtree
        while curr is not None and curr.left is not None:
            curr = curr.left

        return curr

    def get_inorder_predecessor(self, root):
        curr = root.left
        while curr is not None and curr.right is not None:
            curr = curr.right
        return curr


def main():
    arr = input("Enter the tree level order: ").strip().split()
    key = int(input("Enter the key to search: ").strip())
    arr = [x.replace(",", "").strip() for x in arr]
    bst = BinarySearchTree()
    root = bst.build_bst(arr)
    bst.print_tree()

    soln = Solution()
    result = soln.deletion_rec(root, key)
    print(result)


if __name__ == "__main__":
    main()


"""
Scenarios to handle while doing deletion in BST to maintain the BST property

Case 1: Node has No Children (Leaf Node)

If the target node is a leaf node, it can be directly removed from the tree since it has no child to maintain.

Case 2: Node has One Child(Left or Right Child)

If the target node has only one child, we remove the node and connect its parent directly to its only child. This way, the tree remains valid after deletion of target node.

Case 3: Node has Two Children

If the target node has two children, deletion is slightly more complex.

To maintain the BST property, we need to find a replacement node for the target. The replacement can be either:

    The inorder successor — the smallest value in the right subtree, which is the next greater value than the target node.
    The inorder predecessor — the largest value in the left subtree, which is the next smaller value than the target node.

Once the replacement node is chosen, we replace the target node’s value with that node’s value, and then delete the replacement node, which will now fall under Case 1 (no children) or Case 2 (one child).

"""
