"""
Given a Binary Search Tree, the task is to find the second largest element in the given BST.

Example:

    Input:
    Second-largest-element-in-BST-1
        7
      /   \
     4     8
    / \
   3   5

    Output:  7
    Explanation:  The Second Largest value in the given BST is 7.

    Input:
    Second-largest-element-in-BST-2
        10
       /  \
      5    20
             \
              30

    Output:  20
    Explanation:  The Second Largest value in the given BST is 20
"""

import os, sys

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."))
from binary_search_tree_helper import BinarySearchTree

from queue import LifoQueue


class Solution:
    def kth_largest(self, root, x=2):
        if root is None:
            return None

        k_count = 0
        st = LifoQueue()
        curr = root

        while curr or not st.empty():
            # Reverse inorder traversal, traversing to the right most node
            while curr:
                st.put(curr)
                curr = curr.right

            curr = st.get()

            k_count += 1
            # Counting from inorder end (reverse inorder)
            if k_count == x:
                return curr.data

            curr = curr.left

        return None

    def kth_largest_rec(self, root, x=2):
        if root is None:
            return None

        # List instead of primative int to mutate the value by passing as reference on each recursive call
        k_count = [0]
        return self.kth_largest_rec_helper(root, x, k_count)

    def kth_largest_rec_helper(self, root, x, k_count):
        if root is None:
            return None

        # Reverse inorder traversal as the largest will be at the end of inorder result
        r_subtree = self.kth_largest_rec_helper(root.right, x, k_count)

        k_count[0] += 1
        if k_count[0] == x:
            return root.data

        l_subtree = self.kth_largest_rec_helper(root.left, x, k_count)
        if r_subtree is not None:
            return r_subtree
        if l_subtree is not None:
            return l_subtree
        return None


def main():
    arr = input("Enter the tree level order: ").strip().split()
    x = 2
    arr = [x.replace(",", "").strip() for x in arr]
    bst = BinarySearchTree()
    root = bst.build_bst(arr)
    bst.print_tree()

    soln = Solution()
    result = soln.kth_largest_rec(root, x)
    print(result)


if __name__ == "__main__":
    main()
