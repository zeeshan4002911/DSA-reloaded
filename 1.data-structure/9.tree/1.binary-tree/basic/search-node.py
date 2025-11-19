"""
Given a Binary tree and a key. The task is to search and check if the given key exists in the binary tree or not.

Examples:

Input: root = [1, 2, 3], target = 4
        1
      /   \
     2     3
Output: 0

Input: root = [3, 2, 5, 1, 4], target = 4
         3
       /   \
      2     5
    /   \
   1     4
Output: 3

Constraints:
1 <= number of nodes<= 10^5
1 <= data of a node<= 10^5
1 <= target <= 10^5

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(h)
"""

import sys, os

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."))
from binary_tree_helper import BinaryTree


class Solution:
    def search_node(self, root, target):
        if root is None:
            return False

        if root.data == target:
            return True

        res_l = self.search_node(root.left, target)
        res_r = self.search_node(root.right, target)
        res = res_l or res_r
        return res


def main():
    arr = input("Enter tree in form of level order list: ").strip().split()
    target = input("Enter target: ").strip()
    arr = [None if val == "N" else val for val in arr]
    bt = BinaryTree()
    root = bt.build_tree(arr)

    soln = Solution()
    result = soln.search_node(root, target)
    print(result)


if __name__ == "__main__":
    main()
