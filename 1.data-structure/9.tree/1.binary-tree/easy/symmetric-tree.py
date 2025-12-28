"""
Given the root of a binary tree, check whether it is symmetric, i.e., whether the tree is a mirror image of itself.

Note: A binary tree is symmetric if the left subtree is a mirror reflection of the right subtree.

Examples:

Input: root = [10, 5, 5, 2, N, N, 2]

Output: True
Explanation: As the left and right half of the above tree is mirror image, the tree is symmetric.

Input: root = [8, 4, 4, N, 6, N, 6]

Output: False
Explanation:  As the left and right half of the above tree is not the mirror image, the tree is not symmetric.

Constraints:
0 ≤ number of nodes ≤ 2000
1 ≤ node->data ≤ 100

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(h)
"""

import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from binary_tree_helper import BinaryTree


class Solution:
    def check_symmetric_tree_rec(self, root):
        if root is None:
            return True

        return self.check_symmetric_helper(root.left, root.right)

    def check_symmetric_helper(self, r1, r2):
        # Condition for the base case of leaf node
        if r1 is None and r2 is None:
            return True
        # Condition to check if any one of tree is missing similar branch
        if r1 is None or r2 is None:
            return False
        # Condition to check if the data is different
        if r1.data != r2.data:
            return False

        """
        Checking both the branch of tree, 
        1) left node of left sub tree with right node of right sub tree
        2) right node of left sub tree with left node of right sub tree
        """
        res_1 = self.check_symmetric_helper(r1.left, r2.right)
        res_2 = self.check_symmetric_helper(r1.right, r2.left)

        return res_1 and res_2


def main():
    arr = input("Enter tree in form of level order list: ").strip().split()
    bt = BinaryTree()
    root = bt.build_tree(arr)

    soln = Solution()
    res = soln.check_symmetric_tree_rec(root)
    print(res)


if __name__ == "__main__":
    main()
