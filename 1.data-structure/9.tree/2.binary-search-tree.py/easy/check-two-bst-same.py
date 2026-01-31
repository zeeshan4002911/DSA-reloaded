"""
Given two Binary Search Trees consisting of unique positive elements, the task is to check whether the two BSTs contain the same set of elements or not. The structure of the two given BSTs can be different. 

Example:
        15                15
       /   \            /    \
     10    20          12    20
    /  \     \        /        \
   5   12    25      5         25
                      \
                       10

Output: True
Explanation: The above two BSTs contains same set of elements {5, 10, 12, 15, 20, 25}
"""

import os, sys

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."))
from binary_search_tree_helper import BinarySearchTree

from collections import deque


class Solution:
    """
    Checking the inorder of both the bst to verify that the elements are same or not
    Alternative: Using set/map to store the visited values of first bst,
      and then checking whether all values of sets are present in second bst
    """

    def check_if_two_bst_contains_same_elements(self, root1, root2):
        inorder1 = self.get_in_order_traversal(root1)
        inorder2 = self.get_in_order_traversal(root2)

        # checks if both the content and the order of elements are identical
        if inorder1 == inorder2:
            return True

        return False

    def get_in_order_traversal(self, root):
        curr = root
        result = []
        st = deque()

        while curr or st:
            while curr:
                st.append(curr)
                curr = curr.left

            curr = st.pop()
            result.append(curr.data)

            curr = curr.left

        return result


def main():
    arr1 = input("Enter the tree level order: ").strip().split()
    arr2 = input("Enter the tree level order: ").strip().split()
    arr1 = [x.replace(",", "").strip() for x in arr1]
    arr2 = [x.replace(",", "").strip() for x in arr2]
    bst1 = BinarySearchTree()
    bst2 = BinarySearchTree()
    root1 = bst1.build_bst(arr1)
    root2 = bst2.build_bst(arr2)

    soln = Solution()
    result = soln.check_if_two_bst_contains_same_elements(root1, root2)
    print(result)


if __name__ == "__main__":
    main()
