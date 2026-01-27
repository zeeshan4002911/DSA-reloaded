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


def main():
    arr = input("Enter the tree level order: ").strip().split()
    x = 2
    arr = [x.replace(",", "").strip() for x in arr]
    bst = BinarySearchTree()
    root = bst.build_bst(arr)
    bst.print_tree()

    soln = Solution()
    result = soln.kth_largest(root, x)
    print(result)


if __name__ == "__main__":
    main()
