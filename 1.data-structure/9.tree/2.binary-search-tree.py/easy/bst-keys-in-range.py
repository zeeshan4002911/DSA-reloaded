"""
Given a Binary Search Tree and a range [low, high]. Find all the numbers in the BST that lie in the given range.
Note: Element greater than or equal to root go to the right side.

Example 1:

Input:
       17
     /    \
    4     18
  /   \
 2     9 
l = 4, h = 24
Output: 
4 9 17 18 

Example 2:

Input:
       16
     /    \
    7     20
  /   \
 1    10
l = 13, h = 23
Output: 
16 20 

Your Task:
You don't need to read input or print anything. Your task is to complete the function printNearNodes() which takes the root Node of the BST and the range elements low and high as inputs and returns an array that contains the BST elements in the given range low to high (inclusive) in non-decreasing order.

Constraints:
1 ≤ Number of nodes ≤ 10^5
1 ≤ l ≤ h ≤ 10^6

"""

import os, sys

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."))
from binary_search_tree_helper import BinarySearchTree


class Solution:
    def bst_keys_in_range_ittr(self, root, low, high):
        return

    def bst_keys_in_range_rec(self, root, low, high):
        return self.bst_keys_in_range_rec_helper(root, low, high, [])

    def bst_keys_in_range_rec_helper(self, root, low, high, result):
        if root is None:
            return result

        # If it's within range then doing inorder traversal to get non-decreasing order result
        if low <= root.data <= high:
            self.bst_keys_in_range_rec_helper(root.left, low, high, result)
            result.append(root.data)
            self.bst_keys_in_range_rec_helper(root.right, low, high, result)

        # Going to right subtree if current node data is less than start range
        elif root.data < low:
            self.bst_keys_in_range_rec_helper(root.right, low, high, result)
        # Going to left subtree if current node data is greater than end range
        elif root.data > high:
            self.bst_keys_in_range_rec_helper(root.left, low, high, result)

        return result


def main():
    arr = input("Enter the tree level order: ").strip().split()
    low = int(input("Enter the value of low: ").strip())
    high = int(input("Enter the value of high: ").strip())
    arr = [x.replace(",", "").strip() for x in arr]
    bst = BinarySearchTree()
    root = bst.build_bst(arr)
    bst.print_tree()

    soln = Solution()
    result = soln.bst_keys_in_range_rec(root, low, high)
    print(result)


if __name__ == "__main__":
    main()
