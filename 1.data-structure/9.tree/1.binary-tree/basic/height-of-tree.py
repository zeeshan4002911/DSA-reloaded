"""
Given the root of a binary tree, your task is to find the maximum depth of the tree.

Note: The maximum depth or height of the tree is the number of edges in the tree from the root to the deepest node.

Examples:

Input: root = [12, 8, 18, 5, 11]

Output: 2
Explanation: One of the longest path from the root(node 12) goes through node 8 to node 5, which has 2 edges.

Input: root = [1, 2, 3, 4, N, 10, 5, N, N, N, N, 6, 7]

Output: 3
Explanation: The longest path from the root(node 1) to a leaf node 6 with 3 edges.

Constraints:
1 ≤ number of nodes ≤ 3*10^4
0 ≤ node->data ≤ 10^5

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(h)
"""

import sys, os
from queue import Queue

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."))
from binary_tree_helper import BinaryTree


class Traversal:
    def depth_of_tree(self, root):
        return self._helper(root, 0, 0)

    def _helper(self, node, curr_level, max_level):
        if node is None:
            return max_level

        max_level = max(max_level, curr_level)
        max_left_level = self._helper(node.left, curr_level + 1, max_level)
        max_right_level = self._helper(node.right, curr_level + 1, max_level)

        return max(max_right_level, max_left_level)

    def depth_of_tree_ittr(self, root):
        if root is None:
            return 0

        result = 0
        queue = Queue()
        queue.put((root, 0))

        while not queue.empty():
            curr, level_num = queue.get()
            result = max(result, level_num)

            if curr.left:
                queue.put((curr.left, level_num + 1))
            if curr.right:
                queue.put((curr.right, level_num + 1))

        return result


def main():
    arr = input("Enter tree in form of level order list: ").strip().split()
    arr = [None if val == "N" else val for val in arr]
    bt = BinaryTree()
    root = bt.build_tree(arr)
    # bt.print_tree()

    traversal = Traversal()
    # result = traversal.depth_of_tree(root)
    result = traversal.depth_of_tree_ittr(root)
    print(result)


if __name__ == "__main__":
    main()
