"""
You are given a BST(Binary Search Tree) with n number of nodes and value x. your task is to find the greatest value node of the BST which is smaller than or equal to x.
Note: when x is smaller than the smallest node of BST then returns -1.

Examples:

Input:
n = 7               2
                     \
                      81
                    /     \
                 42       87
                   \       \
                    66      90
                   /
                 45
x = 87
Output: 87
Explanation: 87 is present in tree so floor will be 87.

Input:
n = 4                     6
                           \
                            8
                          /   \
                        7       9
x = 11
Output: 9

Input:
n = 4                     6
                           \
                            8
                          /   \
                        7       9
x = 5
Output: -1

Constraint:
1 <= Node data <= 10^9
1 <= n <= 10^5

Expected Complexities
Time Complexity: O(height of tree)
Auxiliary Space: O(height of tree)
"""

import os, sys

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."))
from binary_search_tree_helper import BinarySearchTree


class Solution:
    def get_floor_ittr(self, root, x):
        if root is None:
            return -1

        curr = root
        floor_value = -1
        while curr:
            # Capturing the floor value of the current node data before going to next
            if curr.data <= x:
                floor_value = curr.data

            if curr.data < x:
                curr = curr.right
            elif curr.data > x:
                curr = curr.left
            else:
                return curr.data

        return floor_value

    def get_floor_rec(self, root, x, floor_value=-1):
        if root is None:
            return floor_value

        if root.data <= x:
            floor_value = root.data

        if root.data < x:
            return self.get_floor_rec(root.right, x, floor_value)
        elif root.data > x:
            return self.get_floor_rec(root.left, x, floor_value)
        else:
            return floor_value


def main():
    arr = input("Enter the tree level order: ").strip().split()
    x = int(input("Enter the value of x: ").strip())
    arr = [x.replace(",", "").strip() for x in arr]
    bst = BinarySearchTree()
    root = bst.build_bst(arr)
    bst.print_tree()

    soln = Solution()
    result = soln.get_floor_ittr(root, x)
    print(result)


if __name__ == "__main__":
    main()
