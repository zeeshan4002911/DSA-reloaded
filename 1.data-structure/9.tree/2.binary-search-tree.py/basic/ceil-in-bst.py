"""
You are given a root binary search tree and an integer x . Your task is to find the Ceil of x in the tree.
Note: Ceil(x) is a number that is either equal to x or is immediately greater than x.
If Ceil could not be found, return -1.

Examples:

Input: root = [5, 1, 7, N, 2, N, N, N, 3], x = 3

Output: 3
Explanation: We find 3 in BST, so ceil of 3 is 3.

Input: root = [10, 5, 11, 4, 7, N, N, N, N, N, 8], x = 6

Output: 7
Explanation: We find 7 in BST, so ceil of 6 is 7.

Constraints:
1  ≤ Number of nodes  ≤ 10^5
1  ≤ Value of nodes ≤ 10^5

Expected Complexities
Time Complexity: O(log n)
Auxiliary Space: O(1)
"""

import os, sys

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."))
from binary_search_tree_helper import BinarySearchTree


class Solution:
    def get_ceil_ittr(self, root, x):
        if root is None:
            return -1

        curr = root
        ceil_value = -1
        while curr:
            # Capturing the ceil value of the current node data before going to next
            if curr.data >= x:
                ceil_value = curr.data

            if curr.data < x:
                curr = curr.right
            elif curr.data > x:
                curr = curr.left
            else:
                return curr.data

        return ceil_value

    def get_ceil_rec(self, root, x, ceil_value=-1):
        if root is None:
            return ceil_value

        if root.data >= x:
            ceil_value = root.data

        if root.data < x:
            return self.get_ceil_rec(root.right, x, ceil_value)
        elif root.data > x:
            return self.get_ceil_rec(root.left, x, ceil_value)
        else:
            return ceil_value


def main():
    arr = input("Enter the tree level order: ").strip().split()
    x = int(input("Enter the value of x: ").strip())
    arr = [x.replace(",", "").strip() for x in arr]
    bst = BinarySearchTree()
    root = bst.build_bst(arr)
    bst.print_tree()

    soln = Solution()
    result = soln.get_ceil_ittr(root, x)
    print(result)


if __name__ == "__main__":
    main()
