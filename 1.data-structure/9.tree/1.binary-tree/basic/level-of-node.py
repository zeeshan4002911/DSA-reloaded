"""
Given a Binary Tree and a target key, you need to find the level of the target key in the given Binary Tree.

Note: The level of the root node is 1. If no such key exists then return 0.

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
from queue import Queue

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."))
from binary_tree_helper import BinaryTree


class Solution:
    def level_of_node(self, root, target, res=0):
        if root is None:
            return 0

        if root.data == target:
            return 1

        res_l = self.level_of_node(root.left, target, res)
        res_r = self.level_of_node(root.right, target, res)

        # Bactrack and add the value if it's coming from found
        if res_l > 0:
            res += res_l + 1
        elif res_r > 0:
            res += res_r + 1
        return res

    def level_of_node_ittr(self, root, target):
        if root is None:
            return 0

        queue = Queue()
        queue.put((root, 1))

        while not queue.empty():
            curr, level_num = queue.get()
            # Return level number once target is found
            if curr.data == target:
                return level_num

            if curr.left:
                queue.put((curr.left, level_num + 1))
            if curr.right:
                queue.put((curr.right, level_num + 1))

        # Target not exists in tree
        return 0


def main():
    arr = input("Enter tree in form of level order list: ").strip().split()
    target = input("Enter target: ").strip()
    arr = [None if val == "N" else val for val in arr]
    bt = BinaryTree()
    root = bt.build_tree(arr)

    soln = Solution()
    result = soln.level_of_node_ittr(root, target)
    print(result)


if __name__ == "__main__":
    main()
