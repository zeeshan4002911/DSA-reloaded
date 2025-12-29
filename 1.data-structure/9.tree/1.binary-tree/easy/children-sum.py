"""
Given the root of a binary tree, determine whether the tree satisfies the Children Sum Property. In this property, each non-leaf node must have a value equal to the sum of its left and right children's values. A NULL child is considered to have a value of 0, and all leaf nodes are considered valid by default.
Return true if every node in the tree satisfies this condition, otherwise return false.

Examples:

Input: root = [35, 20, 15, 15, 5, 10, 5]

Output: True
Explanation: Here, every node is sum of its left and right child.

Input: root = [1, 4, 3, 5]

Output: False
Explanation: Here, 1 is the root node and 4, 3 are its child nodes. 4 + 3 = 7 which is not equal to the value of root node. Hence, this tree does not satisfy the given condition.

Constraints:
1 ≤ number of nodes ≤ 10^5
0 ≤ node->data ≤ 10^5

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(h)
"""

import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from binary_tree_helper import BinaryTree


class Solution:
    def check_children_sum_parent(self, root):
        if root is None:
            return True

        l_res = self.check_children_sum(root.left)
        r_res = self.check_children_sum(root.right)

        if l_res is False or r_res is False:
            return False

        child_sum = 0
        if root.left:
            child_sum += root.left.data
        if root.right:
            child_sum += root.right.data
        res = root.data == child_sum
        
        return res


def main():
    arr = input("Enter tree in form of level order list: ").strip().split()
    bt = BinaryTree()
    root = bt.build_tree(arr)

    soln = Solution()
    res = soln.check_children_sum_parent(root)
    print(res)


if __name__ == "__main__":
    main()
