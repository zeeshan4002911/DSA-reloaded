"""
Given two binary trees with their root nodes r1 and r2, return true if both of them are identical, otherwise return false.
Note: Two trees are identical when they have the same data and the arrangement of the data is also same.

Examples:

Input: r1 = [1, 2, 3, 4], r2 = [1, 2, 3, 4]

Output: true
Explanation: Trees are identical.

Input: r1 = [1, 2, 3, 4], r2 = [1, 2, 3, N, N, 4]

Output: false
Explanation: Trees are not identical.

Constraints:
1 ≤ number of nodes ≤ 10^5
1 ≤ node->data ≤ 10^9

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(h)
"""

import os, sys

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."))
from binary_tree_helper import BinaryTree

from queue import LifoQueue


class Solution:
    def check_if_identical_ittr(self, r1, r2):
        st = LifoQueue()
        st.put((r1, r2))

        while not st.empty():
            curr1, curr2 = st.get()
            # Condition to check if any one of tree is missing similar branch
            if curr1 is None or curr2 is None:
                return False
            # Condition to check if the data is different
            elif curr1.data != curr2.data:
                return False

            if curr1.right:
                st.put((curr1.right, curr2.right))
            if curr1.left:
                st.put((curr1.left, curr2.left))

        return True

    def check_if_identical_rec(self, r1, r2):
        # Condition for the base case of leaf node
        if r1 is None and r2 is None:
            return True
        # Condition to check if any one of tree is missing similar branch
        if r1 is None or r2 is None:
            return False
        # Condition to check if the data is different
        if r1.data != r2.data:
            return False

        l_result = self.check_if_identical_rec(r1.left, r2.left)
        r_result = self.check_if_identical_rec(r1.right, r2.right)

        # Not identical if either left or right sub tree is not identical
        return l_result and r_result


def main():
    arr1 = input("Enter tree 1 in form of level order list: ").strip().split()
    arr2 = input("Enter tree 2 in form of level order list: ").strip().split()
    bt = BinaryTree()
    root1 = bt.build_tree(arr1)
    root2 = bt.build_tree(arr2)

    soln = Solution()
    result = soln.check_if_identical_ittr(root1, root2)
    print(result)


if __name__ == "__main__":
    main()
